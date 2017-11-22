# -*- coding: utf-8 -*-

import os
import csv
import time
import sys
import yaml
from yaml.scanner import ScannerError
from enums import InstanciaStatus, DocumentoStatus, SpiderStatus


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
    'status': SpiderStatus,
    'captcha': bool,
    'arquivos': DocumentoStatus,
    '1-grau-fisico': InstanciaStatus,
    '2-grau-fisico': InstanciaStatus,
    '1-grau-eletronico': InstanciaStatus,
    '2-grau-eletronico': InstanciaStatus,
    'jec-1-grau-fisico': InstanciaStatus,
    'jec-2-grau-fisico': InstanciaStatus,
    'jec-1-grau-eletronico': InstanciaStatus,
    'jec-2-grau-eletronico': InstanciaStatus,
}

COVERAGE_TYPE = {
    '0': 'Não Existe',
    '1': 'Implementado',
    '2': 'Não implementado',
}


class CoverageCsvFactory(object):

    def create_row(self, sdc_dict):
        row = []
        for key, value in HEADER.items():
            if key in sdc_dict.keys():
                value = str(sdc_dict[key])
                import ipdb
                ipdb.set_trace()
                if value in COVERAGE_TYPE.keys():
                    value = COVERAGE_TYPE[value]
                row.append(value)
            else:
                row.append(None)
        return row

    @classmethod
    def export_data_coverage(results):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        with open('spider-report-%s.csv' % timestr, 'wb') as csvfile:
            coverage = csv.writer(csvfile, delimiter=';', quotechar='|')
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
                        coverage.writerow(create_row(sdc_subdict))
                else:
                    coverage.writerow(create_row(sdc_dict))
        print 'CSV EXPORTADO COM SUCESSO!'


if __name__ == '__main__':

    args = sys.argv

    if 'csv' in args:
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

        CoverageCsvFactory.export_data_coverage(spiders_results)
