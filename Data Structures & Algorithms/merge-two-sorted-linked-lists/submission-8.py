# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ref1, ref2 = list1,list2

        dummyRef = dummy = ListNode()

        while ref1 and ref2:
            if ref1.val <= ref2.val:
                dummy.next = ref1
                ref1 = ref1.next
            else:
                dummy.next = ref2
                ref2 = ref2.next

            dummy = dummy.next

        dummy.next = ref1 if ref1 else ref2

        return dummyRef.next