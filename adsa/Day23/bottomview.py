
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
from collections import deque
class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return None
        ans =[]
        queue = deque()
        result ={}
        queue.append((root,0))
        while queue:
            e,line = queue.popleft()
            result[line] =e.data
            if e.left:
                queue.append((e.left,line-1))
            if e.right:
                queue.append((e.right,line+1))
        for key in sorted(result):
            ans.append(result[key])
        return ans