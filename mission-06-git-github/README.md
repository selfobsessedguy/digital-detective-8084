# Mission 06 - Git and GitHub

## 1. Task / objective

The objective of Mission 06 was to understand how version control works using Git, practice inspecting status, staging files, creating descriptive commits, branching out with an update-about branch, opening and understanding Pull Requests, and compiling a one-line glossary of core Git commands.

## 2. Work completed

I worked through the full Git workflow. I inspected the status of my repository, staged changes, and examined commit logs. I created a new branch called update-about, modified the root README.md to add a My Learning section, committed the changes on that branch, and merged them back into main. I documented the Pull Request process and wrote a complete Git glossary in my own words.

Here are the detailed explanations and activities:

### Task 6.1 - Understand the basic Git workflow

Git operations:

Operation 1: Check repository status
- Command: git status
- What it does in my own words: It asks Git what has changed in the project folder. It shows which files have been modified, which files are untracked (new), and which files are currently staged and ready to be committed.

Operation 2: Stage selected changes
- Command: git add filename
- What it does in my own words: It places a modified file into the staging area (also called the index). This tells Git, "Include this file's changes in the next snapshot."

Operation 3: Create a commit
- Command: git commit -m "commit message"
- What it does in my own words: It takes everything currently in the staging area and permanently records it as a new snapshot in the project history with a descriptive log message.

Operation 4: View commit history
- Command: git log
- What it does in my own words: It lists all the past commits that have been recorded in the repository, showing who made each commit, when it was made, the commit hash, and the message.

Difference between staging a change and committing it:
Staging a change (git add) is like putting selected items into a shipping box before taping it shut. You can pick and choose which files go in. Committing (git commit) is like sealing the box, stamping it with a date, time, and label, and storing it permanently in the archive. Staging is temporary preparation; committing is permanent history.

### Task 6.2 - Create and use a branch

- Branch name created: update-about
- Command used: git checkout -b update-about
- Root README modification: Added a new section titled "My Learning" describing three key things learned so far (terminal navigation, OS responsibilities, and binary data encoding).
- Staged and committed on branch update-about with the message: Add My Learning section to root README on branch update-about

### Task 6.3 - Create a Pull Request

Understanding branches and Pull Requests:
- What is a branch: A branch is an independent, parallel workspace that branches off from the main project code. It allows you to build a new feature, test an idea, or fix a bug without risking breaking the working main code. If something goes wrong on the branch, the main branch remains completely safe.
- What is a Pull Request (PR): A Pull Request is a collaborative review process hosted on GitHub. It notifies project teammates or the instructor that work on a separate branch is ready to be reviewed. Teammates can see the exact line-by-line diff, comment on code, request changes, and safely merge the branch into main once approved.
- Why they are useful in teamwork: When multiple developers work on the same project at the same time, working on separate branches prevents people from accidentally overwriting each other's files. Pull Requests ensure that no code enters the main project without another set of eyes checking it first.
- Branch merge status: The update-about branch was merged into the main branch locally using git merge update-about. Both main and update-about branches remain in the repository so they can be pushed to GitHub.

### Task 6.4 - Build your Git command glossary

One-line explanations in my own words:
- Initialise a repository: git init sets up a new hidden .git directory so Git can begin tracking files in the folder.
- Check status: git status shows what has changed in the working folder and what is staged for the next commit.
- Stage changes: git add prepares selected file modifications to be saved in the next commit.
- Commit changes: git commit saves a permanent snapshot of staged changes into project history with a message.
- View history: git log displays the chronological list of all previous commits made to the repository.
- Create or list branches: git branch shows existing branches in the project or creates a new branch name.
- Switch branches: git checkout or git switch changes your active working branch to another branch.
- Publish changes: git push uploads your local commits and branches up to an online remote server like GitHub.
- Retrieve remote changes: git pull downloads the newest updates from GitHub and merges them into your local branch.

## 3. Commands / tools used

- git status: inspected working tree status.
- git add: staged changes to README.md.
- git commit: recorded commits to branch history.
- git log --oneline: reviewed concise commit history.
- git checkout -b update-about: created and switched to the update-about branch.
- git checkout main: switched back to the main branch.
- git merge update-about: merged changes from the feature branch into main.
- git branch: listed all branches.

## 4. My understanding

Before this mission, I thought Git and GitHub were the exact same thing. Now I understand that Git is the local software tool on my computer that tracks file changes, while GitHub is a website that stores Git repositories online and provides tools like Pull Requests for people to collaborate.

Learning about branches made me realize how modern software teams avoid breaking production websites. You make changes on a branch, open a PR for review, and only merge when everything passes.

## 5. Difficulties faced

At first, I was confused about how a branch knows where to start from and whether switching branches would delete my files.

## 6. How I resolved them

I noticed that switching branches with git checkout simply updates the files in the folder to match whatever commit that branch is pointing to. As long as changes are committed before switching, nothing gets lost.

## 7. Evidence / files

- Root documentation updated: README.md
- Mission documentation: mission-06-git-github/README.md
- Branches verified: main and update-about

## 8. Commit details

Commit message: Complete Git and GitHub collaboration mission
Status: Committed to local git repository on branch main.
