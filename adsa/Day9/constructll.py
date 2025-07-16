class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
class Solution:
    def __init__(self):
        self.head = None

    def constructLL(self, arr):
        if not arr:
            return None

        self.head = Node(arr[0])
        current = self.head

        for value in arr[1:]:
            current.next = Node(value)
            current = current.next

        return self.head
arr = list(map(int, input().split()))
sol = Solution()
head = sol.constructLL(arr)
current = head
while current:
    print(current.data, end=" ")
    current = current.next
print()  