# https://leetcode.com/problems/valid-parentheses/description/


class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char not in hashmap:  # если открывающая
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    value = stack.pop()
                    if hashmap[char] != value:
                        return False

        return not stack


s = Solution()

print(s.isValid("()"))  # true
print(s.isValid("()[]{}"))  # true
print(s.isValid("(]"))  # false
print(s.isValid("([])"))  # true
print(s.isValid("([)]"))  # true
