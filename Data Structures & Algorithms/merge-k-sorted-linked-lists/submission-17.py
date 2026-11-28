# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    class NodeWrapper():
        def __init__(self, node):
            self.node = node
        
        def __lt__(self, other):
            return self.node.val < other.node.val

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        if len(lists) == 0:
            return None

        for lt in lists:
            if lt:
                heapq.heappush(heap, self.NodeWrapper(lt))

        ref = dummy = ListNode()

        while heap:
            nodeWrapper = heapq.heappop(heap)

            dummy.next = nodeWrapper.node
            dummy = dummy.next
            if nodeWrapper.node and nodeWrapper.node.next:
                heapq.heappush(heap, self.NodeWrapper(nodeWrapper.node.next))

        return ref.next