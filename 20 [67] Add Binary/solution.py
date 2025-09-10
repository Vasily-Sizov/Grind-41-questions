# 67. Add Binary
# https://leetcode.com/problems/add-binary/description/

"""
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []

        idxA, idxB = len(a) - 1, len(b) - 1

        while idxA >= 0 or idxB >= 0 or carry == 1:
            if idxA >= 0:
                carry += int(a[idxA])
                idxA -= 1
            if idxB >= 0:
                carry += int(b[idxB])
                idxB -= 1

            res.append(str(carry % 2))
            carry = carry // 2
        res.reverse()
        return "".join(res)


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("1", "11"))  # 100
    print(s.addBinary("1010", "1011"))  # 10101
