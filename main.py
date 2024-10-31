from window import *
from window import Point

def main():
    # Create a window
    win = Window(800, 600)

    # Create some points
    p1 = Point(100, 100)
    p2 = Point(300, 300)
    p3 = Point(400, 100)
    p4 = Point(600, 300)

    # Create some lines between the points
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)

    # Draw the lines on the window canvas
    win.draw_line(line1, fill_color="blue")
    win.draw_line(line2, fill_color="red")

    # Create some cells with different configurations
    cell1 = Cell(100, 100, 200, 200, win)  # Full walls
    cell2 = Cell(250, 100, 350, 200, win)  # No left wall
    cell2.has_left_wall = False
    cell3 = Cell(100, 250, 200, 350, win)  # No bottom wall
    cell3.has_bottom_wall = False
    cell4 = Cell(250, 250, 350, 350, win)  # No right and top walls
    cell4.has_right_wall = False
    cell4.has_top_wall = False

    # Draw the cells
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()

    # Create some cells
    cell1 = Cell(100, 100, 200, 200, win)  # Full walls
    cell2 = Cell(250, 100, 350, 200, win)  # Full walls
    cell3 = Cell(250, 250, 350, 350, win)  # Full walls

    # Draw the cells
    cell1.draw()
    cell2.draw()
    cell3.draw()

    # Draw moves between the cells
    cell1.draw_move(cell2)  # Red move from cell1 to cell2
    cell2.draw_move(cell3)  # Red move from cell2 to cell3
    cell3.draw_move(cell2, undo=True)  # Gray undo from cell3 to cell2

    # Wait for the window to close
    win.wait_for_close()

if __name__ == "__main__":
    main()
    