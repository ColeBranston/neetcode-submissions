# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            take each linked list and reverse and traverse to get real number for both, then add those two
            numbers and build and reverse that linked list as well
        '''

        ref1 = l1
        prev = None
        while ref1:
            temp = ref1.next
            ref1.next = prev
            prev = ref1
            ref1 = temp
        l1 = prev

        ref2 = l2
        prev = None
        while ref2:
            temp = ref2.next
            ref2.next = prev
            prev = ref2
            ref2 = temp
        l2 = prev

        number1, number2 = '', ''
        ref1 = l1
        while ref1:
            number1 += str(ref1.val)
            ref1 = ref1.next

        ref2 = l2
        while ref2:
            number2 += str(ref2.val)
            ref2 = ref2.next

        finalNumber = int(number1) + int(number2)
        finalNumber = str(finalNumber)[::-1]

        dummy = dummy1 = ListNode(0)
        for char_num in finalNumber:
            dummy1.next = ListNode(int(char_num))
            dummy1 = dummy1.next

        return dummy.next
