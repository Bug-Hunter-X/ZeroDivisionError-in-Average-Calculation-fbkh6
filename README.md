# Python Bug: ZeroDivisionError in Average Calculation

This repository demonstrates a common Python bug: a `ZeroDivisionError` that can occur when calculating the average of an empty list. The `bug.py` file contains the buggy code, while `bugSolution.py` provides the corrected version.

## Bug Description
The original code attempts to calculate the average of a list of numbers. However, if the list is empty, it will result in a `ZeroDivisionError` because it attempts to divide by zero. 

## Solution
The solution adds a check to see if the input list is empty. If it is, the function returns 0, preventing the error.