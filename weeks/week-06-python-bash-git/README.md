# Python + Bash + Git

This week focused on moving from Python fundamentals to practical scripting, command-line tools, Bash automation, and Git workflow.

The practical work focused on small cybersecurity-related scripts and using Git to manage the projects.

---

## Topics Studied

### Python

* `pathlib`
* Files
* `try`
* `except`
* `finally`
* `json`
* `re`
* Command line arguments
* `logging`
* `subprocess`
* `ipaddress`
* `socket`

### Bash

* Variables
* `$?`
* `if`
* `for`
* `while`
* Functions
* Arguments

### Git

```text
git init
git clone
git status
git add
git commit
git push
git pull
git branch
git merge
```

---

## Python

### Files

Studied working with files using Python.

Focused on:

* Reading files
* Writing files
* Handling file paths
* Using `pathlib`

---

### Exceptions

Studied exception handling with:

```python
try
except
finally
```

Practiced handling errors such as:

```text
FileNotFoundError
```

---

### JSON

Studied reading and writing structured data using the `json` module.

Practiced:

```python
json.load()
json.dump()
```

---

### Regular Expressions

Studied the `re` module and basic regex patterns.

Used regex to search for specific information inside test log files.

---

### Command Line Arguments

Studied how Python scripts receive arguments from the terminal.

The goal was to make scripts usable directly from the command line instead of relying only on hardcoded values.

---

### System and Network Modules

Studied:

```python
logging
subprocess
ipaddress
socket
```

Focused on understanding how Python can interact with the operating system and work with network-related data.

---

## Practical Python Project

### Python CLI Log Analyzer

Created a Python CLI for analyzing a test log file.

The project combines several concepts studied during the week:

```text
Files
   ↓
Exceptions
   ↓
JSON
   ↓
Regex
   ↓
Command Line Arguments
   ↓
Logging
   ↓
Python CLI
```

The project is intentionally kept small and focused on practical log analysis.

---

## Bash

Studied Bash scripting fundamentals.

### Variables

Learned how to create and use variables in Bash scripts.

---

### Exit Status

Studied:

```bash
$?
```

Used it to check the exit status of commands.

---

### Conditions

Studied:

```bash
if
```

Used conditions to control script behavior.

---

### Loops

Studied:

```bash
for
while
```

Used loops to repeat operations inside scripts.

---

### Functions

Studied how to create Bash functions and reuse code.

---

### Arguments

Studied how Bash scripts receive arguments from the command line.

---

## Practical Bash Project

### system-info.sh

Created a Bash script that displays basic system information.

The script provides information such as:

```text
Hostname
Kernel version
Current user
Date
Disk usage
Memory usage
System uptime
IP address
```

---

## Git

Studied the basic Git workflow and repository management.

### Basic Commands

```bash
git init
git clone
git status
git add
git commit
git push
git pull
```

Learned how to:

* Initialize a repository
* Clone a repository
* Check repository status
* Stage changes
* Create commits
* Push changes to GitHub
* Pull changes from GitHub

---

### Branches and Merge

Studied:

```bash
git branch
git merge
```

Practiced creating a branch, making changes, committing them, and merging the branch back into the main branch.

---

## Practical Work

The week consisted of three main areas:

```text
Python CLI
   ↓
Log analysis

Bash script
   ↓
System information

Git
   ↓
Version control
   ↓
Branches
   ↓
Merge
   ↓
GitHub
```

---

## What I Can Explain

After this week, I can explain:

* how `pathlib` works;
* how Python works with files;
* how `try`, `except`, and `finally` work;
* how JSON is loaded and saved;
* what regex is and how `re` is used;
* how command line arguments work;
* what `logging` is used for;
* how `subprocess` interacts with system commands;
* how `ipaddress` works with IP addresses;
* how `socket` is used for network operations;
* how Bash variables work;
* what `$?` represents;
* how Bash conditions and loops work;
* how Bash functions work;
* how Bash arguments work;
* how basic Git workflow works;
* how branches and merging work.

---

## Tools Used

```text
Python
Bash
Git
GitHub
Terminal
```

---

## Projects

* **Python CLI Log Analyzer**
* **system-info.sh**

---

## Progress

**Duration:** 1 week
**Focus:** Practical Python, Bash scripting, and Git
**Status:** IN PROGRESS
