from graphics.constructs import Cell
from graphics.window import Window

CELL_SIZE = 80


if __name__ == "__main__":
    win = Window(800, 600)
    cell1 = Cell(win, (True, False, True, True))
    cell2 = Cell(win, (True, True, False, False))
    cell3 = Cell(win, (False, True, True, True))
    cell1.draw(0, 0, CELL_SIZE, CELL_SIZE)
    cell2.draw(CELL_SIZE, 0, 2 * CELL_SIZE, CELL_SIZE)
    cell3.draw(CELL_SIZE, CELL_SIZE, 2 * CELL_SIZE, 2 * CELL_SIZE)
    cell1.draw_move(cell2)
    cell2.draw_move(cell3)

    win.redraw()
    win.wait_for_close()
