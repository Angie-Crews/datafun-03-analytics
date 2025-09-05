# datafun-03-analytics
## Topic CC3.1 Start a Python Data Project

### 01 Create New Repository

### 02 Clone Repo to Local
```shell
git clone https://github.com/Angie-Crews/datafun-03-analytics
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
Run the following commands from the project root directory. The commands work in PowerShell.

```shell
.\.venv\Scripts\activate
py myfile.py
```
