# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []

        for ll in lists:
            ref = ll
            while ref:
                res.append(ref.val)
                ref = ref.next

        res.sort()
        dummyNode = dummy = ListNode()

        for num in res:
            dummy.next = ListNode(num)
            dummy = dummy.next

        return dummyNode.next