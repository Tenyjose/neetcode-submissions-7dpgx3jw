# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        p1 = dummy
        p2 = head
        count = 0

        while p2!= None:
            p2 = p2.next
            count += 1

            if count > n:
                p1 = p1.next

        p1.next = p1.next.next
        return dummy.next