# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         #fast,slow pointers to find out the middle point of the list
#         slow,fast = head,head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
        
#         second = slow.next
#         slow.next = None

#         #reverse second half
#         prev = None
#         while second:
#             nxt = second.next
#             second.next = prev
#             prev = second
#             second = nxt
        
#         first = head
#         second = prev

#         #merge broooo
#         while second:
#             tmp1 = first.next
#             tmp2 = second.next
#             first.next = second
#             second.next = tmp1
#             first = tmp1
#             second = tmp2
        
#         |A|->|B|->|C|->|D|->|E|->|F|->|G|

#         #mergeeee


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        prev = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        
        second = prev
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2