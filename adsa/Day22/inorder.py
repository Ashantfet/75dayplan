# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result =[]
        if root ==None:
            return []

        result+= self.inorderTraversal(root.left)
        result+= [root.val]
        result+= self.inorderTraversal(root.right)
        return result