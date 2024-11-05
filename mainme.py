from window import *

def main():
    # Create a window
    win = Window(800, 600)

    # # Create some cells
    # cell1 = Cell(100, 100, 200, 200, win)  # Full walls
    # cell2 = Cell(250, 100, 350, 200, win)  # Full walls
    # cell3 = Cell(250, 250, 350, 350, win)  # Full walls

    # # Draw the cells
    # cell1.draw()
    # cell2.draw()
    # cell3.draw()

    # # Draw moves between the cells
    # cell1.draw_move(cell2)  # Red move from cell1 to cell2
    # cell2.draw_move(cell3)  # Red move from cell2 to cell3
    # cell3.draw_move(cell2, undo=True)  # Gray undo from cell3 to cell2

    # Create a maze with specified dimensions
    maze = Maze(x1=50, y1=50, num_rows=10, num_cols=10, cell_size_x=40, cell_size_y=40, win=win)


    # Wait for the window to close
    win.wait_for_close()

if __name__ == "__main__":
    main()