from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator

EMPTY_LIST_MESSAGE = "The list is empty."


class EmptyListException(Exception):  # noqa: N818
    pass


class Node:
    def __init__(self, value: Any, next_node: Node | None = None) -> None:
        self._next = next_node
        self._value = value

    def next(self) -> Node | None:
        return self._next

    def value(self) -> Any:
        return self._value


class LinkedList:
    def __init__(self, values: Iterable[Any] | None = None) -> None:
        self._head: Node | None = None
        self._len = 0
        if values:
            for value in values:
                self.push(value)

    class LLIterator:
        def __init__(self, head: Node | None) -> None:
            self._current = head

        def __iter__(self) -> LinkedList.LLIterator:
            return self

        def __next__(self) -> Any:
            if self._current is None:
                raise StopIteration

            value = self._current.value()
            self._current = self._current.next()

            return value

    def __iter__(self) -> Iterator[Any]:
        return LinkedList.LLIterator(self._head)

    def __len__(self) -> int:
        return self._len

    def head(self) -> Node:
        if self._head is None:
            raise EmptyListException(EMPTY_LIST_MESSAGE)

        return self._head

    def push(self, value: Any) -> None:
        new_head = Node(value, self._head)
        self._head = new_head
        self._len += 1

    def pop(self) -> Any:
        head = self.head()
        self._head = head.next()
        self._len -= 1

        return head.value()

    def reversed(self) -> LinkedList:
        new_list = LinkedList()
        for value in self:
            new_list.push(value)

        return new_list
