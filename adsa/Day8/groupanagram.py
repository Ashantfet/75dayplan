from collections import defaultdict
import ast

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        anagram_map = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            anagram_map[key].append(word)
        return list(anagram_map.values())

strs = ast.literal_eval(input())
sol = Solution()
result = sol.groupAnagrams(strs)
for group in result:
    print(group)
