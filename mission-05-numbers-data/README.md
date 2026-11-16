# Mission 05 - Numbers and data

## 1. Task / objective

The objective of Mission 05 was to learn how data is represented inside a computer. This included calculating binary, decimal, and hexadecimal conversions by hand, verifying each calculation using Python functions, writing a Python program (number_converter.py) to convert numbers automatically, and understanding how text is encoded using ASCII and UTF-8.

## 2. Work completed

I solved all seven number conversion problems step by step on paper, showing the full division or positional multiplication for each one. I then tested each calculation inside Python using functions like bin, hex, and int. Next, I wrote number_converter.py, ran it from the terminal, and tested it with three different inputs. Finally, I researched ASCII codes and why computers need text encoding standards.

Here is the detailed work:

### Task 5.1 - Convert numbers by hand

Question 1: Convert decimal 13 to binary
- Working:
  13 divided by 2 = 6, remainder 1
  6 divided by 2 = 3, remainder 0
  3 divided by 2 = 1, remainder 1
  1 divided by 2 = 0, remainder 1
  Reading the remainders from the last division to the first (bottom to top): 1101.
- Answer: 1101 (in binary)

Question 2: Convert decimal 25 to binary
- Working:
  25 divided by 2 = 12, remainder 1
  12 divided by 2 = 6, remainder 0
  6 divided by 2 = 3, remainder 0
  3 divided by 2 = 1, remainder 1
  1 divided by 2 = 0, remainder 1
  Reading the remainders from bottom to top: 11001.
- Answer: 11001 (in binary)

Question 3: Convert binary 1010 to decimal
- Working:
  Bit 3 (value 2^3 = 8): 1 * 8 = 8
  Bit 2 (value 2^2 = 4): 0 * 4 = 0
  Bit 1 (value 2^1 = 2): 1 * 2 = 2
  Bit 0 (value 2^0 = 1): 0 * 1 = 0
  Adding them up: 8 + 0 + 2 + 0 = 10.
- Answer: 10 (in decimal)

Question 4: Convert binary 1101 to decimal
- Working:
  Bit 3 (value 2^3 = 8): 1 * 8 = 8
  Bit 2 (value 2^2 = 4): 1 * 4 = 4
  Bit 1 (value 2^1 = 2): 0 * 2 = 0
  Bit 0 (value 2^0 = 1): 1 * 1 = 1
  Adding them up: 8 + 4 + 0 + 1 = 13.
- Answer: 13 (in decimal)

Question 5: Convert hexadecimal A to decimal
- Working:
  In hexadecimal, digits go from 0 to 9, then A=10, B=11, C=12, D=13, E=14, F=15.
  Digit A is at position 0 (value 16^0 = 1).
  Calculation: 10 * 1 = 10.
- Answer: 10 (in decimal)

Question 6: Convert hexadecimal 1F to decimal
- Working:
  Digit 1 is at position 1 (value 16^1 = 16): 1 * 16 = 16
  Digit F is at position 0 (value 16^0 = 1, where F = 15): 15 * 1 = 15
  Adding them up: 16 + 15 = 31.
- Answer: 31 (in decimal)

Question 7: Convert binary 1111 to hexadecimal
- Working:
  First convert binary 1111 to decimal:
  (1 * 8) + (1 * 4) + (1 * 2) + (1 * 1) = 8 + 4 + 2 + 1 = 15.
  In hexadecimal, decimal 15 is represented by the single letter F.
- Answer: F (or 0xF)

### Task 5.2 - Verify using Python

Check 1: Decimal to binary
- Expression tested: bin(13)
- Result: '0b1101'
- Matches manual calculation: Yes (the 0b prefix tells Python it is binary).

Check 2: Decimal to binary
- Expression tested: bin(25)
- Result: '0b11001'
- Matches manual calculation: Yes.

Check 3: Binary to decimal
- Expression tested: int('1010', 2)
- Result: 10
- Matches manual calculation: Yes.

Check 4: Binary to decimal
- Expression tested: int('1101', 2)
- Result: 13
- Matches manual calculation: Yes.

Check 5: Hexadecimal to decimal
- Expression tested: int('A', 16)
- Result: 10
- Matches manual calculation: Yes.

Check 6: Hexadecimal to decimal
- Expression tested: int('1F', 16)
- Result: 31
- Matches manual calculation: Yes.

Check 7: Binary to hexadecimal
- Expression tested: hex(0b1111)
- Result: '0xf'
- Matches manual calculation: Yes (the 0x prefix indicates hexadecimal).

### Task 5.3 - Build a small number converter

I wrote number_converter.py which asks the user to enter a decimal number, converts it to an integer, and displays both its binary and hexadecimal values.

Terminal test runs:

Test 1:
- Input number: 13
- Binary output: 0b1101
- Hexadecimal output: 0xd

Test 2:
- Input number: 25
- Binary output: 0b11001
- Hexadecimal output: 0x19

Test 3:
- Input number: 42
- Binary output: 0b101010
- Hexadecimal output: 0x2a

Explanation of functions:
- bin(): This built-in Python function converts an integer number into a binary string representation with the prefix 0b.
- hex(): This built-in Python function converts an integer number into a hexadecimal string representation with the prefix 0x.

### Task 5.4 - How is text stored?

- ASCII decimal codes:
  Uppercase letter A: 65 (can be checked in Python with ord('A'))
  Lowercase letter a: 97 (can be checked in Python with ord('a'))

- Why a computer needs an encoding standard:
  Computers cannot store physical letters or alphabets directly because circuits and memory chips can only store binary numbers (0s and 1s). An encoding standard creates an agreed system so every computer knows which number code stands for which letter, allowing text to be written, saved, and read accurately anywhere.

- Character not in basic ASCII:
  The Indian Rupee symbol (₹), the Euro sign (€), or an emoji like the smiling face 😊 are not part of basic ASCII. Basic ASCII only has 128 characters (0 to 127) for standard English letters and symbols, so modern computers use UTF-8 to represent thousands of symbols and international languages.

## 3. Commands / tools used

- Python 3 interactive shell: used to test built-in conversion functions bin, hex, and int with base parameters.
- Text editor: used to write number_converter.py.
- python3 number_converter.py: executed the converter program in terminal.

## 4. My understanding

I now understand why binary is so fundamental to computers. Because electrical circuits have two states (on or off / high voltage or low voltage), base 2 is the most natural way for hardware to work.

Hexadecimal is like a convenient shorthand for binary. Instead of writing long strings of ones and zeros, four binary bits can be neatly represented by a single hexadecimal digit (from 0 to F).

## 5. Difficulties faced

At the beginning, when dividing by 2 to get binary, I was not sure whether to read the remainders from top to bottom or bottom to top.

## 6. How I resolved them

I realized that the first division gives the least significant bit (the 1s place) and the final division gives the most significant bit. Therefore, reading the remainders from bottom to top gives the correct binary number. I confirmed this by checking my results with bin() in Python.

## 7. Evidence / files

- Python script: mission-05-numbers-data/number_converter.py
- Mission documentation: mission-05-numbers-data/README.md

## 8. Commit details

Commit message: Build number converter and practise data representation
Status: Committed to local git repository on branch main.
