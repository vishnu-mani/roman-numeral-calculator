# Roman Numeral Calculator

The Roman numeral calculator is a python script for addition, subtraction, multiplication, and division of Roman Numerals.

## Execution

For executing Roman Numeral Calculator

```bash
python3 roman_numeral_calculator.py
```

## Unit Test

For testing the code with unit test cases

```bash
python3 -m unittest test_roman_numeral_calculator
```

## Code Coverage

The amount lines/blocks of your code are executed while the automated tests are running.

#### Installation

```bash
pip3 install coverage
```

For running code coverage for unit tests

```bash
coverage run -m unittest test_roman_numeral_calculator
```

For getting the code coverage report

```bash
coverage report -m
```

Output:

```bash
Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
roman_numeral_calculator.py           53      8    85%   81-89
test_roman_numeral_calculator.py      21      0   100%
----------------------------------------------------------------
TOTAL                                 74      8    89%
```
