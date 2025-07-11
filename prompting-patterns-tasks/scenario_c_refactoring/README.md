# Scenario C: Refactoring Pattern

## Step 1: Test the messy contact manager

First, run the app to see how messy the code is:

```bash
python contact_manager.py
```

**Try these commands:**
- `add`: Add a new contact (try adding a few).
- `list`: Show all contacts.
- `search`: Search for a contact.
- `delete`: Delete a contact.
- `save`: Manually save contacts.
- `quit`: Exit (auto-saves).

**What works:** All the features are in place.

**What's wrong:** The entire program is packed into one giant 150+ line function. It's a mess!

## Step 2: The refactoring formula
**Current issues + goals + success criteria**

### Example prompt
```
Current issues:
- All code is in one 150-line main() function
- No error handling for invalid phone numbers
- Duplicate code for input validation

Goals:
1. Split into separate classes (Contact, ContactManager, InputValidator)
2. Add proper error handling
3. Remove duplicate validation code

Success criteria:
- Each function under 20 lines
- All user inputs validated consistently
- Program handles errors gracefully without crashing
```

### Why this pattern works
- **Current issues**: Identifies specific problems with existing code.
- **Goals**: Clear targets for improvement.
- **Success criteria**: Measurable outcomes to know when everything is done.

## Step 3: Try it yourself

After exploring the messy code, write refactoring prompts for:

1. **Database separation**: Move all file operations to a separate class.
2. **Menu system**: Replace the if/elif chain with a cleaner menu system.
3. **Search functionality**: Add the ability to find contacts by name/phone.

*Check expert-solution.md when you're done!*
