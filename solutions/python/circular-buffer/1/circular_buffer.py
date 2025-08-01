from collections import deque

ERR_EMPTY = "Circular buffer is empty"
ERR_FULL = "Circular buffer is full"


class BufferFullException(BufferError):  # noqa: N818
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message: str) -> None:
        self.message = message


class BufferEmptyException(BufferError):  # noqa: N818
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message: str) -> None:
        self.message = message


class CircularBuffer:
    def __init__(self, capacity: int) -> None:
        self.buffer: deque = deque([], capacity)

    def read(self) -> str:
        try:
            return self.buffer.pop()
        except IndexError:
            raise BufferEmptyException(ERR_EMPTY) from None

    def write(self, data: str) -> None:
        try:
            self.buffer.insert(0, data)
        except IndexError:
            raise BufferFullException(ERR_FULL) from None

    def overwrite(self, data: str) -> None:
        self.buffer.appendleft(data)

    def clear(self) -> None:
        self.buffer.clear()
