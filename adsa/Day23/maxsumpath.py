# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = float('-inf')
    def solve(self,root: Optional[TreeNode]) -> int:
        if root ==None:
            return 0
        ls = self.solve(root.left)
        if ls<0:
            ls=0
        rs = self.solve(root.right)
        if rs<0:
            rs=0
        self.ans = max(self.ans,ls+root.val+rs)
        return root.val+max(ls,rs)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.solve(root)
        return self.ans