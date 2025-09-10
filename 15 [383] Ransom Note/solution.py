# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/description/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransomNote_store: dict = {}
        magazine_store: dict = {}

        for char in ransomNote:
            if not ransomNote_store.get(char):
                ransomNote_store[char] = 1
            else:
                ransomNote_store[char] += 1

        for char in magazine:
            if not magazine_store.get(char):
                magazine_store[char] = 1
            else:
                magazine_store[char] += 1

        for char in ransomNote_store.keys():
            if not magazine_store.get(char):
                return False
            elif ransomNote_store[char] > magazine_store[char]:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    s.canConstruct("aa", "aab")
