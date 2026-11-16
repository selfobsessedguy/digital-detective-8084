# Mission 02 - Terminal

## 1. Task / objective

The objective of Mission 02 was to learn and practice essential terminal commands for inspecting directories, managing files and folders safely, understanding how command line flags and pipe operators work, and exploring package managers such as Homebrew on macOS.

## 2. Work completed

I practiced all required terminal commands inside a dedicated practice folder called terminal-practice to avoid touching any important files. I executed nine core file operations, created and edited text using redirection operators, compared simple listings with detailed flag-based listings, piped output into a filter, and checked Homebrew package manager details.

Here is the breakdown of the operations and findings:

### Task 2.1 - Explore basic Terminal operations

Operation 1: Current-directory display
- Command: pwd
- What it does: Prints the working directory, showing the complete path from root to where the terminal is currently sitting.
- What I observed: It printed /Users/[redacted]/.../digital-detective-8084/terminal-practice, so I knew my exact location.

Operation 2: Directory listing
- Command: ls
- What it does: Shows the names of files and folders in the current folder.
- What I observed: It printed the names of the files in my practice folder in simple clean columns.

Operation 3: Detailed listing
- Command: ls -la
- What it does: Displays a long list format including hidden files starting with dot, permissions, owner, file size, and modification date.
- What I observed: I could see dot folders (. and ..), permission strings like drwxr-xr-x, and the exact byte count of each file.

Operation 4: Change directory
- Command: cd ..
- What it does: Moves the terminal session up one level to the parent directory.
- What I observed: Running pwd after cd .. showed that I went up from terminal-practice to the digital-detective-8084 root folder.

Operation 5: Create directory
- Command: mkdir terminal-practice
- What it does: Makes a new directory (folder) with the specified name.
- What I observed: The folder was created immediately without any error output.

Operation 6: Create empty file
- Command: touch practice.txt
- What it does: Creates a new empty file if it does not exist, or updates its timestamp if it does.
- What I observed: A new zero-byte file called practice.txt appeared in the directory listing.

Operation 7: Copy file
- Command: cp practice.txt practice-backup.txt
- What it does: Makes an exact duplicate copy of a file with a new destination name.
- What I observed: Both the original practice.txt and the new practice-backup.txt were present in the directory.

Operation 8: Move / rename file
- Command: mv practice-backup.txt practice-renamed.txt
- What it does: Renames a file or moves it to another directory path.
- What I observed: The practice-backup.txt file disappeared and its content now existed under the name practice-renamed.txt.

Operation 9: Display file contents
- Command: cat practice.txt
- What it does: Reads and prints the entire text content of a file straight to the terminal screen.
- What I observed: The lines of text I typed into the file appeared directly in the terminal output.

### Task 2.2 - Practise file changes safely

I worked exclusively inside the terminal-practice folder.
I used the command echo "First line of practice notes." > practice.txt to write one line.
Then I used echo "Second line of practice notes added." >> practice.txt to add a second line without erasing the first.
I ran cat practice.txt, which confirmed that both lines were present.
Then I copied the file to practice-backup.txt and renamed it to practice-renamed.txt.

Answers to questions:
- Difference between replacing a file's contents and adding text to the end: The single greater-than sign (>) completely overwrites and replaces any existing content in the target file. The double greater-than sign (>>) appends the new text to the very end of the file, preserving everything that was already written.
- Difference between copying a file and moving a file: Copying makes a second independent clone of the file, leaving the original in place. Moving relocates the file or changes its name, so the original file at the old location is gone.
- What information does the current-directory display provide: The pwd command shows the full absolute path from the computer root folder (/) down to your current directory. This prevents accidental mistakes when deleting or editing files.
- Why is a directory-listing operation useful: The ls command allows you to confirm whether a file or folder actually exists, check exact spellings, and ensure files were created in the right folder.

### Task 2.3 - Understand flags and pipes

Flags comparison:
Running plain ls only printed file names.
Running ls -lha changed the behavior significantly:
- The -l flag gave long format with permissions, owner, size, and date.
- The -h flag changed file sizes into human-readable units like K for kilobytes or M for megabytes instead of raw byte counts.
- The -a flag revealed hidden dot files like . and .. which normal ls hides.

Pipes:
Command executed: ls -la | head -n 5
- What the pipe symbol (|) does: It takes the standard output from the command on the left and connects it directly as the standard input into the command on the right.
- Left side contribution: ls -la generates the full detailed list of all files in the directory.
- Right side contribution: head -n 5 reads that stream and displays only the first five lines, cutting off the rest of the output. This is very useful when a folder has hundreds of files.

### Task 2.4 - Understand package managers

I checked Homebrew on macOS:
- Version check command: brew --version
- Result: Homebrew 7.0.9
- Managed packages check command: brew list
- Result: Packages like git, ffmpeg, openssl, and ca-certificates are managed by Homebrew.

Why package managers are useful:
A package manager is useful because it automates downloading, installing, updating, and removing software tools from the command line. Instead of searching the web for installers, unzipping folders, and fixing missing dependencies manually, a single command like brew install tool-name sets up the program and all needed helper libraries cleanly.

## 3. Commands / tools used

- pwd: print working directory
- ls, ls -la, ls -lha: list directory contents with different detail flags
- cd, cd ..: change directory and navigate to parent directory
- mkdir: create directories
- touch: create new empty files
- cp: copy files
- mv: move or rename files
- cat: display file contents
- echo with > and >>: write and append text lines to a file
- | (pipe) and head -n 5: chain command outputs and limit displayed lines
- brew: Homebrew package manager to check version and list installed packages

## 4. My understanding

Working in the terminal felt intimidating at the start because there are no buttons or icons to click. But after doing these exercises, I understand that the terminal is just a direct way to tell the computer what to do using text commands.

Flags give commands superpowers by turning on extra options, like making numbers readable with -h. Pipes are especially cool because you can connect simple tools together like Lego bricks to do complex things.

## 5. Difficulties faced

At the beginning, I was nervous about whether using > would delete my whole file. I also got slightly confused about relative path navigation with cd .. versus cd folder-name.

## 6. How I resolved them

I practiced only inside terminal-practice so that if I made a mistake, nothing important would be affected. Testing both > and >> on a practice file showed me clearly that >> keeps previous lines while > replaces them.

## 7. Evidence / files

- Practice folder: terminal-practice/
- Practice file: terminal-practice/practice.txt
- Renamed practice file: terminal-practice/practice-renamed.txt
- Mission documentation: mission-02-terminal/README.md

## 8. Commit details

Commit message: Complete Terminal and file management mission
Status: Committed to local git repository on branch main.
