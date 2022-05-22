from test_kanalservis_project.celery import app


@app.task()
def get_and_write_an_order_in_the_database():
    """ Обновление заказов в БД """
    pass

