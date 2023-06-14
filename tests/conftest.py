from piethon.stack import Stack
from piethon.navigation import CodelChooser, DirectionPointer

import pytest


@pytest.fixture
def stack_obj() -> Stack:
    return Stack()
