# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        

        second = slow.next
        slow.next = None

        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        head2 = prev

        while head and head2:
            temp1 = head.next
            head.next = head2
            head = temp1

            temp2 = head2.next
            head2.next = head
            head2 = temp2

        return

