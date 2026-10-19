## Week 3: Virtual Environments and .zshrc
`python3 -m venv .venv` - Creates a virtual environment called `.venv`.
`source .venv/bin/activate` - Activates the virtual environment.
`which python3` - Shows which Python is being used.
`pip list` - Shows the packages installed in the environment.
`pip install pytest ruff` - Installs pytest and ruff.
`pip freeze > requirements.txt` - Saves the installed packages to a requirements file.
`cat requirements.txt` - Shows what is in the requirements file.
`deactivate` - Leaves the virtual environment.
`pip install -r requirements.txt` - Installs the packages from the requirements file.
`echo '.venv/' > .gitignore` - Adds the virtual environment to `.gitignore`.
`echo '__pycache__/' >> .gitignore` - Adds Python cache files to `.gitignore`.
`cat .gitignore` - Shows what is inside the `.gitignore` file.
`code ~/.zshrc` - Opens the `.zshrc` file in VS Code.
`source ~/.zshrc` - Reloads the `.zshrc` file so the changes take effect.
`alias ll='ls -la'` - Lists files with more details, including hidden files.
`alias c='clear'` - Clears the terminal screen.
`alias py='python3'` - Lets you use `py` instead of `python3`.
`alias gs='git status'` - Shows the current Git status.
`alias ga='git add .'` - Adds all changes to Git.
`alias gcmsg='git commit -m'` - Creates a Git commit with a message.
`alias gp='git push'` - Pushes changes to the remote repository.
`alias gl='git log --oneline'` - Shows the Git history in a shorter format.
`alias tree2='tree -L 2'` - Shows the folder structure up to two levels.
`mkcd() { mkdir -p "$1" && cd "$1"; }` - Creates a folder and moves into it.# ism3232-module02
