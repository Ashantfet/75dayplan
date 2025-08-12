class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            # Reached end of search word
            if index == len(word):
                return node.is_end

            ch = word[index]

            # Wildcard '.' → try all children
            if ch == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(index + 1, node.children[ch])

        return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# Example usage:
word_dict = WordDictionary()
word_dict.addWord("bad")
word_dict.addWord("dad")
word_dict.addWord("mad")

print(word_dict.search("pad"))  # Output: False
print(word_dict.search("bad"))  # Output: True
print(word_dict.search(".ad"))  # Output: True
print(word_dict.search("b.."))  # Output: True
print(word_dict.search("b.d"))  # Output: False
print(word_dict.search("..d"))  # Output: True
print(word_dict.search("..."))  # Output: False
print(word_dict.search("b..d"))  # Output: False
print(word_dict.search("b..a"))  # Output: False
print(word_dict.search("b..d."))  # Output: False
print(word_dict.search("b..."))  # Output: False    