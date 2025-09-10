# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        store: dict = {}

        for number in nums:
            store[number] = store.get(number, 0) + 1

        for value in store.values():
            if value > 1:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))  # true
    print(s.containsDuplicate([1, 2, 3, 4]))  # false
    print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # true
