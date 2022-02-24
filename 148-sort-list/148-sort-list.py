# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        nums.sort()
        head = prev = curr = None
        
        for i in nums:
            curr = ListNode(val=i)
            if not head:
                head = curr
            if prev:
                prev.next = curr
            prev = curr
        return head