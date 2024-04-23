# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Initialize dummy nodes for the heads of the two lists
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        # Initialize pointers for the two lists
        less_ptr = less_head
        greater_ptr = greater_head
        
        # Traverse the original linked list
        while head:
            # If the current node's value is less than x, append it to the less list
            if head.val < x:
                less_ptr.next = head
                less_ptr = less_ptr.next
            # Otherwise, append it to the greater list
            else:
                greater_ptr.next = head
                greater_ptr = greater_ptr.next
            
            # Move to the next node in the original list
            head = head.next
        
        # Connect the end of the less list to the head of the greater list
        less_ptr.next = greater_head.next
        # Set the end of the greater list to None to terminate the combined list
        greater_ptr.next = None
        
        # Return the head of the combined list
        return less_head.next

# Helper function to convert a list to a linked list
def list_to_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst