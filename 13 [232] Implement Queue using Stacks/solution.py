# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/description/


class MyQueue:

    def __init__(self):
        """Инициализируем два стека"""
        self.input_stack = []  # Для входящих элементов
        self.output_stack = []  # Для исходящих элементов

    def push(self, x: int) -> None:
        """Добавляет элемент x в конец очереди"""
        self.input_stack.append(x)

    def pop(self) -> int:
        """Удаляет элемент из начала очереди и возвращает его"""
        self._ensure_output_has_elements()
        return self.output_stack.pop()

    def peek(self) -> int:
        """Возвращает элемент в начале очереди"""
        self._ensure_output_has_elements()
        return self.output_stack[-1]

    def empty(self) -> bool:
        """Возвращает true, если очередь пуста"""
        return len(self.input_stack) == 0 and len(self.output_stack) == 0

    def _ensure_output_has_elements(self) -> None:
        """Перекладывает элементы из input в output, если output пуст"""
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
