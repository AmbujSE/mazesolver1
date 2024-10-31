from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Line class to represent a line between two points
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="black"):
        """Draw the line on the canvas with the specified fill color."""
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y,
            fill=fill_color, width=2
        )

# Window class for creating and managing the tkinter window
class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Create the root widget
        self.root = Tk()
        self.root.title("Maze Solver")

        # Create a Canvas widget
        self.canvas = Canvas(self.root, bg="white", width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=True)

        # Window running state
        self.running = False

        # Protocol to handle window close button
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """Redraw the graphics on the window."""
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        """Run the window until it is closed."""
        self.running = True
        while self.running:
            self.redraw()
            

    def close(self):
        """Stop the window loop and close the window."""
        self.running = False

    def draw_line(self, line, fill_color="black"):
        """Draw a line on the canvas."""
        line.draw(self.canvas, fill_color)

# Cell class to represent an individual cell in the maze grid
class Cell:
    def __init__(self, x1, y1, x2, y2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window

    def draw(self):
        """Draw the cell with its walls."""
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, fill_color="black")
        
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, fill_color="black")
            
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, fill_color="black")

        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, fill_color="black")

    def draw_move(self, to_cell, undo=False):
        """Draw a move from this cell to the to_cell, optionally in undo mode."""
        # Calculate the center of the current cell
        center_self = Point(
            (self._x1 + self._x2) // 2,
            (self._y1 + self._y2) // 2
        )

        # Calculate the center of the target cell
        center_to = Point(
            (to_cell._x1 + to_cell._x2) // 2,
            (to_cell._y1 + to_cell._y2) // 2
        )

        # Set the color based on whether this is a move or an undo
        fill_color = "gray" if undo else "red"

        # Draw the line representing the move
        move_line = Line(center_self, center_to)
        self._win.draw_line(move_line, fill_color)