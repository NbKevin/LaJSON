#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
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
    def __init__(self, char: str, line_no: int, char_no: int, message=None):
        self.msg = 'Error parsing *%s* at line %s, column %s: %s' % \
                   (char, line_no, char_no, message if message is not None else '')
