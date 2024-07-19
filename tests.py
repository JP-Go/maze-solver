import unittest

from graphics.maze import Maze
from graphics.cell import Cell


class MazeTests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 8
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)
        self.assertFalse(maze._cells[0][0].has_left_wall)
        self.assertFalse(maze._cells[num_cols - 1][num_rows - 1].has_right_wall)

    def test_maze_create_maze_single_cell(self):
        num_cols = 1
        num_rows = 1
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)
        self.assertFalse(maze._cells[0][0].has_left_wall)
        self.assertFalse(maze._cells[num_cols - 1][num_rows - 1].has_right_wall)
        self.assertEqual(
            maze._cells[0][0].has_left_wall,
            maze._cells[num_cols - 1][num_rows - 1].has_right_wall,
        )
        self.assertTrue(maze._cells[0][0] == maze._cells[num_cols - 1][num_rows - 1])
        self.assertIsInstance(maze._cells[0][0], Cell)

    def test_maze_create_cells_zero_cells(self):
        num_cols = 0
        num_rows = 0
        self.assertRaises(ValueError, lambda: Maze(0, 0, num_rows, num_cols, 10, 10))

    def test_maze_create_cells_negative_cells(self):
        num_cols = -4
        num_rows = -4
        self.assertRaises(ValueError, lambda: Maze(0, 0, num_rows, num_cols, 10, 10))

    def test_reset_cells(self):
        num_cols = 12
        num_rows = 8
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in maze._cells:
            for cell in col:
                self.assertFalse(cell.visited)


if __name__ == "__main__":
    unittest.main()
