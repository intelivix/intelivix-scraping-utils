import enum


def raw_value(coverage_dict):
    for key, init_value in x.items():
        if type(init_value) == enum.EnumMeta:
            coverage_dict.update({key: init_value.value})
    return coverage_dict