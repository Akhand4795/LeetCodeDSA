# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            while stack and head.val > stack[-1]:
                stack.pop()
            stack.append(head.val)
            head = head.next
        result = ListNode(0)
        temp = result
        for i in stack:
            temp.next = ListNode(i)
            temp = temp.next
        return result.next
    

        
        