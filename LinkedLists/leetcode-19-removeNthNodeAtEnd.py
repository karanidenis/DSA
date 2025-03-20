# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        first = 
        
        # if len(head) < n+1 or len(head) ==  n +  1:
        #     # pop tail
        #     pass
        # else:
        #     # pop tail.next