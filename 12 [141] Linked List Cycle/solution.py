"""
Понимал в данной задаче, что нужно исползовать 2 указателя, но не понимал как.
Догадался:
- пускаем 2 указателя:  +1 шаг и +2 шага.
- вне зависимости от того, какое расстояние между шагами, указатели всегда встретятся, если они в цикле.
Быстрый сначала перегонит, а потом догонит.

Получается, что пока идет медленный указатель, быстрый идет вперед.
И если они встретились, то есть цикл, а если не встретились, то нет цикла.

И все это, пока идет медленный до самого конца.

Time complexity: O(n)
Space complexity: O(1)

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
