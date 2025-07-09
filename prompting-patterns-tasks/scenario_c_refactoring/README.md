# Scenario C: Refactoring Pattern

## Step 1: Test the Messy Contact Manager

First, see how bad the code is:

```bash
python contact_manager.py
```

**Try these commands:**
- `add` - Add a new contact (try adding a few)
- `list` - Show all contacts
- `search` - Search for a contact
- `delete` - Delete a contact
- `save` - Manually save contacts
- `quit` - Exit (auto-saves)

**What works:** All the functionality is there.

**What's wrong:** Look at the code! Everything is crammed into one giant 150+ line function. It's a mess!

## Step 2: The Refactoring Formula
**Current Issues + Goals + Success Criteria**

### Example Prompt
```
Current Issues:
- All code is in one 150-line main() function
- No error handling for invalid phone numbers
- Duplicate code for input validation

Goals:
1. Split into separate classes (Contact, ContactManager, InputValidator)
2. Add proper error handling
3. Remove duplicate validation code

Success Criteria:
- Each function under 20 lines
- All user inputs validated consistently
- Program handles errors gracefully without crashing
```

### Why This Pattern Works
- **Current Issues**: Identifies specific problems with existing code
- **Goals**: Clear targets for improvement
- **Success Criteria**: Measurable outcomes to know when you're done

## Step 3: Your Turn to Practice

After exploring the messy code, write refactoring prompts for:

1. **Database separation** - Move all file operations to separate class
2. **Menu system** - Replace if/elif chain with cleaner menu system
3. **Search functionality** - Add ability to find contacts by name/phone

*Check answers.md when you're done!*

## Test the Current Code
```bash
python contact_manager.py
```

Try these commands:
- `add` - add a new contact
- `list` - show all contacts
- `search` - find contacts
- `delete` - remove a contact
- `save` - save to file
- `quit` - exit

## Your Challenge
Use the **Refactoring** prompt pattern to clean up this messy code.

## Now You Try!
Write your refactoring prompt using all 5 elements above. Be specific about what good code looks like.

## Expert Solution
Check `/practice/expert_solutions/scenario_c_refactoring.md` after you write your prompt. 