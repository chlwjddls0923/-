# ds.py
from __future__ import annotations
from typing import Any, Optional

class ArrayList: 

    def __init__(self):
        self._data: list[Any] = []

    def append(self, value: Any) -> None:
        """# Time: O(1) amortized, Space: O(1)
        Append value to the end.
        """
        # TODO: implement
        self._data.append(value)
        pass

    def insert(self, index: int, value: Any) -> None:
        """# Time: O(n), Space: O(1)
        Insert value at index, shifting elements to the right.
        Raise IndexError if index is out of range [0, size].
        """
        # TODO: implement
        if 0 <= index <= len(self._data):
            self._data.insert(index, value)
        else:
            raise IndexError("Index out of range")

    def remove(self, index: int) -> Any:
        """# Time: O(n), Space: O(1)
        Remove and return the element at index, shifting left.
        Raise IndexError if index is out of range.
        """
        # TODO: implement
        if 0 <= index < len(self._data):
            return self._data.pop(index)
        else:
            raise IndexError("Index out of range")        

    def get(self, index: int) -> Any:
        """# Time: O(1), Space: O(1)
        Return element at index. Raise IndexError if out of range.
        """
        # TODO: implement
        if 0 <= index < len(self._data):
            return self._data[index]
        else:
            raise IndexError("Index out of range")

    def size(self) -> int:
        """# Time: O(1), Space: O(1)"""
        # TODO: implement
        return len(self._data)

    def __len__(self) -> int:
        return self.size()


class _Node:

    def __init__(self, value: Any, next: Optional[_Node] = None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self._head: Optional[_Node] = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        """# Time: O(n), Space: O(1)
        Append value to the end.
        """
        # TODO: implement
        pass

    def _node_at(self, index: int) -> _Node:
        """# Time: O(n), Space: O(1)
        Return node at index (0-based). Raise IndexError if out of range.
        """
        # TODO: implement
        pass

    def insert(self, index: int, value: Any) -> None:
        """# Time: O(n), Space: O(1)
        Insert value at index (0..size). Raise IndexError if out of range.
        """
        # TODO: implement
        pass

    def remove(self, index: int) -> Any:
        """# Time: O(n), Space: O(1)
        Remove and return element at index. Raise IndexError if out of range.
        """
        # TODO: implement
        pass

    def get(self, index: int) -> Any:
        """# Time: O(n), Space: O(1)
        Return element at index. Raise IndexError if out of range.
        """
        if not 0 <= index < self._size:
            raise IndexError("Index out of range")

        current = self._head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        if current is None:
            raise IndexError("Index out of range")

        return current.value

    def size(self) -> int:
        """# Time: O(1), Space: O(1)"""
        # TODO: implement
        pass

    def __len__(self) -> int:
        return self.size()


class Stack:

    def __init__(self):
        self._arr = ArrayList()

    def push(self, value: Any) -> None:
        """# Time: O(1) amortized, Space: O(1)"""
        # TODO: implement
        pass

    def pop(self) -> Any:
        """# Time: O(1) amortized (ArrayList remove at end), Space: O(1)
        Raise IndexError if empty.
        """
        # TODO: implement
        pass

    def peek(self) -> Any:
        """# Time: O(1), Space: O(1)
        Raise IndexError if empty.
        """
        # TODO: implement
        pass

    def is_empty(self) -> bool:
        """# Time: O(1), Space: O(1)"""
        # TODO: implement
        pass

    def size(self) -> int:
        """# Time: O(1), Space: O(1)"""
        # TODO: implement
        pass


class Queue:

    def __init__(self):
        self._head: Optional[_Node] = None
        self._tail: Optional[_Node] = None
        self._size: int = 0

    def enqueue(self, value: Any) -> None:
        """# Time: O(1), Space: O(1)"""
        # TODO: implement
        pass

    def dequeue(self) -> Any:
        """# Time: O(1), Space: O(1)
        Remove and return front element. Raise IndexError if empty.
        """
        # TODO: implement
        pass

    def peek(self) -> Any:
        """# Time: O(1), Space: O(1)
        Return front element without removing. Raise IndexError if empty.
        """
        # TODO: implement
        pass

    def is_empty(self) -> bool:
        """# Time: O(1), Space: O(1)"""
        # TODO: implement
        pass

    def size(self) -> int:
        """# Time: O(1), Space: O(1)"""
        # TODO: implement
        pass
