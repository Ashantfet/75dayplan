from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        n= len(adj)
        ans =[]
        queue = deque()
        visited =[0]*n
        queue.append(0)
        visited[0]=1
        while len(queue)!=0:
            e=queue.popleft()
            ans.append(e)
            for node in adj[e]:
                if visited[node]==0:
                    queue.append(node)
                    visited[node]=1
                    
        return ans
adjacency_list = [[1, 2], [0, 3], [0], [1]]
sol = Solution()
print(sol.bfs(adjacency_list))  # Output: [0, 1, 2, 3]