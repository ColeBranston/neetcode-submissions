# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyRef = dummy = ListNode()
        ref1,ref2 = list1,list2
        while ref1 and ref2:
            print(dummyRef.val)
            if ref1.val <= ref2.val:
                dummyRef.next = ref1
                ref1 = ref1.next
            else:
                dummyRef.next = ref2
                ref2 = ref2.next

            dummyRef = dummyRef.next

        dummyRef.next = ref1 if ref1 else ref2

        return dummy.next