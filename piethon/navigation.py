from enum import Enum


class Direction(Enum):
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4

    def rotate(self, rotations: int) -> "Direction":
        idx = self.value + rotations
        return Direction(idx % len(Direction))


class CodelChooser:
    ...


class DirectionPointer:
    direction = Direction.RIGHT

    def rotate(self, rotations: int) -> None:
        self.direction = self.direction.rotate(rotations)
