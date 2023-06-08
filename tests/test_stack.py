from piethon.stack import Stack

import pytest


@pytest.fixture
def stack_obj() -> Stack:
    return Stack()


def test_stack_push_value(stack_obj):
    stack_obj.push(1)
    assert stack_obj.top == 1

    stack_obj.push(2)
    assert stack_obj.top == 2
    assert stack_obj.top.prev == 1


def test_stack_push_length(stack_obj):
    assert len(stack_obj) == 0

    stack_obj.push(0)
    assert len(stack_obj) == 1

    stack_obj.push(0)
    assert len(stack_obj) == 2


def test_stack_pop(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.pop()

    assert stack_obj.top == 1


def test_stack_pop_nothing(stack_obj):
    stack_obj.pop()


def test_stack_add(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.add()

    assert stack_obj.top == 3
    assert len(stack_obj) == 1


def test_stack_add_nothing(stack_obj):
    stack_obj.push(1)
    stack_obj.add()

    assert len(stack_obj) == 1


def test_stack_subtract(stack_obj):
    stack_obj.push(3)
    stack_obj.push(2)
    stack_obj.subtract()

    assert stack_obj.top == 1
    assert len(stack_obj) == 1


def test_subtract_negative(stack_obj):
    stack_obj.push(2)
    stack_obj.push(3)
    stack_obj.subtract()

    assert stack_obj.top == -1
    assert len(stack_obj) == 1


def test_subtract_nothing(stack_obj):
    stack_obj.push(2)
    stack_obj.subtract()

    assert len(stack_obj) == 1


def test_multiply(stack_obj):
    stack_obj.push(5)
    stack_obj.push(10)
    stack_obj.multiply()

    assert stack_obj.top == 50
