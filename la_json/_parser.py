#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
The parser.
"""

__author__ = 'Nb'

from la_json._util import Stack, JSONSyntaxError
from la_json._elements import JSONObject, JSONArray, JSONKVPair, Undefined, JSONIdentifier


class States:
    """
    States of the parser.
    """
    ENTRANCE = -1

    OBJECT_INITIAL = 0
    OBJECT_EXPECT_KEY = 1
    OBJECT_KEY = 2
    OBJECT_EXPECT_COLON = 3
    OBJECT_EXPECT_VALUE = 4
    OBJECT_VALUE_STRING = 5
    OBJECT_VALUE_IDENTIFIER = 6
    OBJECT_EXIT = 7

    ARRAY_INITIAL = 8
    ARRAY_EXPECT_ITEM = 9
    ARRAY_STRING = 10
    ARRAY_IDENTIFIER = 11
    ARRAY_EXIT = 12


class Parser:
    """
    JSON parser.
    """

    element_set = (JSONObject, JSONArray)

    def __init__(self, io_object):
        """Initialise the parser from a readable I/O object."""
        self._source = io_object
        self.__pos = -1
        self.__line_no = 1
        self.__char_no = 0

    def get_char(self, move_cursor=False):
        """Get next char from source string."""
        if move_cursor:
            self.__pos += 1
            self.__char_no += 1
        try:
            char = self._source[self.__pos]
            if move_cursor:
                if char in '\r\n':
                    self.__line_no += 1
                    self.__char_no = 0
            return char
        except IndexError:
            raise JSONSyntaxError('', self.__line_no, self.__char_no,
                                  'No root element found before the end of the file')

    def parse(self):
        """Parse the source JSON string."""
        # state
        _STATE = States.ENTRANCE

        # char pool
        char_pool = []

        # stacks
        container_stack = Stack()
        content_stack = Stack()

        # whether to ignore space
        _IGNORE_SPACE = True

        # whether to move cursor
        _MOVE_CURSOR = True

        # the core state machine
        while True:

            # get next char and set default _MOVE_CURSOR
            char = self.get_char(_MOVE_CURSOR)
            _MOVE_CURSOR = True

            # skip space and new line separator if _IGNORE_SPACE is True
            if (char.isspace() or char in '\r\n') and _IGNORE_SPACE:
                continue

            # ENTRANCE turns either to OBJECT_INITIAL or ARRAY_INITIAL
            # depending on which char it finds, { or [.
            if _STATE == States.ENTRANCE:
                if char == '{':
                    _STATE = States.OBJECT_INITIAL
                    _MOVE_CURSOR = False
                elif char == '[':
                    _STATE = States.ARRAY_INITIAL
                    _MOVE_CURSOR = False
                else:
                    raise JSONSyntaxError(char, self.__line_no, self.__char_no,
                                          'Root element can either be an object or an array')

            # OBJECT_INITIAL creates a JSONObject, pushes it to
            # the container stack and set its content stack as
            # the current one. Then it turns to OBJECT_EXPECT_KEY.
            elif _STATE == States.OBJECT_INITIAL:
                new_object = JSONObject()
                container_stack.push(new_object)
                content_stack = new_object.content_stack
                _STATE = States.OBJECT_EXPECT_KEY

            # OBJECT_EXPECT_KEY expects a " as the beginning of a key
            # and turns to OBJECT_KEY if it finds one. Specially,
            # if a } is found, it turns to OBJECT_EXIT without
            # moving the cursor directly.
            # _IGNORE_SPACE is set to False if a " is found.
            elif _STATE == States.OBJECT_EXPECT_KEY:
                if char == '"':
                    _STATE = States.OBJECT_KEY
                    _IGNORE_SPACE = False
                elif char == '}':
                    _STATE = States.OBJECT_EXIT
                    _MOVE_CURSOR = False
                else:
                    raise JSONSyntaxError(char, self.__line_no, self.__char_no,
                                          'Object key must be a string')

            # OBJECT_KEY expects a string to be the key.
            # All char will be put into the char pool
            # and when " is found, the string is created.
            # Then it creates a JSONKVPair and set the string
            # as its key, push the K-V pair to content stack
            # and turn to OBJECT_COLON.
            # _IGNORE_SPACE is set to True thus.
            elif _STATE == States.OBJECT_KEY:
                if char != '"':
                    char_pool.append(char)
                else:
                    kv_pair = JSONKVPair()
                    kv_pair.key = ''.join(char_pool)
                    content_stack.push(kv_pair)
                    char_pool = []
                    _STATE = States.OBJECT_EXPECT_COLON
                    _IGNORE_SPACE = True

            # OBJECT_EXPECT_COLON expects a : between a key and
            # its value and turns to OBJECT_VALUE if found.
            elif _STATE == States.OBJECT_EXPECT_COLON:
                if char == ':':
                    _STATE = States.OBJECT_EXPECT_VALUE
                else:
                    raise JSONSyntaxError(char, self.__line_no, self.__char_no,
                                          'Object key must be followed with a colon')

            # OBJECT_EXPECT_VALUE expects a string, an object, an
            # array or an identifier and turns to OBJECT_VALUE_STRING,
            # OBJECT_INITIAL, ARRAY_INITIAL or OBJECT_VALUE_IDENTIFIER
            # correspondingly.
            # _IGNORE_SPACE is set to False if a string is found.
            elif _STATE == States.OBJECT_EXPECT_VALUE:
                if char == '{':
                    _STATE = States.OBJECT_INITIAL
                    _MOVE_CURSOR = False
                elif char == '[':
                    _STATE = States.ARRAY_INITIAL
                    _MOVE_CURSOR = False
                elif char == '"':
                    _STATE = States.OBJECT_VALUE_STRING
                    _IGNORE_SPACE = False
                else:
                    _STATE = States.OBJECT_VALUE_IDENTIFIER
                    _MOVE_CURSOR = False

            # OBJECT_VALUE_STRING expects a string to be the value of
            # last K-V pair. When found is set the string to be the value
            # and turns to OBJECT_EXIT.
            # _IGNORE_SPACE is set to True afterwards.
            elif _STATE == States.OBJECT_VALUE_STRING:
                if char == '"':
                    content_stack.peek().value = ''.join(char_pool)
                    char_pool = []
                    _STATE = States.OBJECT_EXIT
                    _IGNORE_SPACE = True
                else:
                    char_pool.append(char)

            # OBJECT_VALUE_IDENTIFIER expects an identifier or a number.
            # If found then it push that identifier or number to the
            # content stack. Then it turns to OBJECT_EXIT without moving
            # the cursor.
            elif _STATE == States.OBJECT_VALUE_IDENTIFIER:
                if char not in ',}':
                    char_pool.append(char)
                else:
                    raw_identifier_string = ''.join(char_pool)
                    char_pool = []
                    if raw_identifier_string not in JSONIdentifier.SET:
                        try:
                            number = int(raw_identifier_string)
                        except ValueError:
                            try:
                                number = float(raw_identifier_string)
                            except ValueError:
                                raise JSONSyntaxError(char, self.__line_no, self.__char_no,
                                                      'Unknown identifier *%s*' % raw_identifier_string)
                        content_stack.peek().value = number
                    else:
                        content_stack.peek().value = JSONIdentifier.TO_PYTHON_DICT[raw_identifier_string]
                    _STATE = States.OBJECT_EXIT
                    _MOVE_CURSOR = False

            # OBJECT_EXIT expects either a , as the splitter or the
            # end of the object. If a , is found, it turns to OBJECT_KEY.
            # If a } is found, it first pops all content from the
            # content stack and assigns them to the current object.
            # Then it checks if there is any other container in the
            # container stack. If not, it returns the current object
            # as the root element. Otherwise, it assigns the current
            # object to the last container in the container stack
            # and set the content stack of that container to be the
            # current one.
            # If that last container in the container stack is an
            # array, then it simply appends the object. Otherwise it
            # sets the object as the key of the last K-V pair in the
            # content stack of that container.
            elif _STATE == States.OBJECT_EXIT:
                if char == ',':
                    _STATE = States.OBJECT_EXPECT_KEY
                elif char == '}':
                    object_ = container_stack.pop()
                    object_.kv_pairs.extend(content_stack)
                    if not container_stack.is_empty:
                        last_container_in_stack = container_stack.peek()
                        content_stack = last_container_in_stack.content_stack
                        if isinstance(last_container_in_stack, JSONObject):
                            if content_stack.peek().value is Undefined:
                                content_stack.peek().value = object_
                            else:
                                raise JSONSyntaxError(char, self.__line_no, self.__char_no,
                                                      'KVPair has already got a value')
                        elif isinstance(last_container_in_stack, JSONArray):
                            content_stack.push(object_)
                            _STATE = States.ARRAY_EXIT
                        else:
                            raise JSONSyntaxError(char, self.__line_no, self.__char_no,
                                                  'Unknown container type in the stack *%s*' % last_container_in_stack)
                    else:
                        return object_
                else:
                    raise JSONSyntaxError(char, self.__line_no, self.__char_no,
                                          'Invalid end character for object')

            # ARRAY_INITIAL creates an JSONArray, pushes it to the
            # container stack and set its content stack as the current
            # one. Then it turns to ARRAY_ITEM.
            elif _STATE == States.ARRAY_INITIAL:
                new_array = JSONArray()
                container_stack.push(new_array)
                content_stack = new_array.content_stack
                _STATE = States.ARRAY_EXPECT_ITEM

            # ARRAY_EXPECT_ITEM expects a string, an object, an array or
            # an identifier and turns to ARRAY_STRING, OBJECT_INITIAL,
            # ARRAY_INITIAL oor ARRAY_IDENTIFIER correspondingly. If a [
            # is found, it turns to ARRAY_EXIT directly.
            elif _STATE == States.ARRAY_EXPECT_ITEM:
                if char == '"':
                    _STATE = States.ARRAY_STRING
                    _IGNORE_SPACE = False
                elif char == '{':
                    _STATE = States.OBJECT_INITIAL
                    _MOVE_CURSOR = False
                elif char == '[':
                    _STATE = States.ARRAY_INITIAL
                    _MOVE_CURSOR = False
                elif char == ']':
                    _STATE = States.ARRAY_EXIT
                    _MOVE_CURSOR = False
                else:
                    _STATE = States.ARRAY_IDENTIFIER
                    _MOVE_CURSOR = False

            # ARRAY_STRING expects a string. All char will be stored
            # in the char pool and when a " is found, the string is
            # created and pushed to content stack. Then it turns to
            # ARRAY_EXIT.
            elif _STATE == States.ARRAY_STRING:
                if char == '"':
                    string = ''.join(char_pool)
                    content_stack.push(string)
                    char_pool = []
                    _STATE = States.ARRAY_EXIT
                    _IGNORE_SPACE = True
                else:
                    char_pool.append(char)

            # ARRAY_IDENTIFIER expects an identifier or a number.
            # If found then it push that identifier or number to
            # the content stack. Then it turns to ARRAY_EXIT without
            # moving the cursor.
            elif _STATE == States.ARRAY_IDENTIFIER:
                if char not in ',]':
                    char_pool.append(char)
                else:
                    raw_identifier_string = ''.join(char_pool)
                    char_pool = []
                    if raw_identifier_string not in JSONIdentifier.SET:
                        try:
                            number = int(raw_identifier_string)
                        except ValueError:
                            try:
                                number = float(raw_identifier_string)
                            except ValueError:
                                raise JSONSyntaxError(char, self.__line_no, self.__char_no,
                                                      'Unknown identifier *%s*' % raw_identifier_string)
                        content_stack.push(number)
                    else:
                        content_stack.push(JSONIdentifier.TO_PYTHON_DICT[raw_identifier_string])
                    _STATE = States.ARRAY_EXIT
                    _MOVE_CURSOR = False

            # ARRAY_EXIT expects either a , or a ]. The former one
            # results in turning to ARRAY_ITEM. The latter one, as
            # very similar to OBJECT_EXIT, first assign all content
            # in the content stack to current container. Then it checks
            # whether there is still containers in the container stack.
            # If so, it assigns current container to the last containers
            # in the stack as its content and set the content stack of
            # that container as the current one. Otherwise it just
            # return the current array as the root element.
            # If the last container in the stack is an object, the
            # current array will be assigned to the value of the last
            # K-V pair in the content stack of the container. If it is
            # an array, then the current array will just be simply pushed
            # to the content stack of the container.
            elif _STATE == States.ARRAY_EXIT:
                if char == ',':
                    _STATE = States.ARRAY_EXPECT_ITEM
                elif char == ']':
                    array_ = container_stack.pop()
                    array_.array.extend(content_stack.reversed())
                    if not container_stack.is_empty:
                        last_container_in_stack = container_stack.peek()
                        content_stack = last_container_in_stack.content_stack
                        if isinstance(last_container_in_stack, JSONObject):
                            if content_stack.peek().value is Undefined:
                                content_stack.peek().value = array_
                                _STATE = States.OBJECT_EXIT
                            else:
                                raise JSONSyntaxError(char, self.__line_no, self.__char_no,
                                                      'KVPair has already got a value')
                        elif isinstance(last_container_in_stack, JSONArray):
                            content_stack.push(array_)
                        else:
                            raise JSONSyntaxError(char, self.__line_no, self.__char_no,
                                                  'Unknown container type in the stack *%s*' % last_container_in_stack)
                    else:
                        return array_
                else:
                    raise JSONSyntaxError(char, self.__line_no, self.__char_no,
                                          'Invalid end character for object')
            else:
                raise JSONSyntaxError(char, self.__line_no, self.__char_no,
                                      'Unknown state *%s*' % _STATE)
