# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1, sum2 = 0, 0
        weight = 1
        pointer = l1
        while pointer is not None:
            sum1 = sum1 + (weight * pointer.val)
            weight *= 10
            pointer = pointer.next

        pointer = l2
        weight = 1
        while pointer is not None:
            sum2 = sum2 + (weight * pointer.val)
            weight *= 10
            pointer = pointer.next

        sum = sum1 + sum2
        res = [int(x) for x in reversed(str(sum))]
        node = ListNode()
        result = self.create_node(node, 0, res)
        return result
        
    
    def create_node(self, node: ListNode, index: int, array: list):
        if len(array) > index:
            node.val = array[index]
            node.next = self.create_node(ListNode(), index + 1, array)
            return node
