class Solution:
    def search(self, nums: list[int], target: int) -> int:

        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            med = (p1 + p2) // 2

            if target > nums[med]:
                p1 = med + 1
            elif target < nums[med]:
                p2 = med - 1
            else:
                return med
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 9))
    print(s.search([-1, 0, 3, 5, 9, 12], 2))
