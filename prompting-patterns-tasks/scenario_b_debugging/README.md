# Scenario B: Debugging Pattern

## Step 1: Test the buggy file organizer

First, let's trigger the bug and observe what happens:

```bash
python file_organiser.py
```

**Expected behavior:** Files get organized into folders by type (images, documents, etc.)

**Actual behavior:** The program crashes when it encounters certain file types.

**Error message:**
```
TypeError: unsupported operand type(s) for /: 'NoneType' and 'str'
```

**Root cause:** The script doesn't know how to handle `.py`, `.ini`, or `.md` files.

## Step 2: The debugging formula
**Problem + expected vs actual + context files**

### Example prompt
```
Problem: My file organiser crashes with a "KeyError" when processing files.

Expected: Should handle unknown file types gracefully.
Actual: It crashes and stops processing.

Context files:
- file_organiser.py (main logic)
- test_files/ (sample files that cause crashes)

Error message:
KeyError: '.xyz' in get_file_category() function
```

### Why this pattern works
- **Problem**: A clear description of what's going wrong.
- **Expected vs actual**: Highlights the gap between what the intended behavior and what's happening.
- **Context files**: Points to the relevant code and test cases.

## Step 3: Try it yourself

After you reproduce the crash, write debugging prompts for:

1. **Current crash**: Fix the immediate error.
2. **Memory leak**: Program gets slower with large files.
3. **Permission errors**: Can't move files to certain folders.
