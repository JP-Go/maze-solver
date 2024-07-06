from graphics.constructs import Cell, Line, Point
from graphics.window import Window

CELL_SIZE = 80


if __name__ == "__main__":
    win = Window(800, 600)
    cell1 = Cell(win, (True, True, True, False))
    cell2 = Cell(win, (True, False, True, False))
    cell3 = Cell(win, (False, True, False, True))
    cell1.draw(CELL_SIZE, CELL_SIZE, 2 * CELL_SIZE, 2 * CELL_SIZE)
    cell2.draw(200, 100 + CELL_SIZE, 200 + CELL_SIZE, 100 + 2 * CELL_SIZE)
    cell3.draw(8 * CELL_SIZE, 8 * CELL_SIZE, 9 * CELL_SIZE, 9 * CELL_SIZE)

    win.redraw()
    win.wait_for_close()
