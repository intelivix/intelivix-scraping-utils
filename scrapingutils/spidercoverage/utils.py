import enum


def raw_value(coverage_dict):
    for key, init_value in coverage_dict.items():
        if isinstance(init_value, enum.Enum):
            coverage_dict.update({key: init_value.value})
        elif isinstance(init_value, dict):
            coverage_dict.update({key: raw_value(init_value)})
    return coverage_dict
