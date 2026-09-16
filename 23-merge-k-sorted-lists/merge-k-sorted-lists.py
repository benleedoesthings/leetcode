# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(list1, list2):
            dummy = ListNode()
            curr = dummy

            i = list1
            j = list2

            while i and j:
                if i.val < j.val:
                    curr.next = i
                    i = i.next
                else:
                    curr.next = j
                    j = j.next

                curr = curr.next

            while i:
                curr.next = i
                i = i.next
                curr = curr.next

            while j:
                curr.next = j
                j = j.next
                curr = curr.next

            return dummy.next

        list1 = lists[0]
        for i in range(1, len(lists)):
            list1 = merge(list1, lists[i])

        return list1