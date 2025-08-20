class Solution:
    def dfs(self,node,parent,visited,adj_list):
        visited[node]=1
        for adjNode in adj_list[node]:
            if visited[adjNode]==0:
                ans=self.dfs(adjNode,node,visited,adj_list)
                if ans==True:
                    return True
            elif  visited[adjNode] ==1 and adjNode!=parent:
                return True
        return False
    def isCycle(self, V, edges):
        # code here
        adj_list =[[] for _ in range(V)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited =[0]*V
        for i in range(0,V):
            if visited[i]==1:
                continue
            if self.dfs(i,-1,visited,adj_list):
                return True
        return False
# Example usage:
edges = [(0, 1), (1, 2), (2, 0)]  # Example undirected graph with a cycle
solution = Solution()
print(solution.isCycle(3, edges))  # Output: True
edges = [(0, 1), (1, 2), (2, 3)]  # Example undirected graph without a cycle
print(solution.isCycle(4, edges))  # Output: False  