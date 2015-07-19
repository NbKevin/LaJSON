#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
Definition of JSON elements.
"""

__author__ = 'Nb'

from la_json._util import Stack


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

    __repr__ = __str__


class JSONKVPair:
    """
    A JSON key-value pair.
    """

    def __init__(self):
        self.key = Undefined
        self.value = Undefined

    def __str__(self):
        if isinstance(self.value, str):
            return '"%s": "%s"' % (self.key, self.value)
        else:
            return '"%s": %s' % (self.key, self.value)

    __repr__ = __str__


class JSONArray(JSONElement):
    """
    A JSON array.
    """

    def __init__(self):
        super(JSONArray, self).__init__()
        self.array = []

    def __str__(self):
        return str(self.array)

    def to_python(self):
        return [
            item.to_python()
            if isinstance(item, JSONObject) or isinstance(item, JSONArray)
            else item
            for item in self.array
            ]

    __repr__ = __str__


class JSONIdentifier:
    """
    JSON identifiers.
    """
    SET = ('true', 'false', 'null')
    TO_PYTHON_DICT = {
        'true': True,
        'false': False,
        'null': None
    }


Undefined = JSONUndefined()
