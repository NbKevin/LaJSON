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

Shortcut to the JSON parser.
"""

__author__ = 'Nb'

from ._parser import Parser
from ._util import PY_FLOAT_NAN


def parse(source: str, allow_nan=False, convert_nan_to=PY_FLOAT_NAN, allow_inf=False):
    """
    Parse JSON elements from string.

    :param allow_nan: when set to True, NaN would
        be converted to convert_nan_to, by default
        PY_FLOAT_NAN
    :param convert_nan_to: what to convert NaN to
    :param allow_inf: when set to True, Inf and
        -Inf would be converted to corresponding
        python floating point number
    """
    return Parser(source, allow_nan, convert_nan_to, allow_inf).parse().to_python()


def serialise(python_dict_or_list):
    """Convert python dict or list to JSON string.
    Note that NaN and Inf is not allowed."""
    return Parser.from_python(python_dict_or_list).__str__()
