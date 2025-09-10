# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

"""
Долго думал куда писать пустые значения. 
Оказалось все просто - нужно просто идти с максимума к минимуму и заполнять в обратную сторону.
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        p1 = m-1
        p2 = n-1
        p_end = m+n-1

        while p1 >=0 and p2>=0:
            if nums1[p1] >= nums2[p2]:
                nums1[p_end] = nums1[p1]
                p1-=1
            else:
                nums1[p_end] = nums2[p2]
                p2-=1
            p_end -=1
        
        while p2 >= 0:
            nums1[p_end] = nums2[p2]
            p2-=1
            p_end -=1

        print(nums1)

s = Solution()
s.merge([1,2,3,7,0,0,0], 4, [2,5,6], 3)
s.merge([3,3,4,7,0,0,0], 4, [2,2,2], 3)
s.merge([1], 1, [], 0)
s.merge([0], 0, [1], 1)