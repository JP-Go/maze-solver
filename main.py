from graphics.maze import Maze
from graphics.window import Window

if __name__ == "__main__":
    win = Window(800, 600)

    maze = Maze(
        80,
        80,
        20,
        20,
        30,
        40,
        win,
    )

    maze.solve()

    win.wait_for_close()
