module_value = 10
shadow = 100


def read_global():
    return module_value + 1


def local_frame(arg):
    module_value = arg + 1
    local_only = module_value + 1
    return local_only


local_result = local_frame(5)

function_local_missing = False
try:
    local_only
except NameError:
    function_local_missing = True


class FrameClass:
    seen_global = module_value
    class_local = seen_global + 2
    shadow = 3


class_local_missing = False
try:
    class_local
except NameError:
    class_local_missing = True

comp_values = [shadow + item for shadow in [1, 2] for item in [10]]

comp_item_missing = False
try:
    item
except NameError:
    comp_item_missing = True

result = (
    read_global() == 11
    and local_result == 7
    and module_value == 10
    and function_local_missing
    and FrameClass.seen_global == 10
    and FrameClass.class_local == 12
    and FrameClass.shadow == 3
    and class_local_missing
    and comp_values == [11, 12]
    and shadow == 100
    and comp_item_missing
)

result
