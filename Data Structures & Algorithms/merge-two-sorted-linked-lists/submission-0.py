# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            check while there is still list1 and list2, with list1 being the main return list, 
            check if the item in list2 is less than the current list1 node and if it is setting
            the current list1 node to the list2 node with the next element to track the next list1
            node and then continue if the list2 node is larger to keep going until its smaller

            -> then if the list1 node has been exhausested to just add the list2 node unto the end
            of list1 or if list2 is exhauseted to just return list1 
        '''

        new_list = ListNode()
        ref = new_list

        while list1 and list2:
            if list1.val < list2.val:
                ref.next = list1
                list1 = list1.next

            else:
                ref.next = list2
                list2 = list2.next

            ref = ref.next

        ref.next = list1 if list1 else list2

        return new_list.next
        