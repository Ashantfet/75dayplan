# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def solve(self,root:Optional[TreeNode]) -> int:
        if root ==None:
            return 0
        lh = self.solve(root.left)
        rh= self.solve(root.right)
        self.ans = max(self.ans,lh+rh)
        return 1+max(lh,rh)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.solve(root)
        return self.ans