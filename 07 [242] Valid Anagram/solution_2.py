class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count: dict = {}

        # Подсчитываем символы в s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Вычитаем символы из t
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]

        return len(char_count) == 0


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram("rat", "car"))
