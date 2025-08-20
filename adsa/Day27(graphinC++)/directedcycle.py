class Solution:
    def dfs(self, node, visited, pathVisited, adj_list):
        visited[node] = True
        pathVisited[node] = True

        for adjNode in adj_list[node]:
            if not visited[adjNode]:
                if self.dfs(adjNode, visited, pathVisited, adj_list):
                    return True
            elif pathVisited[adjNode]:  # Found a back edge
                return True

        pathVisited[node] = False  # Backtrack
        return False

    def isCycle(self, V, edges):
        adj_list = [[] for _ in range(V)]
        for u, v in edges:
            adj_list[u].append(v)  # directed edge

        visited = [False] * V
        pathVisited = [False] * V

        for i in range(V):
            if not visited[i]:
                if self.dfs(i, visited, pathVisited, adj_list):
                    return True
        return False
# Example usage:
edges = [(0, 1), (1, 2), (2, 0)]  # Example directed graph with a cycle
solution = Solution()
print(solution.isCycle(3, edges))  # Output: True