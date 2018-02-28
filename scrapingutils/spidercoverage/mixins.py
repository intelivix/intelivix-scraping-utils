# -*- coding: utf-8 -*-

import json

from utils import raw_value
from constants import DEFAULT_COVERAGE, ESTADOS_BRASIL


class SpiderCoverageMixin(object):
    default_coverage = DEFAULT_COVERAGE

    @classmethod
    def check_multiple_coverage(cls, coverage_fields):
        inter = len(set(ESTADOS_BRASIL).intersection(set(coverage_fields)))
        if inter > 0 or 'default' in coverage_fields:
            return True
        return False

    @classmethod
    def check_default_coverage(cls):
        coverage = getattr(cls, 'coverage', {})
        return cls.default_coverage != coverage

    @classmethod
    def check_coverage(cls):
        default_fields = DEFAULT_COVERAGE.keys()
        coverage = getattr(cls, 'coverage', {})

        coverage_fields = coverage.keys()
        if cls.check_multiple_coverage(coverage_fields):
            for value in coverage.values():
                if not set(default_fields).issubset(value.keys()):
                    return False
            return True

        elif set(default_fields).issubset(coverage_fields):
            return True
        return False

    @classmethod
    def test_spider(cls):
        if ('extrair' not in getattr(cls, 'name', '') and
                not getattr(cls, 'skip_coverage', False)):
            if not cls.check_default_coverage():
                raise Exception(
                    u'Spider coverage arguments are equal to default')
            if not cls.check_coverage():
                raise Exception(u'Error on spider coverage arguments')

    @classmethod
    def output_json(cls):
        output = {}
        # Required Fields
        for arg in ['name', 'fonte', 'justica']:
            arg_dict = {arg: getattr(cls, arg, '')}
            output.update(arg_dict)

        # Estados
        if hasattr(cls, 'estados_config'):
            estados = [estado_dict['meta']['estado']
                       for estado_dict in getattr(cls, 'estados_config', '')]
            output.update({'estados': estados})
        elif hasattr(cls, 'estados'):
            output.update({'estados': getattr(cls, 'estados', '')})
        else:
            output.update({'estado': getattr(cls, 'estado', '')})

        # Coverage
        coverage = getattr(cls, 'coverage', {})
        if cls.check_multiple_coverage(coverage.keys()):
            output.update({'coverage': raw_value(coverage)})
        else:
            output.update(raw_value(getattr(cls, 'coverage', {})))

        # Arguments
        valid_args = set([
            'nome',
            'documento',
            'numero',
            'advogado',
            'oab',
            'cnpj',
            'cpf'
        ])
        args_set = set(getattr(cls, 'optional_args', {}))
        args_list = list(args_set.intersection(valid_args))
        if args_list:
            argumentos = '; '.join(args_list)
            output.update({'argumentos': argumentos})

        return json.dumps(output, ensure_ascii=False)
