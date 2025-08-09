class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def solve(self,node,vis,result,adj):
        vis[node]=1
        result.append(node)
        for n in adj[node]:
            if vis[n]==0:
                self.solve(n,vis,result,adj)
    def dfs(self, adj):
        # code here
        node =0
        vis=[0]*len(adj)
        result=[]
        self.solve(node,vis,result,adj)
        return result

adjacency_list = [[1, 2], [0, 3], [0], [1]]
sol = Solution()
print(sol.dfs(adjacency_list))  # Output: [0, 1, 3, 2]