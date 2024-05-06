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
        print(stack)
        result = ListNode(0)
        temp = result
        i = 0
        while i < len(stack):
            temp.next = ListNode(stack[i])
            i += 1
            temp = temp.next
        return result.next
    

        
        