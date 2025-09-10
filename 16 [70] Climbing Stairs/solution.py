# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        one_steps_before, two_steps_before = 2, 1

        for _ in range(3, n + 1):
            curr = one_steps_before + two_steps_before
            two_steps_before, one_steps_before = one_steps_before, curr
        return curr
