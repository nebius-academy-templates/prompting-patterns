# Scenario A: New Features Pattern

## Step 1: Test the current calculator

Start by checking what the calculator can do:

```bash
python calculator.py
```

**Try these commands:**
- `add`: Add two numbers (e.g. 5 + 3).
- `subtract`: Subtract two numbers.
- `multiply`: Multiply two numbers.
- `divide`: Divide two numbers.
- `history`: Show calculation history.
- `clear`: Clear the history.
- `quit`: Exit the calculator.

**Current functionality:** Basic arithmetic operations with history tracking.

## Step 2: The new features prompting formula
**Context + requirements + file structure**

### Example prompt
```
Here's my current calculator code:
[paste calculator.py]

I need to add the following features:
1. Square root function
2. Power/exponent function  
3. Clear button to reset display

Please update:
- calculator.py: Add the new calculation methods.
- The GUI: Include buttons for the new features.
```

### Why this pattern works
- **Context**: Shows current code state.
- **Requirements**: A numbered list of new features to add.
- **File structure**: You specify which files need changes.

## Step 3: Try it yourself

Write prompts using the same formula for these scenarios:

1. **Add memory functions** (store, recall, clear memory)
2. **Add percentage calculations** 
3. **Add history feature** (show last 5 calculations)

*Check expert-solution.md when you're done!* 
