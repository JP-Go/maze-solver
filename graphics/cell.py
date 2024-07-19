from .primitives import Line, Point
from typing import Literal, Self


class Cell:

    def __init__(
        self,
        win,
        walls: tuple[bool, bool, bool, bool] = (True, True, True, True),
    ) -> None:

        self._x1 = 0.0
        self._y1 = 0.0
        self._x2 = 0.0
        self._y2 = 0.0
        (
            self.has_top_wall,
            self.has_right_wall,
            self.has_bottom_wall,
            self.has_left_wall,
        ) = walls
        self._win = win
        self.visited = False

    def draw(self, x1: float, y1: float, x2: float, y2: float):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self._win is None:
            return
        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "white"
            )
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "white"
            )
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "white"
            )
        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "white"
            )

    def break_wall(self, wall: Literal["left", "right", "top", "bottom"]):
        match wall:
            case "left":
                self.has_left_wall = False
            case "right":
                self.has_right_wall = False
            case "top":
                self.has_top_wall = False
            case "bottom":
                self.has_bottom_wall = False

    def __was_drawn(self):
        return self._x1 != self._x2 and self._y1 != self._y2

    def center_point(self) -> Point:
        if not self.__was_drawn():
            raise RuntimeError("Cell needs to be drawn first")
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

    def draw_move(self, to_cell: Self, undo=True):
        if not self.__was_drawn():
            raise RuntimeError("Cell needs to be drawn first")
        start_point = self.center_point()
        end_point = to_cell.center_point()
        color = "gray" if undo else "red"
        self._win.draw_line(Line(start_point, end_point), color)

    def __str__(self) -> str:
        return (
            f"Cell(x1={self._x1},x2={self._x2},y1={self._y1},y2={self._y2},"
            f"walls=[top={self.has_top_wall},left={self.has_left_wall},bottom={self.has_bottom_wall},right={self.has_right_wall}])"
        )
