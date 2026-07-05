import keyword as kwmod
from keyword import iskeyword as ik
from keyword import issoftkeyword
from keyword import kwlist as imported_kwlist
from keyword import softkwlist


expected_all = ["iskeyword", "issoftkeyword", "kwlist", "softkwlist"]
expected_kwlist = [
    "False",
    "None",
    "True",
    "and",
    "as",
    "assert",
    "async",
    "await",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "with",
    "yield",
]
expected_softkwlist = ["_", "case", "match", "type"]

result = (
    kwmod.__name__ == "keyword"
    and kwmod.__all__ == expected_all
    and kwmod.kwlist == expected_kwlist
    and imported_kwlist == expected_kwlist
    and kwmod.softkwlist == expected_softkwlist
    and softkwlist == expected_softkwlist
    and callable(kwmod.iskeyword)
    and callable(issoftkeyword)
    and kwmod.iskeyword is ik
    and kwmod.iskeyword == ik
    and ik("if")
    and ik("async")
    and not ik("match")
    and not ik(1)
    and issoftkeyword("_")
    and issoftkeyword("case")
    and issoftkeyword("match")
    and issoftkeyword("type")
    and not issoftkeyword("if")
    and not issoftkeyword(None)
)

result
