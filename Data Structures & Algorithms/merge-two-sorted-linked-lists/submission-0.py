# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2
        newList = ListNode(0)
        head = newList

        while curr1 and curr2:
            node = None
            if curr1.val < curr2.val:
                node = ListNode(curr1.val)
                curr1 = curr1.next
            elif curr2.val < curr1.val:
                node = ListNode(curr2.val)
                curr2 = curr2.next
            elif curr2.val == curr1.val:
                node = ListNode(curr2.val)
                node1 = ListNode(curr1.val)
                
                curr1 = curr1.next
                curr2 = curr2.next
                newList.next = node1
                newList = newList.next   

            newList.next = node
            newList = newList.next

        while curr1:
            node = ListNode(curr1.val)
            newList.next = node
            curr1 = curr1.next
            newList = newList.next
        while curr2:
            node = ListNode(curr2.val)
            newList.next = node
            curr2 = curr2.next
            newList = newList.next
        return head.next
        



            

        