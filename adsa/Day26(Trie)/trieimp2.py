from os import *
from sys import *
from collections import *
from math import *
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count_end = 0      # how many words end here
        self.count_prefix = 0   # how many words have this prefix

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count_prefix += 1
        node.count_end += 1

    def countWordsEqualTo(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.count_end

    def countWordsStartingWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.count_prefix

    def erase(self, word):
        # Only erase if it exists
        if self.countWordsEqualTo(word) == 0:
            return
        node = self.root
        for ch in word:
            node = node.children[ch]
            node.count_prefix -= 1
        node.count_end -= 1

# Example usage:
trie = Trie()
trie.insert("hello")
trie.insert("hell")
trie.insert("heaven")
trie.insert("heavy")

print(trie.countWordsEqualTo("hello"))  # Output: 1
print(trie.countWordsStartingWith("he"))  # Output: 4
print(trie.countWordsStartingWith("hell")) # Output: 2

trie.erase("hello")
print(trie.countWordsEqualTo("hello"))  # Output: 0
print(trie.countWordsStartingWith("he"))  # Output: 3
print(trie.countWordsStartingWith("hell")) # Output: 1
trie.erase("heaven")
print(trie.countWordsStartingWith("he"))  # Output: 2
trie.erase("hell")
print(trie.countWordsStartingWith("he"))  # Output: 1
trie.erase("heavy")
print(trie.countWordsStartingWith("he"))  # Output: 0   