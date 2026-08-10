
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # List is already reversed if a) empty or b) only one item
        if not head or not head.next:
            # We either return head, or None if the list is empty (no nodes so no head)
            return head 

        # Process the next item BEFORE any changes so that the deepest is processed first
        new_head = self.reverseList(head.next)

        # Swap the pointers of head and the next node
        head.next.next = head
        head.next = None
        return new_head