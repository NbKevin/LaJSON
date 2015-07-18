##Introduction
LaJSON is a pure python JSON parser. To be honest, it is an result of coincidence
while learning those compiler things.

##How to use
```
>>> from la_json import parse
>>> parse('{"A": ["B": true]}')
{'A': ['B': True]}
```