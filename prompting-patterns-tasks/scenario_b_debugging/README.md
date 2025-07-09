# Scenario B: Debugging Pattern

## Step 1: Test the Buggy File Organiser

First, let's trigger the bug:

```bash
python file_organiser.py
```

**What should happen:** Files get organised into folders by type (images, documents, etc.)

**What actually happens:** Program crashes with an error when it hits certain file types!

**The error you'll see:**
```
TypeError: unsupported operand type(s) for /: 'NoneType' and 'str'
```

**Why it crashes:** The script doesn't know how to handle `.py`, `.ini`, and `.md` files.

## Step 2: The Debugging Formula
**Problem + Expected vs Actual + Context Files**

### Example Prompt
```
Problem: My file organiser crashes with "KeyError" when processing files

Expected: Should handle unknown file types gracefully
Actual: Program crashes and stops processing

Context files:
- file_organiser.py (main logic)
- test_files/ (sample files that cause crashes)

Error message:
KeyError: '.xyz' in get_file_category() function
```

### Why This Pattern Works
- **Problem**: Clear description of what's wrong
- **Expected vs Actual**: Shows the gap between what should happen and what does
- **Context Files**: Points to relevant code and test cases

## Step 3: Your Turn to Practice

After you see the crash, write debugging prompts for:

1. **The current crash** - Fix the immediate error
2. **Memory leak** - Program gets slower with large files
3. **Permission errors** - Can't move files to certain folders

*Check answers.md when you're done!* 