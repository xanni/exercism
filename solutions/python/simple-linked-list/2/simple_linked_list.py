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
    def __init__(self, values: Iterable[Any] = []) -> None:
        self._head: Node | None = None
        self._len = 0
        for value in values:
            self.push(value)

    def __iter__(self) -> Iterator[Any]:
        node = self._head
        while node is not None:
            yield node.value()
            node = node.next()

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
        return LinkedList(self)
