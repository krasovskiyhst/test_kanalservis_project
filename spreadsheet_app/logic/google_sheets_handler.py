import os
from django.conf import settings
import httplib2
from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheetsHandler:
    """
    Класс-обертка для работы с Google Таблицами
    """

    def __init__(self):
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(settings.CREDENTIALS_FILE, [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'])
        self.httpAuth = self.credentials.authorize(httplib2.Http())
        self.service = discovery.build('sheets', 'v4', http=self.httpAuth)
        self.spreadsheet_id = settings.SPREADSHEET_ID
        self.sheet_id = settings.SHEET_ID
        self.sheet_title = self._get_title()

    def _get_title(self):
        """
        Получить название листа при создании объекта "Обработчик таблицы"
        :return:
        """
        sheets_titles = self.service.spreadsheets().get(spreadsheetId=self.spreadsheet_id,
                                                        fields='sheets(properties(sheetId,title))').execute()
        list_sheet_properties = sheets_titles['sheets']
        for sheet_properties in list_sheet_properties:
            if sheet_properties['properties']['sheetId'] == self.sheet_id:
                return sheet_properties['properties']['title']

        return None

    def get_data(self, major_dimension, cell_range=None):
        """
        Получение данных листа (sheet)
        :param major_dimension: ROWS(читать построчно) или COLUMNS(читать по колонкам)
        :param cell_range: Диапазон ячеек. Пример "B1:B" - только вторая колонка
        :return: {'range': "'Лист1'!A1:AB1000", 'majorDimension': 'ROWS', 'values': [[...]]}
        """
        sheet_title_range = self.sheet_title
        if cell_range:
            # Если диапазон ячеек указан, то склеиваем с названием листа
            sheet_title_range = self.sheet_title + '!' + cell_range

        values = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=sheet_title_range,
            majorDimension=major_dimension
        ).execute()
        return values


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_kanalservis_project.settings")
    s = GoogleSheetsHandler()
    print(s.get_data('ROWS', 'A:D'))
