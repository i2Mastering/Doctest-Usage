# Rectangle Area Calculator

## Description
This Python program calculates the area of a rectangle and includes built-in tests using the `doctest` module. It demonstrates basic function definitions, argument handling, and automated testing for correctness.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Function](#function)
- [Requirements](#requirements)
- [License](#license)

## Features
- Computes the area of a rectangle given length and width.
- Uses the `doctest` module to verify function correctness.
- Supports both integer and floating-point inputs.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/rectangle-area-calculator.git
   ```
2. Navigate to the project directory:
   ```sh
   cd rectangle-area-calculator
   ```
3. Ensure Python 3.x is installed.

## Usage
1. Run the script:
   ```sh
   python rectangle_area.py
   ```
2. The program will compute the area based on sample inputs and run automated tests.

## Example
```sh
Computed area: 70.0
```

## Function
### `areaOfARectangle(l, w)`
- Computes the area of a rectangle.
- **Arguments:**
  - `l (float or int)`: Length of the rectangle.
  - `w (float or int)`: Width of the rectangle.
- **Returns:**
  - `float`: The computed area of the rectangle.

#### Example Usage
```python
>>> areaOfARectangle(5.0, 10.0)
50.0
>>> areaOfARectangle(7, 10)
70.0
```

## Requirements
- Python 3.x

## License
This project is licensed under the MIT License.
