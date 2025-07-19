class Solution:
    def delete_node(self, head, x):
        if x == 1:
            if head.next:
                head = head.next
                head.prev = None
            else:
                head = None  
            return head

        temp = head
        count = 1

        while temp is not None and count < x:
            temp = temp.next
            count += 1

        if temp is None:
            return head

        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

        return head
