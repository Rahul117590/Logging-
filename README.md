# Python Logging, Debugging & OS Module — Complete Guide

> A comprehensive hands-on repository covering Python's `logging` module, `ipdb` debugger, and the `os` module — from basic setup to advanced handlers with real-world programs.

---

## Repository Structure

```
├── basic_logging/
│   ├── intro_logging.py          # Basic logging setup
│   ├── labels_and_levels.py      # Logging levels demo
│   └── myfile.log                # Generated log file
│
├── programs/
│   ├── logging_program.py        # General program with logging
│   └── factorial_logging.py      # Factorial with logging
│
├── handlers/
│   ├── file_handler.py           # FileHandler example
│   └── stream_handler.py         # StreamHandler (console) example
│
├── debugging/
│   └── ipdb_demo.py              # ipdb debugger usage
│
├── os_module/
│   └── os_demo.py                # OS module operations
│
└── README.md
```

---

## 🚀 Getting Started

### 1. Create & Clone the Repository

```bash
# Step 1: Create a new repository on GitHub (github.com → New Repository)
# Step 2: Clone it to your local machine
git clone https://github.com/<your-username>/<repo-name>.git

# Step 3: Open in VS Code
cd <repo-name>
code .

# Step 4: Initialize Git (if not already done)
git init
```

---

## 📌 Topics Covered

### 2. Import Logging

```python
import logging
```

---

### 3. Logging Levels (Labels)

Python's logging module has **5 built-in severity levels**:

| Level | Numeric Value | Description |
|-------|--------------|-------------|
| `DEBUG` | 10 | Detailed diagnostic info |
| `INFO` | 20 | General operational messages |
| `WARNING` | 30 | Something unexpected happened |
| `ERROR` | 40 | A serious problem occurred |
| `CRITICAL` | 50 | A very serious error |

```python
import logging

logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")
logging.warning("This is a WARNING message")
logging.error("This is an ERROR message")
logging.critical("This is a CRITICAL message")
```

---

### 4. Format — Basic Configuration

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug("Debugging started")
logging.info("Application running")
```

---

### 5. Filename — Saving Logs to a File

```python
import logging

logging.basicConfig(
    filename='myfile.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True   # Overrides any previous basicConfig
)

logging.info("Log saved to myfile.log")
```

>  **Note:** `force=True` is required when reconfiguring `basicConfig` in the same session (Python 3.8+).

---

### 6. Log File Naming Convention

> 📝 **Rule:** Log files **must always end with `.log`** extension.

```
✅ myfile.log
✅ app_errors.log
✅ debug_output.log

 myfile.logging
 logs.txt
```

---

### 7. General Program Using Logging

```python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)

def divide(a, b):
    logging.info(f"divide() called with a={a}, b={b}")
    if b == 0:
        logging.error("Division by zero attempted!")
        return None
    result = a / b
    logging.debug(f"Result: {result}")
    return result

print(divide(10, 2))
print(divide(5, 0))
```

---

### 8. Factorial Program Using Logging

```python
import logging

