from sys import *
from collections import *
from math import *

from typing import *

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def check_all_prefixes(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
            if not node.is_end:
                return False
        return True

def completeString(n: int, a: List[str]) -> str:
    trie = Trie()
    for word in a:
        trie.insert(word)

    best = ""
    for word in a:
        if trie.check_all_prefixes(word):
            if len(word) > len(best) or (len(word) == len(best) and word < best):
                best = word

    return best if best != "" else "None"

# Example usage:
n = int(input().strip())
a = input().strip().split()
result = completeString(n, a)
print(result)  # Output: Longest word with all prefixes present or "None"