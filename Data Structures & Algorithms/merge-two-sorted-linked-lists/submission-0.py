
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        head = merged
        while True:
            if not list1 and not list2:
                return head.next
            
            if not list1:
                merged.next = list2
                return head.next
            elif not list2:
                merged.next = list1
                return head.next
            
            if list1.val < list2.val:
                node = ListNode(list1.val)
                merged.next = node
                merged = node
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                merged.next = node
                merged = node
                list2 = list2.next

            
            
        