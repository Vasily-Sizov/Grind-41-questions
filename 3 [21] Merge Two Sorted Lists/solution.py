# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        tmp = head = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next  # Правильное обновление cur

        # Присоединяем оставшиеся узлы
        tmp.next = list1 if list1 else list2

        return head.next


def create_linked_list(values: list) -> Optional[ListNode]:
    """
    Создает связный список из массива значений

    Args:
        values: Список значений для создания связного списка

    Returns:
        Голова созданного связного списка
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def print_linked_list(head: Optional[ListNode]) -> str:
    """
    Преобразует связный список в строковое представление

    Args:
        head: Голова связного списка

    Returns:
        Строковое представление списка
    """
    if not head:
        return "[]"

    result = []
    current = head

    while current:
        result.append(str(current.val))
        current = current.next

    return " -> ".join(result)


def test_merge_lists():
    """Тестирует алгоритм слияния списков с заданными данными"""

    print("=== Тестирование слияния двух отсортированных связных списков ===\n")

    # Создаем тестовые данные
    list1_values = [1, 2, 2, 2, 2]
    list2_values = [1, 3, 4]

    print(f"Исходные данные:")
    print(f"list1: {list1_values}")
    print(f"list2: {list2_values}")
    print()

    # Создаем связные списки
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)

    print("Связные списки:")
    print(f"list1: {print_linked_list(list1)}")
    print(f"list2: {print_linked_list(list2)}")
    print()

    # Создаем решение и выполняем слияние
    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)

    print("Результат слияния:")
    print(f"merged: {print_linked_list(merged_list)}")
    print()

    # Ожидаемый результат
    expected = [1, 1, 2, 2, 2, 2, 3, 4]
    print(f"Ожидаемый результат: {expected}")

    # Проверяем корректность
    result_values = []
    current = merged_list
    while current:
        result_values.append(current.val)
        current = current.next

    print(f"Фактический результат: {result_values}")
    print(
        f"Тест {'ПРОЙДЕН' if result_values == expected else 'НЕ ПРОЙДЕН'} ✓"
        if result_values == expected
        else "Тест НЕ ПРОЙДЕН ✗"
    )


test_merge_lists()
