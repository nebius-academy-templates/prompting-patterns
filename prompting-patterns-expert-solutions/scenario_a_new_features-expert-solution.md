# Answers: New Features Pattern

## Practice Exercise Solutions

### 1. Add Memory Functions

**Good Prompt:**
```
Here's my current calculator code:
[paste calculator.py]

I need to add these memory features:
1. Memory store (M+) - save current display value
2. Memory recall (MR) - retrieve stored value
3. Memory clear (MC) - reset memory to zero

Please modify:
- calculator.py: Add memory_store, memory_recall, memory_clear methods
- Add memory variable to store the value
- Update the command interface to handle M+, MR, MC commands
```

**Why this works:** Shows current state, lists specific features, identifies which file to modify.

### 2. Add Percentage Calculations

**Good Prompt:**
```
Here's my current calculator code:
[paste calculator.py]

I need to add percentage calculations:
1. Basic percentage (e.g., 20% of 100 = 20)
2. Percentage increase (e.g., 100 + 20% = 120)
3. Percentage decrease (e.g., 100 - 20% = 80)

Please modify:
- calculator.py: Add percentage, percent_increase, percent_decrease methods
- Update the command interface to handle "percent" command
```

### 3. Add History Feature

**Good Prompt:**
```
Here's my current calculator code:
[paste calculator.py]

I need to add calculation history:
1. Store last 5 calculations with results
2. Display history command showing all stored calculations
3. Clear history command to reset the list

Please modify:
- calculator.py: Add history list and history management methods
- Update each calculation method to store results
- Add "show_history" and "clear_history" commands
```

## Key Takeaways

- **Context**: Always show or reference your current code
- **Requirements**: Number your features for clarity
- **File Structure**: Be specific about which files need changes
- Keep it simple - don't over-complicate the request! 