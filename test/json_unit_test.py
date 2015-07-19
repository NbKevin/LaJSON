#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
The parser.
"""

__author__ = 'Kevin'

import unittest

from la_json import parse, serialise


class JSONUnitTest(unittest.TestCase):
    def test_parse_json(self):
        self.maxDiff = None
        with open('test_1.json') as json_1:
            test_1_json = parse(json_1.read())
            self.assertEqual(test_1_json, {
                "Float": 1.5,
                "NFloat": -1.55,
                "Int": 16,
                "NInt": -16,
                "SaveLocation": "C:/Users/Kevin/Desktop/R",
                "Threads": 16,
                "EnterURL": [],
                "URL": [],
                "Py": {
                    "Pypy": 3.5,
                    "CPython": [
                        2.7,
                        3.4,
                        {
                            "PYTHON": "I LOVE IT",
                            "true": True,
                            "false": False,
                            "null": None,
                            "set": [
                                True,
                                False,
                                None
                            ]
                        }
                    ]
                },
                "URL2": [
                    "http://bvb-fanabteilung.de/fotos/saison-20142015/33-spieltag-vfl-wolfsburg-borussia-dortmund/",
                    "http://bvb-fanabteilung.de/fotos/saison-20142015/34-spieltag-borussia-dortmund-sv-werder-bremen/"
                ]
            })

    def test_serialise_json(self):
        with open('test_2.json') as f:
            test_2_json = parse(f.read())
        self.assertEqual(test_2_json, {
            "AAA": "SS",
            "P\"P": [12, 26, 78, {
                "BB": "CC",
                "DD": -12.5
            }, "X\"D"],
            "ESCAPE": "\""
        })
        self.assertEqual(test_2_json, parse(serialise(test_2_json)))


if __name__ == '__main__':
    unittest.main()
