class TrieNode:
    def __init__(self):
        self.children = {}  # 0 -> TrieNode, 1 -> TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
    def getMaxXor(self, num):
        node = self.root
        if not node.children:  # Trie empty
            return -1
        xor_num = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            opp = 1 - bit
            if opp in node.children:
                xor_num = (xor_num << 1) | 1
                node = node.children[opp]
            else:
                xor_num = (xor_num << 1) | 0
                node = node.children.get(bit, node)
        return xor_num

class Solution:
    def maximizeXor(self, nums, queries):
        nums.sort()
        queries = sorted([(m, x, idx) for idx, (x, m) in enumerate(queries)])
        
        t = Trie()
        res = [-1] * len(queries)
        i = 0
        n = len(nums)
        
        for m, x, idx in queries:
            # Insert all nums ≤ m
            while i < n and nums[i] <= m:
                t.insert(nums[i])
                i += 1
            res[idx] = t.getMaxXor(x)
        
        return res
nums = input().strip().split()
queries = []
q = int(input().strip())
for _ in range(q):
    x, m = map(int, input().strip().split())
    queries.append((x, m))

sol = Solution()
result = sol.maximizeXor(list(map(int, nums)), queries)
print(" ".join(map(str, result)))  # Output: Results for each query