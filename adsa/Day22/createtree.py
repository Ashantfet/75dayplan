

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def createTree(self, root, l):
        # l[0] is already root.val
        root.left = Node(l[1])
        root.right = Node(l[2])

        root.left.left = Node(l[3])
        root.left.right = Node(l[4])

        root.right.left = Node(l[5])
        root.right.right = Node(l[6])

