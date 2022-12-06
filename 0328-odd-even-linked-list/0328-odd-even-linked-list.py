# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd_head = None
        even_head = None
        odd_st_head = even_st_head = None
        curr = 1
        while head:
            last = None
            if curr%2:
                if not odd_head:
                    odd_head = head
                    st_head = odd_head
                else:
                    odd_head.next = head
                    odd_head = odd_head.next
            else:
                if not even_head:
                    even_head = head
                    even_st_head = even_head
                else:
                    even_head.next = head
                    even_head = even_head.next
            curr += 1
            head = head.next

        odd_head.next = even_st_head
        if even_head:
            even_head.next = None
        # print(st_head)
        return st_head