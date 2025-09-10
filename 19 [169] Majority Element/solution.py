# 169. Majority Element
# https://leetcode.com/problems/majority-element/description/

"""
Follow-up: Could you solve the problem in linear time and in O(1) space?

Очень долго думал над задачей, но так и не догадался.
Вся суть догадки в условии - Majority Element - это элемент, который содержится строго больше n/2 раз.

В таком случае алгоритм следующий:
- Выбираем какой-то элемент главным и начинаем его копить, если идут повторы
- Если идут другие значений, то наоборот минусуем.
- Как только выходим в 0, можем взять другой элемент

Суть в том, что так как главный элемент содержится больше n/2 раз, то именно он и останется как Majority Element.
"""
from typing import Optional


class Solution:
    def majorityElement(self, nums: list[int]) -> Optional[int]:

        majority = None
        counter = 0

        for number in nums:
            if counter == 0:
                majority = number
            if majority == number:
                counter += 1
            else:
                counter -= 1

        return majority


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 2, 3]))  # 3
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
