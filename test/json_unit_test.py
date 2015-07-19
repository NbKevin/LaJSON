#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
The parser.
"""

__author__ = 'Kevin'

import unittest

from la_json import _parser


class JSONUnitTest(unittest.TestCase):
    def test_1(self):
        self.maxDiff = None
        with open('test_1.json') as json_1:
            test_1_json = _parser.Parser(json_1.read()).parse().to_python()
            self.assertEqual(test_1_json, {
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
                    "http://bvb-fanabteilung.de/fotos/saison-20142015/34-spieltag-borussia-dortmund-sv-werder-bremen/",
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    }, {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    {
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
                    }
                ]
            })


if __name__ == '__main__':
    unittest.main()
