# Answers: Refactoring Pattern

## Practice Exercise Solutions

### 1. Database Separation

**Good Prompt:**
```
Current Issues:
- File operations scattered throughout main() function
- No error handling for file read/write operations
- Hardcoded filename "contacts.txt" in multiple places

Goals:
1. Create ContactDatabase class to handle all file operations
2. Add proper error handling for file not found, permission errors
3. Make filename configurable through constructor

Success Criteria:
- All file operations in one class with consistent error handling
- Main function only handles user interface, not file operations
- Can easily switch between different storage formats (JSON, CSV, etc.)
```

### 2. Menu System Refactoring

**Good Prompt:**
```
Current Issues:
- Long if/elif chain with 8 different menu options
- Menu display code mixed with action code
- No validation for invalid menu choices

Goals:
1. Create Menu class with clean option handling
2. Separate menu display from menu actions
3. Add input validation and error messages

Success Criteria:
- Each menu option is a separate method
- Easy to add new menu options without changing existing code
- Invalid inputs show helpful error messages
```

### 3. Search Functionality

**Good Prompt:**
```
Current Issues:
- No way to find contacts except by scrolling through full list
- Users have to remember exact names to find contacts

Goals:
1. Add search by partial name matching
2. Add search by phone number
3. Add search by email address

Success Criteria:
- Search is case-insensitive and matches partial strings
- Search results display in same format as full contact list
- Empty search results show helpful "no matches found" message
```

## Key Takeaways

- **Current Issues**: Identify specific problems, not vague complaints
- **Goals**: Clear, numbered objectives for improvement
- **Success Criteria**: Measurable outcomes so you know when you're done
- Focus on one area at a time - don't try to fix everything at once! 