##Introduction
LaJSON is a pure python JSON parser. To be honest, it is just a result of 
coincidence while learning those compiler things.

##How to use
``` python
>>> from la_json import parse, serialise
>>> parse(r'{"A": ["B\"", true]}')
{'A': ['B"': True]}
>>> serialise({'A': 'B"', 'C"': [12, 25.5, 13.7]})
'{"A": "B\\"", "C\\"": [12, 25.5, 13.7]}'
```
Note that only builtin-type of python is supported now and an object key 
can only be of the type string.

##NaN and Inf
IEEE standard includes NaN and Inf which is refused by the JSON standard.
LaJSON allows you to parse NaN and Inf by passing `allow_nan=True` and `
allow_inf=True` to the parser. An additional `convert_nan_to=PY_FLOAT_NAN`
allows you to control which value NaN should be converted to since `NaN` is
not a meaningful number.
However, `NaN` and `Inf` is not supported during serialisation considering
that they are not a part of the standard and thus not recommended to be used.

##Licence
LaJSON is released under Apache License 2.0. See the LICENSE file for more
information.
