from typing import Optional


def needs_one_item(func):
    def wrapper(self: "Stack"):
        if len(self) > 0:
            return func(self)

    return wrapper


def needs_two_items(func):
    def wrapper(self: "Stack"):
        if len(self) > 1:
            return func(self)

    return wrapper


def does_division(func):
    @needs_two_items
    def wrapper(self: "Stack"):
        if self.top != 0:
            return func(self)

    return wrapper


class Stack:
    def __init__(self):
        self.top = StackItem(val=None)

    def __len__(self):
        return self.top.idx

    def __iter__(self):
        i = self.top
        while i:
            yield i.val
            i = i.prev

    def push(self, val: int) -> None:
        """Put a value on the top of the stack."""

        self.top = StackItem(val=val, prev=self.top)

    def pop(self) -> None:
        """Take the top value off the stack and discard it."""

        if self.top:
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

    @does_division
    def divide(self) -> None:
        """
        Take the top two values off the stack,
        divide the second by the first,
        then put the result on top.
        """

        self.top.prev //= self.top
        self.pop()

    @does_division
    def modulo(self) -> None:
        """
        Take the top two values off the stack,
        calculate the second modulo the first,
        then put the result on top.
        """

        self.top.prev %= self.top
        self.pop()

    @needs_one_item
    def negate(self) -> None:
        """
        Replace the top value of the stack with zero if it is non-zero,
        or 1 if it is zero.
        """

        self.top.val = int(not bool(self.top.val))

    @needs_two_items
    def greater(self) -> None:
        """
        Take the top two values off the stack,
        then put 1 on top if the second value is greater,
        or 0 if it is not greater.
        """

        self.top.prev.val = int(self.top.prev > self.top)
        self.pop()

    def pointer(self) -> None:
        raise NotImplementedError

    def switch(self) -> None:
        raise NotImplementedError

    @needs_one_item
    def duplicate(self) -> None:
        """
        Put a copy of the top value on top of the stack.
        """

        self.push(self.top.val)

    def roll(self) -> None:
        num_rolls = self.top.val
        self.pop()

        depth = self.top.val
        self.pop()

        if num_rolls < 0:
            num_rolls = depth - num_rolls

        for _ in range(0, num_rolls):
            move = self.top
            next = move

            for _ in range(1, depth):
                next = next.prev

            self.pop()

            move.prev = next.prev
            next.prev = move

    def stdin(self, val: int) -> None:
        raise NotImplementedError

    def stdout(self) -> int:
        raise NotImplementedError


class StackItem:
    def __init__(self, val: int, prev: Optional["StackItem"] = None):
        self.val = val
        self.prev = prev

    @property
    def prev(self) -> "StackItem":
        return self._prev

    @prev.setter
    def prev(self, val: "StackItem") -> None:
        self._prev = val
        self.update_idx()

    def update_idx(self):
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

    def __gt__(self, x: "StackItem") -> bool:
        return self.val > x.val
