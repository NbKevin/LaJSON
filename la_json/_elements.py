#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
Definition of JSON elements.
"""

__author__ = 'Nb'

from ._util import Stack, PY_FLOAT_INF, PY_FLOAT_NEG_INF, JSONNonStandardElementError


class JSONUndefined:
    def __str__(self):
        return 'Undefined'

    __repr__ = __str__


class JSONElement:
    """
    Base element. Abstract.
    """

    def __init__(self):
        """Create a JSON element."""
        self.content_stack = Stack()


class JSONObject(JSONElement):
    """
    A JSON object.
    """

    start_set = '{'
    end_set = '}'

    def __init__(self):
        super(JSONObject, self).__init__()
        self.kv_pairs = []

    def __str__(self):
        return ''.join(['{', str(self.kv_pairs)[1:-1], '}'])

    def to_python(self):
        return {
            kv.key: kv.value.to_python()
            if isinstance(kv.value, JSONObject) or isinstance(kv.value, JSONArray)
            else kv.value
            for kv in self.kv_pairs
            }

    @staticmethod
    def from_python(python_dict: dict):
        json_object = JSONObject()
        for k, v in python_dict.items():
            kv_pair = JSONKVPair()
            kv_pair.key = k
            if isinstance(v, dict):
                kv_pair.value = JSONObject.from_python(v)
            elif isinstance(v, list):
                kv_pair.value = JSONArray.from_python(v)
            else:
                kv_pair.value = v
            json_object.kv_pairs.append(kv_pair)
        return json_object

    __repr__ = __str__


class JSONKVPair:
    """
    A JSON key-value pair.
    """

    def __init__(self):
        self.key = Undefined
        self.value = Undefined

    def __str__(self):
        if self.value != self.value:
            raise JSONNonStandardElementError(
                'JSON standard does not include NaN, cannot create non standard JSON string'
            )
        elif self.value in [PY_FLOAT_INF, PY_FLOAT_NEG_INF]:
            raise JSONNonStandardElementError(
                'JSON standard does not include Inf, cannot create non standard JSON string'
            )
        if isinstance(self.value, str):
            return '"%s": "%s"' % (self.key.replace('"', r'\"'), self.value.replace('"', r'\"'))
        else:
            return '"%s": %s' % (self.key.replace('"', r'\"'), self.value)

    __repr__ = __str__


class JSONArray(JSONElement):
    """
    A JSON array.
    """

    def __init__(self):
        super(JSONArray, self).__init__()
        self.array = []

    def __str__(self):
        return ''.join(['[',
                        ', '.join(
                            [''.join(['"', item.replace('"', r'\"'), '"'])
                             if isinstance(item, str)
                             else str(item)
                             for item in self.array]
                        ),
                        ']'])

    def to_python(self):
        return [
            item.to_python()
            if isinstance(item, JSONObject) or isinstance(item, JSONArray)
            else item
            for item in self.array
            ]

    @staticmethod
    def from_python(python_list: list):
        json_array = JSONArray()
        for item in python_list:
            if isinstance(item, dict):
                json_item = JSONObject.from_python(item)
            elif isinstance(item, list):
                json_item = JSONArray.from_python(item)
            else:
                if item != item:
                    raise JSONNonStandardElementError(
                        'JSON standard does not include NaN, cannot create non standard JSON string'
                    )
                elif item in [PY_FLOAT_INF, PY_FLOAT_NEG_INF]:
                    raise JSONNonStandardElementError(
                        'JSON standard does not include Inf, cannot create non standard JSON string'
                    )
                json_item = item
            json_array.array.append(json_item)
        return json_array

    __repr__ = __str__


class JSONIdentifier:
    """
    JSON identifiers.
    """
    IDENTIFIER_SET = ('true', 'false', 'null')
    IDENTIFIER_TO_PYTHON_DICT = {
        'true': True,
        'false': False,
        'null': None
    }
    EXTENDED_FLOAT = ('nan', 'inf', '-inf', 'infinity', '-infinity')
    EXTENDED_FLOAT_TO_PYTHON_DICT = {
        'inf': PY_FLOAT_INF,
        'infinity': PY_FLOAT_INF,
        '-inf': PY_FLOAT_NEG_INF,
        '-infinity': PY_FLOAT_NEG_INF
    }


Undefined = JSONUndefined()
