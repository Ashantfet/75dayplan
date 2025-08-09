
from typing import List


class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        # code here
        lst = [[] for _ in range(V)]
        for u,v in edges:
            lst[u].append(v)
            lst[v].append(u)
        return lst
v=int(input())
edges = []
for _ in range(v):
    edges.append(list(map(int, input().split())))
sol = Solution()
print(sol.printGraph(v, edges))  # Output: adjacency list representation of the graph