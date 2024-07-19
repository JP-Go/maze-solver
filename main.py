from graphics.maze import Maze
from graphics.window import Window

if __name__ == "__main__":
    win = Window(801, 600)
    maze = Maze(
        80,
        80,
        12,
        16,
        40,
        40,
        win,
    )

    win.wait_for_close()
