from typing import List
from .cell import Cell
from .primitives import Point
from time import sleep
import random


class Maze:

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        random_seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells: List[List[Cell]] = []
        self._seed = random_seed
        self._animation_time = 0.01
        if random_seed is not None:
            random.seed(self._seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited_cells()

    def _create_cells(self):
        if not self.__valid_maze():
            raise ValueError("Maze must have at least 1 row and 1 column")
        for i in range(self._num_cols):
            col = []
            self._cells.append(col)
            for j in range(self._num_rows):
                cell = Cell(
                    self._win,
                )
                col.append(cell)
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell_top_left = Point(
            self._x1 + i * self._cell_size_x, self._y1 + j * self._cell_size_y
        )
        cell_bottom_right = Point(
            self._x1 + (i + 1) * self._cell_size_x,
            self._y1 + (j + 1) * self._cell_size_y,
        )
        cell = self._cells[i][j]
        cell.draw(
            cell_top_left.x, cell_top_left.y, cell_bottom_right.x, cell_bottom_right.y
        )
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        sleep(self._animation_time)
        self._win.redraw()

    def _break_entrance_and_exit(self):
        if len(self._cells) == 0:
            return
        self._cells[0][0].break_wall("left")
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].break_wall("right")
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def __valid_maze(self):
        return self._num_cols > 0 and self._num_rows > 0

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        oposites = {"left": "right", "right": "left", "top": "bottom", "bottom": "top"}
        while True:
            to_visit: list[tuple[int, int, str]] = []
            if i + 1 < self._num_cols and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j, "right"))
            if i - 1 >= 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j, "left"))
            if j + 1 < self._num_rows and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1, "bottom"))
            if j - 1 >= 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1, "top"))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            new_direction = to_visit[random.randint(0, len(to_visit) - 1)]
            current.break_wall(new_direction[2])
            self._cells[new_direction[0]][new_direction[1]].break_wall(
                oposites[new_direction[2]]
            )
            self._break_walls_r(new_direction[0], new_direction[1])

    def _reset_visited_cells(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _has_wall_between(self, i, j, wall):
        return self._cells[i][j].has_wall(wall)

    def _is_valid_cell(self, i: int, j: int):
        return i >= 0 and i < self._num_cols and j >= 0 and j < self._num_rows

    def _visited(self, i: int, j: int):
        return self._cells[i][j].visited

    def _at_end(self, i: int, j: int):
        return i == self._num_cols - 1 and j == self._num_rows - 1
