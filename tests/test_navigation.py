from piethon.navigation import Direction


def test_rotate_clockwise_once():
    d = Direction.RIGHT

    assert d.rotate(1) is Direction.DOWN


def test_rotate_clockwise_twice():
    d = Direction.LEFT

    assert d.rotate(2) is Direction.RIGHT


def test_rotate_counterclockwise_thrice():
    d = Direction.UP

    assert d.rotate(-3) is Direction.RIGHT


def test_rotate_counterclockwise_eight_times():
    d = Direction.RIGHT

    assert d.rotate(-8) is Direction.RIGHT
