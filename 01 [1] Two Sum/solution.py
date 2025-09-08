# https://leetcode.com/problems/two-sum/

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hash_map: dict[int, int] = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_map and hash_map[target - nums[i]] != i:
                return [i, hash_map[target - nums[i]]]
            hash_map[nums[i]] = i
        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
