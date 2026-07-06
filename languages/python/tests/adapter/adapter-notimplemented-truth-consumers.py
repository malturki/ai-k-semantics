def mark_type_error(thunk):
    try:
        thunk()
    except TypeError:
        return True
    return False


def all_list_case():
    all([NotImplemented])


def all_tuple_case():
    all((1, NotImplemented))


def all_iterator_case():
    all(iter([NotImplemented]))


def any_list_case():
    any([0, NotImplemented])


def any_tuple_case():
    any((NotImplemented,))


def any_iterator_case():
    any(iter([NotImplemented]))


def filter_none_case():
    list(filter(None, [NotImplemented]))


def filter_predicate_case():
    list(filter(lambda value: NotImplemented, [1]))


def sorted_reverse_case():
    sorted([1], reverse=NotImplemented)


def sorted_key_reverse_case():
    sorted([1], key=lambda value: value, reverse=NotImplemented)


def sorted_reverse_key_case():
    sorted([1], reverse=NotImplemented, key=lambda value: value)


def zip_strict_case():
    list(zip([1], strict=NotImplemented))


def map_strict_case():
    list(map(lambda value: value, [1], strict=NotImplemented))


def list_comp_case():
    [value for value in [1] if NotImplemented]


def list_comp_filters_case():
    [value for value in [1] if True if NotImplemented]


def list_comp_target_case():
    [left for (left, right) in [(1, 2)] if NotImplemented]


def set_comp_case():
    {value for value in [1] if NotImplemented}


def set_comp_filters_case():
    {value for value in [1] if True if NotImplemented}


def set_comp_target_case():
    {left for (left, right) in [(1, 2)] if NotImplemented}


def dict_comp_case():
    {value: value for value in [1] if NotImplemented}


def dict_comp_filters_case():
    {value: value for value in [1] if True if NotImplemented}


def dict_comp_target_case():
    {left: right for (left, right) in [(1, 2)] if NotImplemented}


def gen_exp_case():
    list(value for value in [1] if NotImplemented)


result = (
    mark_type_error(all_list_case)
    and mark_type_error(all_tuple_case)
    and mark_type_error(all_iterator_case)
    and mark_type_error(any_list_case)
    and mark_type_error(any_tuple_case)
    and mark_type_error(any_iterator_case)
    and mark_type_error(filter_none_case)
    and mark_type_error(filter_predicate_case)
    and mark_type_error(sorted_reverse_case)
    and mark_type_error(sorted_key_reverse_case)
    and mark_type_error(sorted_reverse_key_case)
    and mark_type_error(zip_strict_case)
    and mark_type_error(map_strict_case)
    and mark_type_error(list_comp_case)
    and mark_type_error(list_comp_filters_case)
    and mark_type_error(list_comp_target_case)
    and mark_type_error(set_comp_case)
    and mark_type_error(set_comp_filters_case)
    and mark_type_error(set_comp_target_case)
    and mark_type_error(dict_comp_case)
    and mark_type_error(dict_comp_filters_case)
    and mark_type_error(dict_comp_target_case)
    and mark_type_error(gen_exp_case)
)

result
