def mark_type_error(thunk):
    try:
        thunk()
    except TypeError:
        return True
    return False


empty_args = []
empty_kwargs = {}


def object_with_argument():
    object(1)


def object_with_keyword():
    object(x=1)


def object_with_mixed_argument():
    object(1, **empty_kwargs)


def object_with_star_argument():
    object(*[1])


o1 = object()
o2 = object()
o3 = object(*empty_args)
o4 = object(**empty_kwargs)
o5 = object(*empty_args, **empty_kwargs)


def int_object():
    int(o1)


def float_object():
    float(o1)


def complex_object():
    complex(o1)


identity_and_type = (
    type(o1) is object
    and o1.__class__ is object
    and getattr(o1, "__class__") is object
    and hasattr(o1, "__class__")
    and isinstance(o1, object)
    and not isinstance(o1, type)
    and bool(o1)
    and not callable(o1)
    and o1 is o1
    and not (o1 is o2)
    and o1 == o1
    and not (o1 == o2)
)

constructor_forms = (
    o3.__class__ is object
    and o4.__class__ is object
    and o5.__class__ is object
    and not (o3 is o4)
    and not (o4 is o5)
)

hash_and_mapping = (
    isinstance(hash(o1), int)
    and hash(o1) == hash(o1)
    and {o1: "first", o2: "second"}[o1] == "first"
    and {o1, o2} == {o2, o1}
)

error_paths = (
    mark_type_error(object_with_argument)
    and mark_type_error(object_with_keyword)
    and mark_type_error(object_with_mixed_argument)
    and mark_type_error(object_with_star_argument)
    and mark_type_error(int_object)
    and mark_type_error(float_object)
    and mark_type_error(complex_object)
)

result = identity_and_type and constructor_forms and hash_and_mapping and error_paths

result
