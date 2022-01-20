Project 0 - Git-Guide
CEG 3120

COMMAND LINE
status
    Shows status of the local repository including the number of local commits not yet synced with remote, a list of files in the local folder not tracked by git, and a list of files in the local folder that have changed needing a commit
    EX: git status

clone
    Creates an clone of the entirety of a repo. If anything happens to the original repo, this clone can be used to restore it
    EX: git clone https://github.com/helloworld

add
    begins tracking for a specified file
    EX: git add helloworld.txt

rm
    removes the file from tracking AND from the repository, --cache removes the files from tracking)
    EX: git rm --cache helloworld

commit
    commits changes to the repo. NOTE: only changes to files that have been tracked will be committed, anything else will stay local
    EX: git commit

commit --amend
    in case a commit is made too early, restage whatever change files are needed and use this command
    EX: commit --amend

push
    pushes your commits to the server repo. If anyone pushed since your last fetch, you will have to fetch before pushing.
    EX: git push <remote> <branch>

fetch
    Downloads any new data to the repository from the server to your local machine. However, it does not merge the data with what you have locally
    EX: git fetch helloworld

merge
    Takes the work you did in a branch and merges it with the master branch.
    EX: git merge nothelloworldbranch

pull
    The opposite of a push. Updates the local repo from the remote
    EX: git pull acreativelynamedrepo

branch
    A branch is a pointer to a commit. Simply put, its an alternative to your clean master that is being used. If testing new features, you would create a branch to test them.
    EX: git branch testworld

checkout
    views the versions of files that a particular tag is pointing to. Any changes are unreachable without creating a branch
    EX: git checkout <tagname>

init
    Creates a subdirectory that contains all the necessary repo files
    EX: git init

remote
    shows the shortname of each remote handle you've specified
    EX: git remote
    Use -v to show the url's as well
    EX: git remote -v

GIT FILES & FOLDERS
.git folder
    contains everything the project needs. Commits, remote address, logs that have commit history etc.

.gitignore file
    Used to tell git to ignore files with certain characters in their names
    EX: cat .gitignore
        *.[ld]
    (ignores all files ending with 'ld')

.git/hooks
    {fill in later}

GITHUB
pull requests
    Allows you to tell other users about the changes you push to a branch

SSH authentication to repositories 
    Allows you to actually connect to the repo so you can write and edit or even clone and download the entire thing. There are private and public keys.
    EX: Folders associated: .ssh 

actions
    {fill in later}