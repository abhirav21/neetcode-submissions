# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count+=1
            temp = temp.next

        temp1 = head
        evaluation = count-(n+1)
        if evaluation ==-1:
            return head.next
        for i in range(count-(n+1)):
            print(temp1.val)
            temp1 = temp1.next
        if temp1 and temp1.next:
            temp1.next = temp1.next.next
        
        return head



        