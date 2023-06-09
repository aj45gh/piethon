# Push
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


# Pop
def test_stack_pop(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)

    stack_obj.pop()
    assert stack_obj.top == 1


def test_stack_pop_nothing(stack_obj):
    stack_obj.pop()


# Add
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


# Subtract
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


# Multiply
def test_multiply(stack_obj):
    stack_obj.push(5)
    stack_obj.push(10)

    stack_obj.multiply()
    assert stack_obj.top == 50


def test_multiply_by_one(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)

    stack_obj.multiply()
    assert stack_obj.top == 2


def test_multiply_by_zero(stack_obj):
    stack_obj.push(100)
    stack_obj.push(0)

    stack_obj.multiply()
    assert stack_obj.top == 0


def test_multiply_negative(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)

    stack_obj.subtract()
    assert stack_obj.top == -1

    stack_obj.push(100)

    stack_obj.multiply()
    assert stack_obj.top == -100


def test_multiply_nothing(stack_obj):
    stack_obj.multiply()
    assert len(stack_obj) == 0


# Divide
def test_divide(stack_obj):
    stack_obj.push(8)
    stack_obj.push(2)

    stack_obj.divide()
    assert stack_obj.top == 4


def test_divide_nothing(stack_obj):
    stack_obj.push(1)

    stack_obj.divide()
    assert len(stack_obj) == 1


def test_divide_floor(stack_obj):
    stack_obj.push(21)
    stack_obj.push(2)

    stack_obj.divide()
    assert stack_obj.top == 10


def test_divide_by_one(stack_obj):
    stack_obj.push(100)
    stack_obj.push(1)

    stack_obj.divide()
    assert stack_obj.top == 100


def test_divide_by_zero(stack_obj):
    stack_obj.push(20)
    stack_obj.push(0)

    stack_obj.divide()
    assert stack_obj.top == 0


def test_negative_division(stack_obj):
    stack_obj.push(10)
    stack_obj.push(20)

    stack_obj.subtract()
    assert stack_obj.top == -10

    stack_obj.push(2)
    stack_obj.divide()

    assert stack_obj.top == -5


# Modulo
def test_modulo_remainder(stack_obj):
    stack_obj.push(3)
    stack_obj.push(2)

    stack_obj.modulo()
    assert stack_obj.top == 1


def test_modulo_nothing(stack_obj):
    stack_obj.push(10)

    stack_obj.modulo()
    assert stack_obj.top == 10


def test_modulo_by_zero(stack_obj):
    stack_obj.push(300)
    stack_obj.push(0)

    stack_obj.modulo()
    assert stack_obj.top == 0


def test_modulo_negative(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)

    stack_obj.subtract()
    assert stack_obj.top == -1

    stack_obj.push(3)

    stack_obj.modulo()
    assert stack_obj.top == 2


# Not/negate
def test_negate_positive(stack_obj):
    stack_obj.push(1)

    stack_obj.negate()
    assert stack_obj.top == 0


def test_negate_zero(stack_obj):
    stack_obj.push(0)

    stack_obj.negate()
    assert stack_obj.top == 1


def test_negate_negative(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)

    stack_obj.subtract()
    assert stack_obj.top == -1

    stack_obj.negate()
    assert stack_obj.top == 0


def test_negate_empty(stack_obj):
    stack_obj.negate()
    assert stack_obj.top.val is None


# Greater
def test_greater_true(stack_obj):
    stack_obj.push(3)
    stack_obj.push(2)

    stack_obj.greater()
    assert stack_obj.top == 1


def test_greater_false(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)

    stack_obj.greater()
    assert stack_obj.top == 0


def test_greater_equal(stack_obj):
    stack_obj.push(1)
    stack_obj.push(1)

    stack_obj.greater()
    assert stack_obj.top == 0


def test_greater_negative(stack_obj):
    stack_obj.push(-1)
    stack_obj.push(-2)

    stack_obj.greater()
    assert stack_obj.top == 1


def test_greater_empty(stack_obj):
    stack_obj.greater()
    assert stack_obj.top.val is None


# Duplicate
def test_duplicate(stack_obj):
    stack_obj.push(1)

    stack_obj.duplicate()
    assert stack_obj.top.prev == 1
    assert len(stack_obj) == 2


def test_duplicate_empty(stack_obj):
    stack_obj.duplicate()
    assert stack_obj.top.prev is None


# Roll
def test_roll_once_by_two(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(3)
    stack_obj.push(4)
    stack_obj.push(5)

    stack_obj.push(2)
    stack_obj.push(1)

    stack_obj.roll()
    assert [*stack_obj] == [4, 5, 3, 2, 1]


def test_roll_once_by_three(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(3)
    stack_obj.push(4)
    stack_obj.push(5)

    stack_obj.push(3)
    stack_obj.push(1)

    stack_obj.roll()
    assert [*stack_obj] == [4, 3, 5, 2, 1]


def test_roll_twice_by_two(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(3)
    stack_obj.push(4)
    stack_obj.push(5)

    stack_obj.push(2)
    stack_obj.push(2)

    stack_obj.roll()
    assert [*stack_obj] == [5, 4, 3, 2, 1]


def test_roll_twice_by_three(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(3)
    stack_obj.push(4)
    stack_obj.push(5)

    stack_obj.push(3)
    stack_obj.push(2)

    stack_obj.roll()
    assert [*stack_obj] == [3, 5, 4, 2, 1]


def test_roll_negative_once_by_three(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(3)
    stack_obj.push(4)
    stack_obj.push(5)

    stack_obj.push(3)

    stack_obj.push(1)
    stack_obj.push(3)
    stack_obj.subtract()

    stack_obj.roll()
    assert [*stack_obj] == [3, 5, 4, 2, 1]


# __iter__
def test_iter(stack_obj):
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(2)

    assert [*stack_obj] == [2, 2, 1]
