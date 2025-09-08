# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: s = "race a car"
# Output: false

# Example 3:
# Input: s = " "
# Output: true
"""
Забыл, что isalnum - проверяет содержит ли строка буквы и цифры.
Возвращает True или False.
isalpha(), например, только для букв (и русских и английских)
isdigit() - для цифр обычных
isnumeric() - даже для римских цифр
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        return cleaned == cleaned[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
    print(s.isPalindrome(" "))
