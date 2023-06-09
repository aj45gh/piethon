from typing import Optional


def needs_two_items(func):
    def wrapper(self: "Stack"):
        if len(self) < 2:
            return

        return func(self)

    return wrapper


class Stack:
    def __init__(self):
        self.top = StackItem(val=None)

    def __len__(self):
        return self.top.idx

    def push(self, val: int) -> None:
        """Put a value on the top of the stack."""

        self.top = StackItem(val=val, prev=self.top)

    def pop(self) -> None:
        """Take the top value off the stack and discard it."""

        if not self.top:
            return

        self.top = self.top.prev

    @needs_two_items
    def add(self) -> None:
        """
        Take the top two values off the stack,
        add them together,
        then put the result on top.
        """

        self.top.prev += self.top
        self.pop()

    @needs_two_items
    def subtract(self) -> None:
        """
        Take the top two values off the stack,
        subtract the first from the second,
        then put the result on top.
        """

        self.top.prev -= self.top
        self.pop()

    @needs_two_items
    def multiply(self) -> None:
        """
        Take the top two values off the stack,
        multiply them together,
        then put the result on top.
        """

        self.top.prev *= self.top
        self.pop()

    @needs_two_items
    def divide(self) -> None:
        """
        Take the top two values off the stack,
        divide the second by the first,
        then put the result on top.
        """

        if self.top == 0:
            return

        self.top.prev //= self.top
        self.pop()

    @needs_two_items
    def modulo(self) -> None:
        """
        Take the top two values off the stack,
        calculate the second modulo the first,
        then put the result on top.
        """

        if self.top == 0:
            return

        self.top.prev %= self.top
        self.pop()


class StackItem:
    def __init__(self, val: int, prev: Optional["StackItem"] = None):
        self.val = val
        self.prev = prev

        self.idx = self.prev.idx + 1 if self else 0

    def __eq__(self, x: int) -> bool:
        return self.val == x

    def __bool__(self) -> bool:
        return self.val is not None

    def __iadd__(self, x: "StackItem") -> "StackItem":
        self.val += x.val
        return self

    def __isub__(self, x: "StackItem") -> "StackItem":
        self.val -= x.val
        return self

    def __imul__(self, x: "StackItem") -> "StackItem":
        self.val *= x.val
        return self

    def __floordiv__(self, x: "StackItem") -> "StackItem":
        self.val //= x.val
        return self

    def __imod__(self, x: "StackItem") -> "StackItem":
        self.val %= x.val
        return self
