# https://leetcode.com/problems/meeting-rooms/description/

"""
Time complexity: O(nlog⁡n)
Space complexity: O(1)
"""
from operator import attrgetter


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:

        intervals.sort(key=lambda i: i.start)
        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canAttendMeetings([Interval(0, 30), Interval(15, 20), Interval(5, 10)]))
