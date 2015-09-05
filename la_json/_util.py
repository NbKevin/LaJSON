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

Helper utilities.
"""

__author__ = 'Nb'


class Stack:
    """
    Simulating a stack.
    """

    def __init__(self):
        """Create a stack."""
        self._stack = []

    def push(self, element):
        """Push an object."""
        self._stack.append(element)

    def pop(self):
        """Pop an object."""
        return self._stack.pop()

    def peek(self):
        """Peek an object."""
        return self._stack[-1]

    @property
    def is_empty(self):
        """Tell if there still element to be popped."""
        return len(self._stack) == 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self._stack.pop()
        except IndexError:
            raise StopIteration

    def reversed(self):
        # noinspection PyPep8Naming
        class _:
            """Reversed iterator of the stack."""

            def __init__(self, stack_: Stack):
                self.pos = -1
                self.stack = stack_._stack

            def __iter__(self):
                return self

            def __next__(self):
                self.pos += 1
                try:
                    return self.stack[self.pos]
                except IndexError:
                    raise StopIteration

        return _(self)


class JSONSyntaxError(SyntaxError):
    """JSON syntax error."""
    def __init__(self, char: str, line_no: int, char_no: int, message=None):
        self.msg = 'Error parsing *%s* at line %s, column %s: %s' % \
                   (char, line_no, char_no, message if message is not None else '')
        # On python 3.3 or higher, when __cause__ is set to
        # None, the context of exception would be suppressed
        # when being printed.
        # See PEP 0409 for more detail.
        self.__cause__ = None


class JSONNonStandardElementError(JSONSyntaxError):
    """JSON standard includes only a small range of data types.
    Elements beyond this range is not supported."""

    def __init__(self, char=None, line_no=None, char_no=None, message=None):
        if char is None and line_no is None and char_no is None:
            self.msg = message
        else:
            super(JSONNonStandardElementError, self).__init__(char, line_no, char_no, message)


# extended floating point numbers
try:
    PY_FLOAT_INF = float('inf')
    PY_FLOAT_NEG_INF = float('-inf')
    PY_FLOAT_NAN = float('NaN')
except ValueError:
    error = FloatingPointError('Cannot create IEEE standard floating point Inf and/or NaN on this platform\n'
                               'Hardware may not be compatible with this software.')
    error.__cause__ = None
    raise error
