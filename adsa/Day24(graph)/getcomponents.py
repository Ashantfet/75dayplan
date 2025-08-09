class Solution:
    # Function to return connected components of the graph
    def getComponents(self, V, edges):
        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * V
        result = []

        def dfs(node, comp):
            visited[node] = True
            comp.append(node)
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, comp)

        for i in range(V):
            if not visited[i]:
                comp = []
                dfs(i, comp)
                result.append(comp)

        return result
v = int(input())
edges = []
for _ in range(int(input())):
    edges.append(list(map(int, input().split())))
sol = Solution()
print(sol.getComponents(v, edges))  # Output: list of connected components in the graph
# Example: For v=5 and edges=[[0, 1], [1, 2], [3, 4]], the output should be [[0, 1, 2], [3, 4]]