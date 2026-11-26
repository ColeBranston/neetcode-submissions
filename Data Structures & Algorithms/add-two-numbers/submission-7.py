# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNum(LL):
            ref = LL
            res = ""

            while ref:
                res += str(ref.val)
                ref = ref.next

            return res

        l1 = int(getNum(l1)[::-1])
        l2 = int(getNum(l2)[::-1])

        combined = str(l1 + l2)
        print(combined)
        combined = [int(char) for char in combined[::-1]]

        print(combined)

        res = ref = ListNode()
        for num in combined:
            ref.next = ListNode(num)
            ref = ref.next

        return res.next
        
