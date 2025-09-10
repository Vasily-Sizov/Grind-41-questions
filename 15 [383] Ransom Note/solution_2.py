# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/description/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        counts: dict = {}
        for ch in magazine:
            counts[ch] = counts.get(ch, 0) + 1

        for ch in ransomNote:
            left = counts.get(ch, 0) - 1
            if left < 0:
                return False
            counts[ch] = left

        return True
