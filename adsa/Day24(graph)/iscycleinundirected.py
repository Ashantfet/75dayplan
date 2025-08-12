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
V = int(input())
edges = []
for _ in range(int(input())):
    u, v = map(int, input().split())
    edges.append((u, v))
sol = Solution()
print(sol.isCycle(V, edges))  # Output: True or False based on the cycle detection