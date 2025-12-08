"""
This script demonstrates two styles of documentation for the same `Rectangle` class:
1. AI-generated docstrings and inline comments
2. Manually written docstrings and inline comments

It also shows a comparison of both styles.
"""


# -------------------------------------------------------------
# 1️⃣ Rectangle Class with AI-GENERATED DOCSTRINGS & COMMENTS
# -------------------------------------------------------------

class RectangleAI:
    """
    Represents a geometric rectangle and provides utility methods for
    calculating fundamental properties such as area and perimeter.

    Attributes
    ----------
    width : float
        The horizontal dimension of the rectangle.
    height : float
        The vertical dimension of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a RectangleAI instance with defined width and height.

        Parameters
        ----------
        width : float
            The rectangle's width dimension.
        height : float
            The rectangle's height dimension.

        Notes
        -----
        This constructor does not enforce type checking. Users are expected
        to pass valid numeric values.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Compute the total surface area of the rectangle.

        Returns
        -------
        float
            The area obtained by multiplying width and height.

        Examples
        --------
        >>> RectangleAI(3, 4).area()
        12
        """
        return self.width * self.height

    def perimeter(self):
        """
        Determine the total perimeter length of the rectangle.

        Returns
        -------
        float
            The perimeter calculated as 2 * (width + height).

        Examples
        --------
        >>> RectangleAI(3, 4).perimeter()
        14
        """
        return 2 * (self.width + self.height)


# -------------------------------------------------------------
# 2️⃣ Rectangle Class with MANUALLY WRITTEN DOCUMENTATION
# -------------------------------------------------------------

class RectangleManual:
    """
    A simple rectangle class with methods to calculate area and perimeter.
    """

    def __init__(self, width, height):
        """
        Create a rectangle with a given width and height.
        """
        self.width = width   # store width
        self.height = height # store height

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


# -------------------------------------------------------------
# 3️⃣ COMPARISON OF AI DOCUMENTATION VS MANUAL DOCUMENTATION
# -------------------------------------------------------------

def compare_docs():
    print("\n=== AI-GENERATED CLASS DOCSTRING ===")
    print(RectangleAI.__doc__)

    print("\n=== MANUAL CLASS DOCSTRING ===")
    print(RectangleManual.__doc__)

    print("\n=== AI AREA DOCSTRING ===")
    print(RectangleAI.area.__doc__)

    print("\n=== MANUAL AREA DOCSTRING ===")
    print(RectangleManual.area.__doc__)

    print("\n=== AI PERIMETER DOCSTRING ===")
    print(RectangleAI.perimeter.__doc__)

    print("\n=== MANUAL PERIMETER DOCSTRING ===")
    print(RectangleManual.perimeter.__doc__)


# -------------------------------------------------------------
# 4️⃣ Example usage
# -------------------------------------------------------------
if __name__ == "__main__":
    r1 = RectangleAI(5, 3)
    r2 = RectangleManual(5, 3)

    print("AI Rectangle Area:", r1.area())
    print("Manual Rectangle Area:", r2.area())

    print("AI Rectangle Perimeter:", r1.perimeter())
    print("Manual Rectangle Perimeter:", r2.perimeter())

    # Compare Documentation
    compare_docs()
