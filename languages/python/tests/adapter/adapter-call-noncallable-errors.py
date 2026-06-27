def zero():
    return 0


callee = 3
den = 0
list_callee = [1]

one_arg_error = False
try:
    callee(1)
except TypeError:
    one_arg_error = True

list_call_error = False
try:
    list_callee(0)
except TypeError:
    list_call_error = True

arg_eval_error = False
try:
    callee(1 // 0)
except ZeroDivisionError:
    arg_eval_error = True

func_eval_error = False
try:
    (1 // den)(zero())
except ZeroDivisionError:
    func_eval_error = True

multi_arg_error = False
try:
    callee(1, 2)
except TypeError:
    multi_arg_error = True

kw_arg_error = False
try:
    callee(x=1)
except TypeError:
    kw_arg_error = True

mixed_arg_error = False
try:
    callee(1, x=2)
except TypeError:
    mixed_arg_error = True

kw_eval_error = False
try:
    callee(x=1 // 0)
except ZeroDivisionError:
    kw_eval_error = True

result = (
    (lambda x: x)(3) == 3
    and one_arg_error
    and list_call_error
    and arg_eval_error
    and func_eval_error
    and multi_arg_error
    and kw_arg_error
    and mixed_arg_error
    and kw_eval_error
)
assert result
result
