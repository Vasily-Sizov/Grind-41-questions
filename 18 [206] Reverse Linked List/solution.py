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

        if not head or not head.next:
            return head

        next_node = head.next
        head.next = None
        last_node = head
        head = next_node

        while next_node:
            next_node = head.next
            head.next = last_node
            last_node = head
            if next_node:
                head = next_node

        return head
