# Definition for a binary tree node.
import collections
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reversepostorder(self,node,level,ans):
        if node is None:
            return
        if len(ans)==level:
            ans.append(node.val)
        if node.right:
            self.reversepostorder(node.right,level+1,ans)
        if node.left:
            self.reversepostorder(node.left,level+1,ans)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # queue= deque()
        # result = []
        # queue.append(root)
        # while len(queue)!=0:
        #     level_size = len(queue)
        #     for i in range(level_size):
        #         node =queue.popleft()
        #         if i==level_size-1:
        #             result.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return result
        ans=[]
        self.reversepostorder(root,0,ans)
        return ans