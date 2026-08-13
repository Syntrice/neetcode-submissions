# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and not list2:
            return list1
        
        if list2 and not list1:
            return list2

        if list1 and list2:
            if list2.val < list1.val:
                list1, list2 = list2, list1
            
            solved = self.mergeTwoLists(list1.next, list2)

            list1.next = solved
            return list1

            


            

