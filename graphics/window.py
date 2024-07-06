from tkinter import Tk, BOTH, Canvas

from .constructs import Line


class Window:

    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title("Maze solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__running = False
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False
