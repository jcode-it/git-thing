

## What is Git?

Git is version control software. Git is local to your machine. Github is a remote place for a git repo to live.

## Basic Commands

'git init' - creates the .git folder. it initializes the git repository

to remove a initialized repo, we can run 'rm -rf .git' (or more safely, place the .git folder in the recycle bin)

'git add [filename] [filename] [...]' - stages files for the next commit

'git add.' - stages all the files in the current directory

'git commit -m "some message"' - makes the snapshot/saves the current state of the project

'git status' - tells us information such as the branch we are on, files that have been staged, files that have been modified since last commit and more.