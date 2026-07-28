# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        n = 0
        if not head:
            return False
        hashtable = {}
        while head.next:
            if head.next.val in hashtable:
                return True
            hashtable[n] = head.val
            head = head.next
            n += 1
        return False


        