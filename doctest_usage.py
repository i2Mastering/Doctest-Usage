"""
Module for calculating the area of a rectangle and testing its correctness using doctest.

This script defines a function to compute the area of a rectangle and includes
built-in tests to verify the function’s correctness using the `doctest` module.

Functions:
    - areaOfARectangle(l, w): Computes and returns the area of a rectangle.

Example Usage:
    ```python
    >>> areaOfARectangle(5.0, 10.0)
    50.0
    >>> areaOfARectangle(7, 10)
    70.0
    ```

Author: Ike Iloegbu
License: MIT
"""

import doctest

def areaOfARectangle(l, w):
    """
    Compute and return the area of a rectangle.
    
    Args:
        l (float or int): The length of the rectangle.
        w (float or int): The width of the rectangle.
    
    Returns:
        float: The computed area of the rectangle.
    
    Example:
    >>> areaOfARectangle(5.0, 10.0)
    50.0
    >>> areaOfARectangle(5, 10)
    50.0
    """
    return float(l * w)

if __name__ == "__main__":
    doctest.testmod(verbose=True)
    
    # Sample input test
    test1 = areaOfARectangle(7, 10)
    print(f"Computed area: {test1}")


