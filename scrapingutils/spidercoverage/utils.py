import enum
import json
import yaml


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
