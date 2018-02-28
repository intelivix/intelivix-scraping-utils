import enum
import gspread
import json
import os
import yaml
from oauth2client.service_account import ServiceAccountCredentials

from constants import KEY_FILE_DICT


def raw_value(coverage_dict):
    for key, init_value in coverage_dict.items():
        if isinstance(init_value, enum.Enum):
            coverage_dict.update({key: init_value.value})
        elif isinstance(init_value, dict):
            coverage_dict.update({key: raw_value(init_value)})
    return coverage_dict


class SpiderDataCoverage(object):

    def __init__(self, yaml_file, spiders):
        self._results = None
        self.spiders = spiders
        self._yaml_file = yaml_file

    @property
    def results(self):
        if not self._results:
            self._results = []
            for spider_cls in self.spiders:
                self._results.append(json.loads(spider_cls.output_json()))
        return self._results

    def export_spider_coverage_yaml(self):
        with open(self._yaml_file, 'w') as yaml_file:
            yaml.dump(self.results, yaml_file, default_flow_style=False)


class GoogleSheetCoverage(object):

    sheet_title = 'Tribunais Coverage'

    def get_credentials(self):
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        dirname = os.path.dirname(os.path.abspath(__file__))
        key_file_path = dirname + '/credentials/tribunais-coverage.json'

        return ServiceAccountCredentials.from_json_keyfile_dict(
            KEY_FILE_DICT, scope
        )

    def update_csv_sheet(self, coverage_csv_name):
        gsheet_client = gspread.authorize(self.get_credentials())

        if not gsheet_client.openall(title=self.sheet_title):
            spread_sheet = gsheet_client.create(self.sheet_title)
            spread_sheet.share(
                'robo_intelivix@intelivix.com',
                perm_type='user',
                role='writer'
            )

        spread_sheet = gc.open(self.sheet_title)

        with open(coverage_csv_name) as csv_file:
            data = csv_file.read()
            gsheet_client.import_csv(spread_sheet.id, data)
