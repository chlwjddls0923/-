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
        new_node = _Node(value)
        if self._head is None:
            self._head = new_node
        else:
            curr = self._head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def _node_at(self, index: int) -> _Node:
        """# Time: O(n), Space: O(1)
        Return node at index (0-based). Raise IndexError if out of range.
        """
        if 0 <= index < self._size:
            curr = self._head
            for _ in range(index):
                curr = curr.next
            return curr
        else:
            raise IndexError("Index out of range")

    def insert(self, index: int, value: Any) -> None:
        """# Time: O(n), Space: O(1)
        Insert value at index (0..size). Raise IndexError if out of range.
        """
        if not (0 <= index <= self._size):
            raise IndexError("Index out of range")
        
        new_node = _Node(value)

        if index == 0:
            new_node.next = self._head
            self._head = new_node
        else:
            prev = self._node_at(index - 1)
            new_node.next = prev.next
            prev.next = new_node

        self._size += 1

    def remove(self, index: int) -> Any:
        """# Time: O(n), Space: O(1)
        Remove and return element at index. Raise IndexError if out of range.
        """
        if not ( 0 <= index < self._size):
            raise IndexError("Index out of range")
        
        if index == 0:
            removed = self._head
            self._head = self._head.next
        else:
            prev = self._node_at(index - 1)
            removed = prev.next
            prev.next = removed.next

        self._size -= 1
        return removed.value

    def get(self, index: int) -> Any:
        """# Time: O(n), Space: O(1)
        Return element at index. Raise IndexError if out of range.
        """
        return self._node_at(index).value

    def size(self) -> int:
        """# Time: O(1), Space: O(1)"""
        return self._size

    def __len__(self) -> int:
        return self.size()


class Stack:

    def __init__(self):
        self._data: list[Any] = []

    def push(self, value: Any) -> None:
        """# Time: O(1) amortized, Space: O(1)"""
        self._data.append(value)

    def pop(self) -> Any:
        """# Time: O(1) amortized (ArrayList remove at end), Space: O(1)
        Raise IndexError if empty.
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any:
        """# Time: O(1), Space: O(1)
        Raise IndexError if empty.
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        """# Time: O(1), Space: O(1)"""
        return len(self._data) == 0

    def size(self) -> int:
        """# Time: O(1), Space: O(1)"""
        return len(self._data)


class Queue:

    def __init__(self):
        self._head: Optional[_Node] = None
        self._tail: Optional[_Node] = None
        self._size: int = 0

    def enqueue(self, value: Any) -> None:
        """# Time: O(1), Space: O(1)"""
        new_node = _Node(value)
        if self._tail is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def dequeue(self) -> Any:
        """# Time: O(1), Space: O(1)
        Remove and return front element. Raise IndexError if empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        removed = self._head
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return removed.value     
    

    def peek(self) -> Any:
        """# Time: O(1), Space: O(1)
        Return front element without removing. Raise IndexError if empty.
        """
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self._head.value

    def is_empty(self) -> bool:
        """# Time: O(1), Space: O(1)"""
        return self._size == 0

    def size(self) -> int:
        """# Time: O(1), Space: O(1)"""
        return self._size
