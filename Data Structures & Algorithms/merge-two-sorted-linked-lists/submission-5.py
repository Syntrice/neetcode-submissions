# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Base cases
        if not list1:
            return list2
        if not list2:
            return list1

        # Keep the smallest node to the left
        if list2.val < list1.val:
            list1, list2 = list2, list1
            
        # Everything to the right of the left solve recursively
        next = self.mergeTwoLists(list1.next, list2)

        # Fix references
        list1.next = next
        return list1

            


            

