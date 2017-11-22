import enum


def raw_value(coverage_dict):
    for key, init_value in coverage_dict.items():
        if isinstance(init_value, enum.Enum):
            coverage_dict.update({key: init_value.value})
    return coverage_dict
