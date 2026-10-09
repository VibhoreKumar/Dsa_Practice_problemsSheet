# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        arr=[]
        curr = head
        # Step 1: Store all values
        while curr:
            arr.append(curr.val)
            curr = curr.next
        # Step 2: Sort the values
        arr.sort()

        # Step 3: Put sorted values back
        curr = head
        i = 0

        while curr:
            curr.val = arr[i]
            i += 1
            curr = curr.next

        return head
