#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
Copyright 2015 Nb<k.memo@live.cn>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Definition of JSON elements.
"""

__author__ = 'Nb'

from ._util import Stack, PY_FLOAT_INF, PY_FLOAT_NEG_INF, JSONNonStandardElementError


class JSONElement:
    """
    A JSON element.
    """


class JSONItem(JSONElement):
    """
    A JSON item.
    """


class JSONUndefined(JSONItem):
    def __str__(self):
        return 'Undefined'

    __repr__ = __str__


class JSONContainer(JSONElement):
    """
    A JSON container.
    """

    def __init__(self):
        """Create a JSON element."""
        self.content_stack = Stack()


class JSONObject(JSONContainer):
    """
    A JSON object.
    """

    def __init__(self):
        super(JSONObject, self).__init__()
        self.kv_pairs = []

    def __str__(self):
        return ''.join(['{', str(self.kv_pairs)[1:-1], '}'])

    def to_python(self):
        """Convert a JSONObject to python dict."""
        return {
            kv.key: kv.value.to_python()
            if isinstance(kv.value, JSONObject) or isinstance(kv.value, JSONArray)
            else kv.value
            for kv in self.kv_pairs
            }

    @staticmethod
    def from_python(python_dict: dict):
        """Convert a python dict to JSONObject."""
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


class JSONKVPair(JSONItem):
    """
    A JSON key-value pair.
    """

    def __init__(self):
        self.key = Undefined
        self.value = Undefined

    def __str__(self):
        if self.value != self.value:
            raise JSONNonStandardElementError(
                message='JSON standard does not include NaN, cannot create non standard JSON string'
            )
        elif self.value in [PY_FLOAT_INF, PY_FLOAT_NEG_INF]:
            raise JSONNonStandardElementError(
                message='JSON standard does not include Inf, cannot create non standard JSON string'
            )
        if isinstance(self.value, str):
            return '"%s": "%s"' % (self.key.replace('"', r'\"'), self.value.replace('"', r'\"'))
        else:
            return '"%s": %s' % (self.key.replace('"', r'\"'), JSONIdentifier.parse_python_keyword(self.value))

    __repr__ = __str__


class JSONArray(JSONContainer):
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
                             else JSONIdentifier.parse_python_keyword(item)
                             for item in self.array]
                        ),
                        ']'])

    def to_python(self):
        """Convert a JSONArray to python list."""
        return [
            item.to_python()
            if isinstance(item, JSONObject) or isinstance(item, JSONArray)
            else item
            for item in self.array
            ]

    @staticmethod
    def from_python(python_list: list):
        """Convert a python list to JSONArray."""
        json_array = JSONArray()
        for item in python_list:
            if isinstance(item, dict):
                json_item = JSONObject.from_python(item)
            elif isinstance(item, list):
                json_item = JSONArray.from_python(item)
            else:
                if item != item:
                    raise JSONNonStandardElementError(
                        message='JSON standard does not include NaN, cannot create non standard JSON string'
                    )
                elif item in [PY_FLOAT_INF, PY_FLOAT_NEG_INF]:
                    raise JSONNonStandardElementError(
                        message='JSON standard does not include Inf, cannot create non standard JSON string'
                    )
                json_item = item
            json_array.array.append(json_item)
        return json_array

    __repr__ = __str__


class JSONIdentifier(JSONItem):
    """
    JSON identifiers.
    """
    IDENTIFIER_SET = ('true', 'false', 'null')
    PYTHON_SET = (True, False, None)
    IDENTIFIER_TO_PYTHON_DICT = {
        'true': True,
        'false': False,
        'null': None
    }
    PYTHON_TO_IDENTIFIER_DICT = {
        True: 'true',
        False: 'false',
        None: 'null'
    }
    EXTENDED_FLOAT_NUMBERS = ('nan', 'inf', '-inf', 'infinity', '-infinity')
    EXTENDED_FLOAT_NUMBERS_TO_PYTHON = {
        'inf': PY_FLOAT_INF,
        'infinity': PY_FLOAT_INF,
        '-inf': PY_FLOAT_NEG_INF,
        '-infinity': PY_FLOAT_NEG_INF
    }

    @staticmethod
    def parse_python_keyword(item) -> str:
        """Parse python keyword."""
        if item in JSONIdentifier.PYTHON_SET and item != 0 and item != 1:
            return JSONIdentifier.PYTHON_TO_IDENTIFIER_DICT[item]
        return str(item)


Undefined = JSONUndefined()
