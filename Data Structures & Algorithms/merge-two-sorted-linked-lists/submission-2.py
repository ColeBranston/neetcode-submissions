# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ref = ListNode()
        myRef = ref
        while list1 and list2:
            if list1.val < list2.val:
                ref.next = list1
                list1 = list1.next
            else:
                ref.next = list2
                list2 = list2.next

            ref = ref.next

        ref.next = list1 or list2

        return myRef.next