from tkinter import Canvas
from typing import Optional

# from graphics.window import Window


class Point:

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Line:

    def __init__(self, start_point: Point, end_point: Point) -> None:
        self.start_point = start_point
        self.end_point = end_point

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.start_point.x,
            self.start_point.y,
            self.end_point.x,
            self.end_point.y,
            fill=fill_color,
            width=2,
        )


class Cell:

    def __init__(
        self,
        win,
        walls: tuple[bool, bool, bool, bool] = (True, True, True, True),
    ) -> None:

        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0
        (
            self.has_top_wall,
            self.has_right_wall,
            self.has_bottom_wall,
            self.has_left_wall,
        ) = walls
        self._win = win

    def draw(self, x1: float, y1: float, x2: float, y2: float):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black"
            )
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black"
            )
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black"
            )
        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black"
            )
