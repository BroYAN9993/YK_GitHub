"""
File: grid.py

A Grid is a dyadic array based on class Array.
"""

from arrays import Array

class Grid(object):
    """
    Represent a two-dimensional array.
    """

    def __init__(self, rows, colums, fillValue = None):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(colums, fillValue)

    def getHeight(self):
        """
        Return the number of rows.
        """
        return len(self._data)

    def getWidth(self):
        """
        Return the number of cloumns.
        """
        return len(self._data[0])

    def __getitem__(self, index):
        """
        Support tow-dimensional indexing with [row][colum].
        """
        return self._data[index]

    def __str__(self):
        """
        Return a string representation of the gird.
        """
        result = ''
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self._data[row][col]) + ' '
            result += '\n'
        return result
