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
                for yield_ in self.traversal(node=node[edge]):
                    yield ''.join([edge + yield_])

    def autocomplete(self, token=''):
        """Return a list of potential completions for given token."""
        node = self._container
        for char in token:
            try:
                node = node[char]
            except KeyError:
                return []
        return [''.join([token, w]) for w in self.traversal(node)]

    def autocomplete_multilist(self, token=''):
        """Return dictionary for possible results for each keystroke in token."""
        token_list = []
        for i in range(1, len(token) + 1):
            token_list.append(token[:i])
        out = {}
        for token in token_list:
            out[token] = sorted([w for w in self.autocomplete(token)][:4])
        return out

