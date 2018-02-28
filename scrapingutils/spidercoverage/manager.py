# -*- coding: utf-8 -*-

import os
import csv
import time
import sys
import yaml
from yaml.scanner import ScannerError
from enums import InstanciaStatus, DocumentoStatus, SpiderStatus
from utils import GoogleSheetCoverage


SCRAPY_SET = {
    'dir': 'tribunais_scrapy',
    'yaml': 'spider-scrapy.yml'
}

SELENIUM_SET = {
    'dir': 'tribunais_selenium',
    'yaml': 'spider-selenium.yml'
}

HEADER = {
    'name': None,
    'estado': None,
    'fonte': None,
    'justica': None,
    'status': SpiderStatus,
    'captcha': None,
    'arquivos': DocumentoStatus,
    'argumentos': None,
    '1-grau-fisico': InstanciaStatus,
    '2-grau-fisico': InstanciaStatus,
    '1-grau-eletronico': InstanciaStatus,
    '2-grau-eletronico': InstanciaStatus,
    'jec-1-grau-fisico': InstanciaStatus,
    'jec-2-grau-fisico': InstanciaStatus,
    'jec-1-grau-eletronico': InstanciaStatus,
    'jec-2-grau-eletronico': InstanciaStatus,
}


class CoverageCsvFactory(object):

    @classmethod
    def create_row(cls, sdc_dict):
        row = []
        for key, header_type in HEADER.items():
            if key in sdc_dict.keys():

                if header_type:
                    value = header_type(sdc_dict[key]).name
                else:
                    value = str(sdc_dict[key])

                row.append(value)
            else:
                row.append(None)
        return row

    @classmethod
    def export_data_coverage(cls, results):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        report_file_name = 'spider-report-{}.csv'.format(timestr)
        with open(report_file_name, 'wb') as csvfile:
            coverage = csv.writer(csvfile, delimiter=',', quotechar='|')
            coverage.writerow(HEADER.keys())
            for sdc_dict in results:
                # Spider que cobre mais de um estado
                if 'estados' in sdc_dict.keys():
                    for estado in sdc_dict['estados']:
                        sdc_subdict = sdc_dict
                        # Coverage especifico para cada estado
                        if 'coverage' in sdc_dict.keys():
                            if estado in sdc_dict['coverage']:
                                sdc_subdict.update(
                                    sdc_dict['coverage'][estado])
                            elif 'default' in sdc_dict['coverage']:
                                sdc_subdict.update(
                                    sdc_dict['coverage']['default']
                                )
                        sdc_subdict['estado'] = estado
                        coverage.writerow(cls.create_row(sdc_subdict))
                else:
                    coverage.writerow(cls.create_row(sdc_dict))
        print('CSV EXPORTADO COM SUCESSO!')
        return report_file_name


def main():
    spiders_results = []
    for settings in [SCRAPY_SET, SELENIUM_SET]:
        os.chdir(settings['dir'])

        try:
            os.system(
                "python spider-coverage.py yaml")
            cov_text = open(settings['yaml'], 'r')
            spiders_results.extend(yaml.load(cov_text))
            os.remove(settings['yaml'])
        except ScannerError as e:
            raise Exception(
                'Problemas ao ler o arquivo "%s".' % settings['yaml'])
        except IOError as e:
            print ('Arquivo da spider não localizado "%s".' %
                   settings['yaml'])

        os.chdir('..')

    report_file_name = CoverageCsvFactory.export_data_coverage(spiders_results)

    google_sc = GoogleSheetCoverage()
    google_sc.update_csv_sheet(report_file_name)
