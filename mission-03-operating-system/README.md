# Mission 03 - Operating system

## 1. Task / objective

The objective of Mission 03 was to explore the operating system environment, check active user identity and disk storage capacity, understand how processes run and what a process identifier (PID) means, compare absolute and relative paths, examine file permissions, and explain the core responsibilities of an operating system.

## 2. Work completed

I ran commands to inspect my operating system build, current user session, and disk space usage. I studied running processes and what information the process table displays. I tested navigating between directories using both relative and absolute paths, examined the permission strings of practice files, and wrote simple explanations for the six major operating system duties.

Here are the findings and observations:

### Task 3.1 - Explore your operating system

Item 1: Operating system / system details
- What it tells you: The exact name, kernel version, and architecture of the operating system managing the computer.
- Privacy-safe observation: Running sw_vers and uname -srm showed that the system is running macOS version 27.2.1 on Darwin kernel arm64 architecture.

Item 2: Current account identity
- What it tells you: The active username that owns the current terminal session.
- Privacy-safe observation: Running whoami showed [redacted], confirming that the terminal is running under a regular standard user account rather than root.

Item 3: Available and used storage
- What it tells you: How much total disk space exists, how much is currently filled with files, and how much free space remains.
- Privacy-safe observation: Running df -h showed the main disk volume has a total capacity of approximately 926 GiB, with around 13 GiB used and over 820 GiB available.

Item 4: System activity snapshot
- What it tells you: A live overview of running tasks, active programs, CPU load, and memory consumption.
- Privacy-safe observation: System activity indicated smooth operation with high idle CPU capacity and normal background service operation.

### Task 3.2 - Understand processes

Answers to process questions:
- What is a process: A process is a program that is actively running in computer memory. When a program is stored on disk it is just a passive file, but once opened and loaded into RAM by the OS, it becomes an active process with allocated resources.
- What does the PID column represent: PID stands for Process Identifier. It is a unique positive number assigned by the operating system kernel to identify and keep track of every individual running process. For example, the very first system process on macOS has PID 1.
- Two examples of processes running on my computer:
  1. The terminal shell process (such as zsh or bash) that takes commands typed from the keyboard.
  2. The Python runtime process (python3) when executing a python script. Other examples include background services like launchd or web browser processes.

### Task 3.3 - Understand paths and permissions

Path navigation:
- Absolute path: An absolute path is the complete full address of a file or folder starting from the very top root directory (/). It always starts with a forward slash. Example from this project: /Users/[redacted]/.../digital-detective-8084/mission-03-operating-system.
- Relative path: A relative path describes where a file or folder is located in relation to where the terminal is currently working. It does not start with a leading root slash. Example: ./mission-03-operating-system/README.md or ../terminal-practice/practice.txt.

Permissions examination:
I checked the detailed listing of terminal-practice/practice.txt using ls -l:
- Output observed: -rw-r--r--
- Meaning of permission letters:
  r stands for read: allows the contents of the file to be opened and viewed.
  w stands for write: allows the file to be edited, modified, or saved.
  x stands for execute: allows a file or script to be executed as a program, or allows entering a directory.
- Owner permissions: The first three letters after the dash are rw-, which means the owner has read and write permission, but not execute permission.
- Group and others: The next triplets are r-- and r--, meaning anyone else can only read the file and cannot modify it.

### Task 3.4 - Explain operating-system responsibilities

1. Process management
- Explanation: The OS creates, schedules, pauses, and terminates running programs so the CPU can run multiple tasks without them freezing or crashing into each other.
- Example: Letting you listen to music in the background while typing an assignment in a text editor.

2. Memory management
- Explanation: The OS decides which program gets which section of RAM, tracks what parts of memory are currently in use, and frees up RAM when a program is closed.
- Example: Allocating 200 MB of RAM when opening a web browser and reclaiming that RAM when the browser is closed.

3. Device management
- Explanation: The OS talks to input and output hardware components through device drivers so programs can use them without knowing hardware details.
- Example: Receiving keypresses from a USB keyboard and sending document data to an external printer.

4. File management
- Explanation: The OS organizes files and folders on physical drives, controls how files are created, renamed, read, or deleted, and prevents unauthorized changes.
- Example: Saving a college assignment inside a specific folder on the SSD.

5. User interface / shell
- Explanation: The OS provides a visual desktop GUI or a text-based command line shell so users can easily interact with the computer.
- Example: Opening a terminal window to type commands or using Finder/Desktop to double click icons.

6. Security and permissions
- Explanation: The OS enforces user accounts and file access permissions to protect private files from being altered or seen by unauthorized users or malicious programs.
- Example: Requiring an administrator password before installing system-wide software or stopping a normal user from editing core system files.

## 3. Commands / tools used

- uname -srm: inspected kernel name, release, and machine hardware architecture.
- sw_vers: checked macOS product name and build version.
- whoami: verified current logged-in user account.
- df -h: checked mounted filesystem storage space in human readable gigabytes.
- ls -l: examined detailed file permission strings and ownership.

## 4. My understanding

I learned that an operating system is like the manager of an entire company. It sits directly between the computer hardware and user applications. Without an OS, every program would have to directly control circuits, screen pixels, and memory chips, which would be impossible.

Understanding file permissions also helped me realize why some files can only be read while others can be edited or executed, which keeps the system secure.

## 5. Difficulties faced

Reading the permission string -rw-r--r-- was confusing at first because it looked like random letters and dashes.

## 6. How I resolved them

I broke the string into parts: the first dash means regular file, the next three letters rw- are for the owner (read and write), the next three r-- are for the group (read only), and the last three r-- are for everyone else. Breaking it into triplets made it very clear.

## 7. Evidence / files

- Mission documentation: mission-03-operating-system/README.md
- System commands tested: uname, sw_vers, whoami, df -h, ls -l

## 8. Commit details

Commit message: Document operating system and file management
Status: Committed to local git repository on branch main.
