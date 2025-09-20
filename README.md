# Quick Commit Note (QCN)

**Interactive CLI to write clean, conventional-style Git commit messages with linting and history tracking.**

---

## Features

* Interactive CLI to generate commit messages following conventional commits.
* Lint your commit messages manually or via Git hooks.
* Keeps a history of all commits made through QCN.
* Optional Git hook integration (`commit-msg`) to enforce commit message rules.
* Configurable commit types and max summary length via `.qcnrc`.
* Lightweight and fully open-source.

---

## Demo (ASCII representation)

```
$ qcn new
Select commit type: feat
Enter scope (optional): cli
Enter short description: add new interactive CLI commit builder
Do you want to add extended description? (y/N): n
Commit created successfully: feat(cli): add new interactive CLI commit builder
```

---

## Installation

1. Clone the repo:

   git clone [https://github.com/](https://github.com/)<your-username>/qcn.git
   cd qcn

2. Create and activate a virtual environment:

   python3 -m venv env
   source env/bin/activate      # Linux/Mac

   # OR

   env\Scripts\activate       # Windows

3. Install QCN in editable mode:

   pip install -e .

4. Install other dependencies (if needed):

   pip install -r requirements.txt

---

## Usage

### Initialize configuration

```
git init                 # only if your project is not a Git repo yet
qcn init                 # creates default .qcnrc configuration
```

### Interactive commit builder

```
qcn new
```

Prompts:

1. Commit type (feat, fix, chore, etc.)
2. Scope (optional)
3. Short description
4. Optional extended body (opens your `$EDITOR`)

Then QCN will commit automatically if you confirm.

### Lint a commit message

```
qcn lint <file-or-message>
```

### Show commit history

```
qcn history
```

### Install Git commit-msg hook

```
qcn install-hook
# OR
bash scripts/install_hook.sh
```

---

## Running Tests

```
pytest tests/test_validators.py
```

All tests should pass ✅

---

## Common Errors & Fixes

### 1. ModuleNotFoundError: No module named 'qcn'

Cause: Python cannot find the package.
Fix:

1. Make sure your folder structure is correct:

   qcn\_project/
   ├── qcn/
   │   ├── **init**.py
   │   ├── cli.py
   │   └── ...
   ├── setup.py
   └── ...

2. Reinstall in editable mode:

   pip uninstall qcn -y
   pip install -e .

---

### 2. RuntimeError: Not in a git repository

Cause: `qcn new` requires a Git repository.
Fix: Initialize Git:

```
git init  
git add -A  
git commit -m "chore: initial commit"  
qcn new
```

---

### 3. Import "toml" could not be resolved

Cause: Missing dependency `toml`.
Fix:

```
pip install toml
```

Reload your editor and make sure the correct Python interpreter is selected.

---

## Tips

* Always run `qcn new` inside a Git repo.
* Customize commit types and rules via `.qcnrc`.
* Use Git hooks to enforce commit message linting.
* Commit history is saved in `.qcn_history.json`.

---

## Contributing

* Fork the repo and submit pull requests.
* Add new validators, commit types, or features.
* Ensure all tests pass before submitting.

---

## License

MIT License

Copyright (c) 2025 <Your Name>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
