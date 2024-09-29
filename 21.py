# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = result = None 
        if (list1 and list2 and list1.val < list2.val) or (list1 and not list2):
            start = list1
            result = list1
            list1 = list1.next
        elif list1 and list2 and list2.val <= list1.val or (list2 and not list1):
            start = list2
            result = list2
            list2 = list2.next

        while list1 or list2:
            if (list1 and list2 and list1.val <= list2.val) or (list1 and not list2):
                result.next = list1
                list1 = list1.next
            elif list1 and list2 and list2.val < list1.val or (list2 and not list1):
                result.next = list2
                list2 = list2.next
            result = result.next
        if result:
            result.next = None
        return start
