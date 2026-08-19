# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        honestly, i like my solution better
        '''
        def convert(LL):
            ref = LL
            string = ''

            while ref:
                string+=str(ref.val)
                ref = ref.next

            return int(string[::-1])

        summ = str(convert(l1) + convert(l2))
        print(convert(l1), print(convert(l2)))
        dRef = dummy = ListNode(summ[len(summ)-1])
        for i in range(len(summ)-2, -1, -1):
            dRef.next = ListNode(int(summ[i]))
            dRef = dRef.next
        
        return dummy