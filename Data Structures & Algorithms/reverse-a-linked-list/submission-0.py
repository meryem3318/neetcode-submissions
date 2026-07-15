class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle the edge case of an empty list
        if not head:
            return None
        
        prev = None
        curr = head
        
        while curr:
            # 1. Save the future: keep track of the rest of the list
            temp = curr.next
            
            # 2. Reverse the link: point the current node backward
            curr.next = prev
            
            # 3. Step forward: move 'prev' up to the current node
            prev = curr
            
            # 4. Step forward: move 'curr' to the next node we saved in temp
            curr = temp
            
        # By the end of the loop, 'prev' will be pointing to the new head of the list
        return prev