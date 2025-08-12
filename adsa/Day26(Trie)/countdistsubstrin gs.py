class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_suffix(self, suffix):
        node = self.root
        new_nodes = 0
        for ch in suffix:
            if ch not in node.children:
                node.children[ch] = TrieNode()
                new_nodes += 1
            node = node.children[ch]
        return new_nodes

def countDistinctSubstrings(s):
    trie = Trie()
    count = 0
    for i in range(len(s)):
        count += trie.insert_suffix(s[i:])
    return count + 1  # +1 for the empty substring
for _ in range(int(input().strip())):
    s= input().strip()
    result = countDistinctSubstrings(s)
    print(result)  # Output: Number of distinct substrings including the empty substring