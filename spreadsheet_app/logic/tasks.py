from spreadsheet_app.logic.google_sheets_handler import GoogleSheetsHandler
from spreadsheet_app.models import Order
from datetime import datetime
import urllib.request
import urllib.error
import xml.etree.cElementTree as ET
from test_kanalservis_project.celery import app


def get_dollar_value_curs():
    """ Получить курс доллара """
    url_cbr = 'https://www.cbr.ru/scripts/XML_daily.asp'
    try:
        xml_file = urllib.request.urlopen(url_cbr)
    except urllib.error.HTTPError as e:
        print('Error code: ', e)
        return
    except urllib.error.URLError as e:
        print('Reason: ', e)
        return
    tree = ET.ElementTree(file=xml_file)
    root = tree.getroot()
    dollar_data = root.find("Valute[@ID='R01235']")
    dollar_value_curs = float(dollar_data.find("Value").text.replace(",", "."))
    return dollar_value_curs


def validation_row(row):
    """ Изменение типа данных в строке таблицы """
    id_n, order_number, cost_in_dollar, delivery_time_str = row
    try:
        id_n = int(id_n)
        order_number = int(order_number)
        cost_in_dollar = float(cost_in_dollar)
        delivery_time = datetime.strptime(delivery_time_str, '%d.%m.%Y')
    except ValueError:
        return
    except TypeError:
        return

    return id_n, order_number, cost_in_dollar, delivery_time


@app.task()
def get_and_write_an_order_in_the_database():
    """ Обновление заказов в БД """

    # Получение всех заказов из Гугл таблицы
    google_sheet = GoogleSheetsHandler()
    orders_from_the_table = google_sheet.get_data('ROWS', 'A:D')['values'][1:]
    del google_sheet

    # Получение курса доллара
    dollar_value_curs = get_dollar_value_curs()

    list_rows = []  # Список номеров строк таблицы, для удаления не входящих в него заказов из БД

    for row in orders_from_the_table:
        try:
            id_n, order_number, cost_in_dollar, delivery_time = validation_row(row)
        except TypeError:
            # Если строка таблицы не прошла валидацию, то пропускаем её
            continue

        # Обновляем или создаём заказы, полученные по № строки из таблицы. № условно привязан к id(БД).
        availability_update = Order.objects.filter(id=id_n).update(
            order_number=order_number,
            cost_in_dollar=cost_in_dollar,
            delivery_time=delivery_time
        )
        if not availability_update and dollar_value_curs:
            # Если объект не найден и курс доллара получен, то создаём

            cost_in_rubles = round(cost_in_dollar * dollar_value_curs, 2)   # Перевод в рубли

            Order.objects.create(
                id=id_n,
                order_number=order_number,
                cost_in_dollar=cost_in_dollar,
                delivery_time=delivery_time,
                cost_in_rubles=cost_in_rubles
            )

        list_rows.append(id_n)

    # Удаление заказов из БД,
    orders_bd = Order.objects.all().values_list('id', flat=True)
    for order_bd in orders_bd:
        if order_bd not in list_rows:
            # Если заказа из таблицы нет в БД, то удаляем
            Order.objects.get(id=order_bd).delete()
