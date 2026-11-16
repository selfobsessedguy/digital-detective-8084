# Mission 04 - Programs

## 1. Task / objective

The objective of Mission 04 was to write and run my very first Python script from the terminal, understand how computers turn source code into running actions, and compare how compiled languages differ from interpreted languages.

## 2. Work completed

I created a Python file called hello.py inside the mission-04-programs directory. I added code to print the exact message required, saved the file, and executed it from terminal using Python 3. The message printed successfully on my screen. I also researched and wrote a detailed comparison between compilers and interpreters.

Here is the comparison and explanation:

### Task 4.1 - Create and run a Python program

- Program file created: hello.py
- Source code written:
print("Hello from Python")
- Command used to run: python3 hello.py
- Observed terminal output:
Hello from Python

### Task 4.2 - Compare compiler and interpreter

Comparison points:

Point 1: When translation / execution happens
- Compiler: Translates the whole source code file all at once into machine code before the program is executed.
- Interpreter: Translates and carries out code line by line at runtime while the program is actually running.

Point 2: Typical output
- Compiler: Produces a separate standalone executable file (like a binary or .exe) that can run directly on the operating system.
- Interpreter: Does not produce a separate permanent executable file; it executes instructions directly in memory.

Point 3: One example
- Compiler: C, C++, or Go.
- Interpreter: Python or JavaScript.

Point 4: One advantage
- Compiler: The final program runs faster and uses less CPU during execution because translation is already done ahead of time.
- Interpreter: Much easier for beginners to write and test quickly because you can run your code immediately without an extra build step, and error messages tell you the exact line that failed.

Summary in my own words:
A compiler translates an entire program from human readable code into computer machine code before anything runs, creating a fast standalone executable. An interpreter translates and runs the code line by line on the fly. Because Python is interpreted, I could write one line in hello.py and run it instantly with python3 without needing to compile it first.

## 3. Commands / tools used

- Text editor: used to create and save hello.py.
- python3 hello.py: ran the Python 3 interpreter on the script file.
- terminal: used to navigate to the mission folder and run the command.

## 4. My understanding

I learned that computers cannot understand English words like print directly. The computer CPU only understands binary machine instructions.

A translator is always needed. A compiler translates the whole book before you read it, while an interpreter translates sentence by sentence as you go. For someone learning programming like me, an interpreter is very friendly because you get instant feedback.

## 5. Difficulties faced

When I ran python instead of python3 at first, I wondered if there was a difference between them on macOS.

## 6. How I resolved them

I learned that modern systems use python3 for Python version 3. Typing python3 hello.py made the script run without any warning or confusion.

## 7. Evidence / files

- Python script: mission-04-programs/hello.py
- Mission documentation: mission-04-programs/README.md

## 8. Commit details

Commit message: Compare compilers and interpreters
Status: Committed to local git repository on branch main.
