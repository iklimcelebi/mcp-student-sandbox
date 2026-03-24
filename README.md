# MCP Student Sandbox

A Python learning project with 4 challenging code files designed to teach clean code, debugging, and security best practices.

## 📚 Project Overview

This sandbox contains four Python files, each demonstrating different programming challenges:

1. **spaghetti_logic.py** - Code quality & modularity
2. **failing_calculator.py** - Error handling & debugging
3. **secret_leak.py** - Security & credential management
4. **mystery_module.py** - Code analysis & documentation

---

## 🎯 Files & Challenges

### 1. spaghetti_logic.py
**Challenge**: Refactor messy, monolithic code into modular, maintainable functions.

**Original Issues**:
- Poor variable naming (res, d, val, s)
- Mixed concerns (calculation, formatting, logging)
- No documentation
- Hard to test individual parts

**Refactored Solution**:
- Separated into single-responsibility functions
- `calculate_total()` - handles multiplication
- `format_total()` - formats output strings
- `log_results()` - manages file I/O
- Added comprehensive docstrings

**Run**:
```bash
python -c "from spaghetti_logic import process_data; print(process_data([10, 20, 30]))"
```

---

### 2. failing_calculator.py
**Challenge**: Debug and fix a runtime error that crashes on specific inputs.

**Original Problem**:
```
ZeroDivisionError: division by zero
print(average_ratios([10, 5, 0]))  # Crashes when 0 is in the list
```

**Root Cause**:
- Function attempts `100 / numbers[i]` without checking for zero values

**Fix Applied**:
- Filter out zero values: `valid_numbers = [num for num in numbers if num != 0]`
- Add error handling and validation
- Return sensible default if all numbers are zero
- Added unit test support with docstring

**Run**:
```bash
export AWS_SECRET_KEY=test_key
python failing_calculator.py
# Output: Result: 15.0, Success! No division by zero error.
```

**Test Cases**:
```bash
# Normal case
python -c "from failing_calculator import average_ratios; print(average_ratios([10, 5]))"

# With zero (now safe)
python -c "from failing_calculator import average_ratios; print(average_ratios([10, 5, 0]))"

# Edge case: all zeros
python -c "from failing_calculator import average_ratios; print(average_ratios([0, 0, 0]))"
```

---

### 3. secret_leak.py
**Challenge**: Implement secure credential management and prevent secret leaks.

**Original Security Issues** ❌:
- Hardcoded AWS secret key in source code
- Secrets visible in version control (GitHub)
- Full credentials printed in logs
- Anyone with repo access could steal keys

**Security Fixes Applied** ✅:
- Load credentials from environment variables
- Safe logging (preview only first 8 characters)
- Proper error handling for missing secrets
- `.gitignore` prevents `.env` file commits
- `.env.example` template for developers

**Usage**:

1. Setup:
```bash
cp .env.example .env
# Edit .env and add your real AWS credentials
# AWS_SECRET_KEY=your_actual_key_here
```

2. Run with environment variable:
```bash
export AWS_SECRET_KEY=AKIA_YOUR_KEY_HERE
python secret_leak.py
# Output: INFO:__main__:Connecting to AWS (key starts with: AKIA_YOU...)
```

**Security Best Practices**:
- Never commit `.env` to git (protected by `.gitignore`)
- Use environment variables for local development
- Use secret managers (AWS Secrets Manager, HashiCorp Vault) in production
- Log only non-sensitive key previews
- Validate that secrets are provided before using them

See `SECURITY_FIXES.md` for detailed security analysis.

---

### 4. mystery_module.py
**Challenge**: Understand and document a function that's hard to read.

**What It Does**:
The function `fn_x(a, b, c)` solves **quadratic equations** using the quadratic formula.

**Decoded Formula**:
```
Equation: ax² + bx + c = 0
Discriminant: d = b² - 4ac
Solutions (roots): x = (-b ± √d) / 2a
```

**Examples**:
```python
# x² - 5x + 6 = 0  →  (x-2)(x-3)=0  →  roots: (3, 2)
fn_x(1, -5, 6)  # Returns (3.0, 2.0)

# x² + 1 = 0  →  no real solutions
fn_x(1, 0, 1)   # Returns None (discriminant < 0)
```

**Key Insight**: Understanding mathematical context makes mysterious code clear!

---

## 📋 Setup & Installation

### Requirements
- Python 3.7+
- Git
- GitHub CLI (optional, for repo management)

### Clone & Run
```bash
git clone https://github.com/iklimcelebi/mcp-student-sandbox.git
cd mcp-student-sandbox

# Test all files
python spaghetti_logic.py
python failing_calculator.py
python secret_leak.py
```

---

## 🔐 Security Configuration

### Environment Variables
Create a `.env` file (not committed to git):
```bash
cp .env.example .env
# Edit with your actual credentials
AWS_SECRET_KEY=AKIA_YOUR_REAL_KEY_HERE
AWS_ACCESS_KEY=ASIA_YOUR_REAL_KEY_HERE
```

### .gitignore
Protected files (automatically ignored):
- `.env` - Local secrets
- `__pycache__/` - Python compiled files
- `*.log` - Log files
- `.vscode/`, `.idea/` - IDE folders

---

## 📚 Learning Outcomes

After completing this sandbox, you'll understand:

✅ **Clean Code**: Modularity, single responsibility, naming conventions  
✅ **Debugging**: Identifying root causes, error handling, testing  
✅ **Security**: Credential management, secret protection, best practices  
✅ **Code Analysis**: Understanding complex functions, mathematical concepts

---

## 📖 Documentation

- `SECURITY_FIXES.md` - Detailed security analysis and solutions
- `.env.example` - Environment variable template
- `.gitignore` - Git exclusion rules

---

## 🤝 Contributing

This is a learning sandbox. Feel free to:
- Refactor further
- Add test cases
- Improve documentation
- Try different approaches

---

## 📝 License

Educational project - use freely for learning purposes.

---

## 🔗 Resources

- [PEP 8 - Python Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [OWASP - Credential Management](https://owasp.org/)
- [Python Logging Best Practices](https://docs.python.org/3/howto/logging.html)
- [Quadratic Formula](https://en.wikipedia.org/wiki/Quadratic_formula)

---

**Happy Learning!** 🚀
