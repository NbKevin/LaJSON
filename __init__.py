#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
Shortcut to the JSON parser.
"""

__author__ = 'Nb'

import _parser


def parse(source: str):
    """Parse JSON elements from string."""
    return _parser.Parser(source).parse().to_python()


with open('test/test_1.json') as f:
    parse(f.read())
