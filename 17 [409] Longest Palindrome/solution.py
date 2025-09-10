# 409. Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/description/


class Solution:
    def longestPalindrome(self, s: str) -> int:

        store: dict = {}
        max_length = 0
        flag_n = False

        for char in s:
            store[char] = store.get(char, 0) + 1

        for char in store.keys():
            if store[char] % 2 == 1:
                flag_n = True
                max_length += store[char] - 1
            else:
                max_length += store[char]

        if flag_n:
            return max_length + 1
        else:
            return max_length


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))
    print(s.longestPalindrome("a"))
