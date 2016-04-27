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

    
                
            


