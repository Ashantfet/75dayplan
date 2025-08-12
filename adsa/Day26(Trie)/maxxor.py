class TrieNode:
    __slots__ = ['children']  # avoid per-object dict
    def __init__(self):
        self.children = [None, None]  # bit 0, bit 1

class Solution:
    def findMaximumXOR(self, nums):
        root = TrieNode()
        L = max(nums).bit_length()

        # Build trie
        for num in nums:
            node = root
            for i in range(L - 1, -1, -1):
                bit = (num >> i) & 1
                if not node.children[bit]:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        # Find max XOR
        max_xor = 0
        for num in nums:
            node = root
            xor_num = 0
            for i in range(L - 1, -1, -1):
                bit = (num >> i) & 1
                opp = 1 - bit
                if node.children[opp]:
                    xor_num = (xor_num << 1) | 1
                    node = node.children[opp]
                else:
                    xor_num = (xor_num << 1) | 0
                    node = node.children[bit]
            max_xor = max(max_xor, xor_num)

        return max_xor
    
nums = list(map(int, input().strip().split()))
sol = Solution()
result = sol.findMaximumXOR(nums)
print(result)  # Output: Maximum XOR of two numbers in the array