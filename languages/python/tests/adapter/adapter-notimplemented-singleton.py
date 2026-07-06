import builtins
import importlib
from builtins import NotImplemented as imported_not_implemented


bool_type_error = False
try:
    bool(NotImplemented)
except TypeError:
    bool_type_error = True

not_type_error = False
try:
    not NotImplemented
except TypeError:
    not_type_error = True

and_type_error = False
try:
    NotImplemented and True
except TypeError:
    and_type_error = True

or_type_error = False
try:
    NotImplemented or False
except TypeError:
    or_type_error = True

conditional_type_error = False
try:
    1 if NotImplemented else 2
except TypeError:
    conditional_type_error = True

if_type_error = False
try:
    if NotImplemented:
        if_marker = 1
except TypeError:
    if_type_error = True

while_type_error = False
try:
    while NotImplemented:
        while_marker = 1
except TypeError:
    while_type_error = True

assert_type_error = False
try:
    assert NotImplemented, "unused"
except TypeError:
    assert_type_error = True

float_type_error = False
try:
    float(NotImplemented)
except TypeError:
    float_type_error = True

complex_type_error = False
try:
    complex(NotImplemented)
except TypeError:
    complex_type_error = True

star_original = NotImplemented
NotImplemented = 17
from builtins import *
star_rebound = NotImplemented is star_original

via_importlib = importlib.import_module("builtins")

result = (
    NotImplemented is star_original
    and imported_not_implemented is NotImplemented
    and builtins.NotImplemented is NotImplemented
    and getattr(builtins, "NotImplemented") is NotImplemented
    and via_importlib.NotImplemented is NotImplemented
    and NotImplemented == imported_not_implemented
    and not (NotImplemented != imported_not_implemented)
    and NotImplemented is not None
    and NotImplemented is not True
    and NotImplemented is not False
    and NotImplemented is not Ellipsis
    and NotImplemented != None
    and NotImplemented != True
    and NotImplemented != False
    and NotImplemented != Ellipsis
    and NotImplemented != 17
    and NotImplemented != "NotImplemented"
    and str(NotImplemented) == "NotImplemented"
    and repr(NotImplemented) == "NotImplemented"
    and ascii(NotImplemented) == "NotImplemented"
    and format(NotImplemented) == "NotImplemented"
    and isinstance(hash(NotImplemented), int)
    and bool_type_error
    and not_type_error
    and and_type_error
    and or_type_error
    and conditional_type_error
    and if_type_error
    and while_type_error
    and assert_type_error
    and float_type_error
    and complex_type_error
    and star_rebound
)

result
