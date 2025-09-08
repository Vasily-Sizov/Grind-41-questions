# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        head = tmp = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                list1 = list1.next

            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next

        tmp.next = list1 if list1 else list2

        return head.next
