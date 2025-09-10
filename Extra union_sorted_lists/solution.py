"""
Задача:
Даны два отсортированных списка.
Необходимо объединить их в один отсортированный список.

Решение:
Данная задача решена методом двух указателей. 

Пока решал - забыл, что срезы в питоне безопасны. То есть можно вызвать любой срез
и исключения не будет. 

Поэтому идем пока не дошли до финальной границы одного из списоков.
Потом уже добавляем остаток.

Вычислительная сложность: O(n+m)
Пространственная сложность: O(n+m)
"""

class Solution:
    def union_sorted_list(self, list1: list[int], list2: list[int]) -> list[int]:
        p1 = p2 = 0
        result = []

        while p1 < len(list1) and p2 < len(list2):
            if list1[p1] <= list2[p2]:
                result.append(list1[p1])
                p1 += 1
            else:
                result.append(list2[p2])
                p2 += 1

        result += list1[p1:]
        result += list2[p2:]
        
        return result
    
list1 = [1,4,5,6]
list2 = [1,7,8]

list3 = [1,1,4,5,6,7,8]

s = Solution()
print(s.union_sorted_list(list1, list2))