# datafun-03-analytics
## Topic CC3.1 Start a Python Data Project

### 01 Create New Repository

### 02 Clone Repo to Local
```shell
git clone https://github.com/Angie-Crews/datafun-02-automation
```

### 03 Create .gitignore and requirements.txt and copy contents of each
Task 1:  Create new .gitignore file in repo and copy contents from https://github.com/denisecase/pro-analytics-01/

Task 2:  Create new requirements.txt file in repo and copy contents from https://github.com/denisecase/pro-analytics-01/

```shell
git add .
git commit -m "Add .gitignore"
git push -u origin main
```

```shell
git add .
git commit -m "Add requirements.txt"
git push -u origin main
```
To Update information from GitHub to VS Code

```shell
git pull
```
### 04 Git Add Commit Push

```shell
git add .
git commit -m "Add your own message log of what is being pushed"
git push -u origin main
```
After changes, you can use the simpler version of the last command
```shell
git push
```

### 05 Git Pull Before Changes
Before making any changes to a project, ALWAYS pull the latest changes from the remote repository on GitHub. Keep both locations up-to-date and in sync.

Pull Changes
```shell
git pull origin main
```
### 06 Create Virtual Environment
In VS Code, right click on the project folder, choose open in integrated terminal

To Create Virtual Environment

```shell
py -m venv .venv
```
To activate a virtual environment

```shell
.\.venv\Scripts\Activate
```
To deactivate a virtual environment

```shell
deactivate
```

### 07 Install Dependencies
.venv is active, update key packages, install dependencies from requirements.txt file
Run the following commands from the project root directory. The commands work in PowerShell.

```shell
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install -r requirements.txt
```

### 08 Activate and Run Python Script
Before Starting, Open your project repository folder in VS Code, Open a terminal, activate the virtual environment (.venv)
If external dependencies have not been installed, install them.

Task 1. Select VS Code Interpreter
VS Code needs our populated .venv to interpret our files correctly.

To set the VS Code Interpreter:

Open the Command Palette: Press Ctrl+Shift+P (Windows/Linux)
Search for "Python: Select Interpreter":
Type Python: Select Interpreter in the Command Palette search bar and select it from the dropdown.
Choose an Interpreter - A list of available Python environments will appear. Look for the recommended local .venv option.
Check the Python version shown in the lower-left status bar.
Making Changes / Saving
Now we can get help from the VS Code editor while working on the Python code files.

After making changes, run the file to verify following the steps below. Save your files periodically to avoid losing progress - or ensure VS Code File / Autosave option is on.

Windows Task 2: Activate and Execute
Ensure .venv is active. If active, you don't need to rerun the activate command.
Run the file.
IMPORTANT: Change the name of the file to your actual file. The file must exist in the root project folder for the execute command to work.

Run the following commands from the project root directory. The commands work in PowerShell.

```shell
.\.venv\Scripts\activate
py myfile.py
```
