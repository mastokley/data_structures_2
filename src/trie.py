# _*_ Coding: Utf-8 _*_

import re


class Trie(object):

    def __init__(self):
        self._container = {}

    def insert(self, token):
        bad_chars = r"[^a-zA-Z']"
        if not isinstance(token, str) or re.findall(bad_chars, token):
            raise TypeError("strings plz, a-z and ' only")
        token = "".join([token, '$'])
        node = self._container
        for char in token:
            if char not in node:
                node[char] = "" if char == '$' else {}
            node = node[char]

    def contains(self, token):
        bad_chars = r"[^a-zA-Z']"
        if not isinstance(token, str) or re.findall(bad_chars, token):
            raise TypeError("strings plz, a-z and ' only")
        token = "".join([token, '$'])
        node = self._container
        for char in token:
            try:
                node = node[char]
            except KeyError:
                return False
        return True

    def traversal(self, node=None):
        if node is None:
            node = self._container
        for edge in node:
            if edge == '$':
                yield ''
            else:
                for yielded in self.traversal(node=node[edge]):
                    yield edge + yielded
