# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/
"""
[1,2,3,4,5]
[5,4,3,2,1]
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev, head = head, nxt
        return prev
