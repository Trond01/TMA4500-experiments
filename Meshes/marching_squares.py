
import numpy as np

# Define a lookup table for the marching squares algorithm
lookupTable = {
    0: [],
    1: [(0, 0.5), (0.5, 0)],
    2: [(0.5, 0), (1, 0.5)],
    3: [(0, 0.5), (1, 0.5)],
    4: [(0.5, 1), (1, 0.5)],
    5: [(0, 0.5), (0.5, 0), (0.5, 1), (1, 0.5)],
    6: [(0.5, 0), (0.5, 1)],
    7: [(0, 0.5), (0.5, 1)],
    8: [(0.5, 1), (0, 0.5)],
    9: [(0.5, 0), (0.5, 1)],
    10: [(0, 0.5), (0.5, 0), (0.5, 1), (1, 0.5)],
    11: [(0.5, 1), (1, 0.5)],
    12: [(0, 0.5), (1, 0.5)],
    13: [(0.5, 0), (1, 0.5)],
    14: [(0, 0.5), (0.5, 0)],
    15: []
}

class marchingSquares:
    def __init__(self, f, resolution: float = 1.0):
        """
        Initialize the marching squares algorithm.

        Parameters:
        - f: Callable function to evaluate the scalar field.
        - resolution: Resolution of the grid.
        """
        self.f = f
        self.resolution = resolution

    def generate_grid(self, x_range, y_range):
        """
        Generate a grid of points and evaluate the scalar field.

        Parameters:
        - x_range: Tuple specifying the range of x values (min, max).
        - y_range: Tuple specifying the range of y values (min, max).

        Returns:
        - grid: 2D array of scalar field values.
        """
        x = np.arange(x_range[0], x_range[1], self.resolution)
        y = np.arange(y_range[0], y_range[1], self.resolution)
        xx, yy = np.meshgrid(x, y)
        grid = self.f(xx, yy)
        return grid

    def process_cell(self, cell):
        """
        Determine the edges to draw based on the cell configuration.

        Parameters:
        - cell: 2x2 array of scalar field values for a grid cell.

        Returns:
        - edges: List of edges to draw within the cell.
        """
        # Determine the case index by thresholding at 0
        threshold = 0
        case_index = 0
        if cell[0, 0] > threshold: case_index |= 1
        if cell[0, 1] > threshold: case_index |= 2
        if cell[1, 1] > threshold: case_index |= 4
        if cell[1, 0] > threshold: case_index |= 8

        return lookupTable[case_index]

    def generate_contours(self, grid):
        """
        Generate contour lines for the scalar field.

        Parameters:
        - grid: 2D array of scalar field values.

        Returns:
        - contours: List of contours as line segments.
        """
        contours = []
        rows, cols = grid.shape
        for i in range(rows - 1):
            for j in range(cols - 1):
                cell = grid[i:i+2, j:j+2]
                edges = self.process_cell(cell)
                for edge in edges:
                    contours.append(((j + edge[0][0], i + edge[0][1]),
                                     (j + edge[1][0], i + edge[1][1])))
        return contours

    def plot_result(self, contours):
        """
        Plot the resulting contours.

        Parameters:
        - contours: List of contours as line segments.
        """
        import matplotlib.pyplot as plt

        for contour in contours:
            for line in contour:
                x_values = [line[0][0], line[1][0]]
                y_values = [line[0][1], line[1][1]]
                plt.plot(x_values, y_values, 'k')

        plt.axis('equal')
        plt.show()

# Example usage
def scalar_field(x, y):
    return np.sin(x) * np.cos(y)

marcher = marchingSquares(scalar_field, resolution=0.5)
grid = marcher.generate_grid((-5, 5), (-5, 5))
contours = marcher.generate_contours(grid)
marcher.plot_result(contours)