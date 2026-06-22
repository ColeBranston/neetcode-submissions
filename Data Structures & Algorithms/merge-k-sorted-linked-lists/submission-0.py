# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        array = []

        if not lists or not lists[0]:
            return None

        for nodes in lists:
            node = nodes
            while node:
                array.append(node)
                node = node.next

        array.sort(key=lambda x: x.val)

        ref = dummy = ListNode(0,0)
        for node in array:
            dummy.next = node
            dummy = dummy.next

        return ref.next