logging.basicConfig(
    filename='factorial.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)

def factorial(n):
    logging.info(f"factorial() called with n={n}")
    if n < 0:
        logging.error("Negative input! Factorial not defined.")
        return None
    if n == 0 or n == 1:
        logging.debug(f"Base case reached: factorial({n}) = 1")
        return 1
    result = n * factorial(n - 1)
    logging.debug(f"factorial({n}) = {result}")
    return result

num = 5
print(f"Factorial of {num} = {factorial(num)}")
```

---

### 9. Logging Handlers

Handlers **send log records to specific destinations** (file, console, email, etc.).

| Handler | Destination |
|---------|------------|
| `FileHandler` | Log file on disk |
| `StreamHandler` | Console / terminal |
| `RotatingFileHandler` | File with size limit |
| `SMTPHandler` | Email |

---

### 10. File Handler

```python
import logging

# Basic config
logging.basicConfig(
    filename='filehandler.log',
    level=logging.DEBUG,
    format='%(name)s - %(asctime)s - %(levelname)s - %(message)s'
)

# Create FileHandler object
file_handler = logging.FileHandler('filehandler.log')
file_handler.setLevel(logging.DEBUG)

# Create Formatter and set it on the handler
formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Get root logger and attach the handler
logger = logging.getLogger('')
logger.addHandler(file_handler)

logger.info("This message goes to the log file via FileHandler")
logger.error("This error is recorded in the file")
```

---

### 11. Stream Handler (Console Output)

```python
import logging

# Basic config (file-based)
logging.basicConfig(
    filename='stream_test.log',
    level=logging.DEBUG,
    format='%(name)s - %(asctime)s - %(levelname)s - %(message)s'
)

# Create StreamHandler — logs to console
console_log = logging.StreamHandler()
console_log.setLevel(logging.DEBUG)

# Create Formatter
formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
console_log.setFormatter(formatter)

# Get root logger and add handler
logging.getLogger('').addHandler(console_log)

# Create a named logger
logger1 = logging.getLogger('user3')
logger1.info("This message appears on the CONSOLE via StreamHandler")
logger1.warning("StreamHandler warning — visible in terminal!")
```

 **Output:** Messages appear **on the console**, not just in the log file.

---

### 12. Debugging with `ipdb`

`ipdb` is an interactive Python debugger — like `pdb` but with better syntax highlighting and tab completion.

**Installation:**
```bash
pip install ipdb
```

**Usage:**
```python
import ipdb

def calculate(x, y):
    result = x + y
    ipdb.set_trace()   # Execution pauses here — interactive debug prompt opens
    return result * 2

print(calculate(3, 4))
```

**Common `ipdb` Commands:**

| Command | Action |
|---------|--------|
| `n` | Next line |
| `s` | Step into function |
| `c` | Continue execution |
| `p var` | Print variable value |
| `q` | Quit debugger |
| `l` | List surrounding code |

---

### 13. OS Module

The `os` module in Python provides a way to **interact with the operating system**, allowing you to perform system-level tasks such as file and directory manipulation, environment variable management, and process handling.

It acts as an **interface between the Python script and the underlying operating system**, providing functionality that is portable across different operating systems like **Windows, macOS, and Linux**.

```python
import os

# ── Current Working Directory ──────────────────────────────────
print(os.getcwd())                    # Get current directory
os.chdir('/path/to/directory')        # Change directory

# ── Directory Operations ───────────────────────────────────────
os.mkdir('new_folder')               # Create single directory
os.makedirs('parent/child/folder')   # Create nested directories
os.rmdir('empty_folder')             # Remove empty directory
os.removedirs('parent/child')        # Remove nested empty dirs

# ── File Operations ────────────────────────────────────────────
os.rename('old.txt', 'new.txt')      # Rename file
os.remove('file.txt')                # Delete file
print(os.listdir('.'))               # List files in directory

# ── Path Operations ────────────────────────────────────────────
print(os.path.exists('myfile.log'))  # Check if path exists
print(os.path.isfile('app.py'))      # Check if it's a file
print(os.path.isdir('logs'))         # Check if it's a directory
print(os.path.join('folder', 'file.txt'))  # Join paths safely

# ── Environment Variables ──────────────────────────────────────
print(os.environ.get('PATH'))        # Get PATH variable
os.environ['MY_VAR'] = 'hello'       # Set environment variable

# ── System Info ────────────────────────────────────────────────
print(os.name)                       # 'nt' (Windows) / 'posix' (Linux/Mac)
print(os.getpid())                   # Current process ID
```

---

## Requirements

```bash
pip install ipdb
```

> All other modules (`logging`, `os`) are part of Python's **standard library** — no installation needed.

---

##  License

This repository is created for educational purposes as part of Python learning practice.

---

##  Author

**Rahul Kumar**  
B.Tech — Computer Science Engineering (Data Analytics)  
Babu Banarasi Das Institute of Technology, Ghaziabad  
GitHub: [Rahul117590](https://github.com/Rahul117590)
