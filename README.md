# Palindrome Checker With PyTest Testcases

This Python project is designed to find palindrome days in the format **DD-MM-YYYY** for a given year. A palindrome day is a day where the date is the same when read forward and backward. For example, 10-02-2001 is a palindrome day, as it reads the same backward.

## Problem Description

The task is to:
1. Take an input year (e.g., 2001).
2. Find all palindrome days (if any) in that year.
3. If no palindrome days exist in the given year, print "No Palindrome days available in the given year."

### Example
- **Input**: 2001
- **Output**: 10-02-2001

If no palindrome days are available in the given year, the program will output: "No Palindrome days available in the given year."

## Script Description

### `palindrome_days.py`

This script implements the following logic:
1. **Input Handling**: The user provides a year as input.
2. **Palindrome Calculation**: The script checks for each day in the given year to see if it forms a palindrome in the **DD-MM-YYYY** format.
3. **Output**: It prints all the palindrome days in the given year. If no palindrome day is found, it prints the message "No Palindrome days available in the given year."

## PyTest

The script is tested using **PyTest**, with at least 5 test cases to ensure the correctness of the logic.

### Example of PyTest usage:
```bash
$ pytest test_palindrome_days.py
