from sys import *
from collections import *
from math import *

# Binary Tree node structure
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Helper function to get inorder traversal
def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)

# Helper function to get preorder traversal
def preorder(node, result):
    if node is None:
        return
    result.append(node.data)
    preorder(node.left, result)
    preorder(node.right, result)

# Helper function to get postorder traversal
def postorder(node, result):
    if node is None:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.data)

# Main function
def getTreeTraversal(root):
    in_order = []
    pre_order = []
    post_order = []

    inorder(root, in_order)
    preorder(root, pre_order)
    postorder(root, post_order)

    return [in_order, pre_order, post_order]