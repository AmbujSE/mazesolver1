import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        # Check if the maze has the correct number of columns
        self.assertEqual(len(m1._cells), num_cols)
        
        # Check if each column has the correct number of rows
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_different_sizes(self):
        # Test a different maze size
        num_cols = 8
        num_rows = 6
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        # Check column count
        self.assertEqual(len(m2._cells), num_cols)
        
        # Check row count
        self.assertEqual(len(m2._cells[0]), num_rows)

    def test_cell_walls(self):
        # Create a small 1x1 maze
        m3 = Maze(0, 0, 1, 1, 10, 10)
        
        # Check that the single cell has all walls initially
        cell = m3._cells[0][0]
        self.assertTrue(cell.has_left_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_bottom_wall)

if __name__ == "__main__":
    unittest.main()
