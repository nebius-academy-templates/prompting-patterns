# Expert Solution: Debugging Pattern

## Practice exercise solutions

### 1. Memory leak issue

**Good prompt:**
```
Problem: File organizer uses increasing amounts of memory and gets slower with large files.

Expected: Memory usage should stay constant regardless of file size.
Actual: Memory grows from 50MB to 500MB when processing 1000 files, processing speed drops from 10 files/sec to 2 files/sec.

Context files:
- file_organizer.py (main processing loop)
- Large test files in test_files/ directory

Suspected issue: File objects or data structures not being properly cleaned up after processing each file.
```

### 2. Permission errors

**Good prompt:**
```
Problem: Program crashes with "PermissionError: [Errno 13] Permission denied" when moving files.

Expected: Should handle permission errors gracefully and continue processing other files.
Actual: Entire program stops when it hits a protected file or folder.

Context files:
- file_organizer.py (file moving logic)
- test_files/ (contains some read-only files)

Error occurs in move_file() function when trying to move files to system directories.
```

### 3. Duplicate file handling

**Good prompt:**
```
Problem: Files with identical names overwrite each other without warning.

Expected: Should detect duplicates and either rename them or ask user what to do.
Actual: Second file with same name silently replaces the first file.

Context files:
- file_organizer.py (file moving and naming logic)
- test_files/ (contains duplicate.txt files)

Issue happens in organize_files() when destination file already exists.
```

## Key takeaways

- **Problem**: Be specific about the error and when it occurs.
- **Expected vs actual**: Clearly show the gap between what should happen and what does.
- **Context files**: Point to the exact files and functions involved.
- Include error messages and specific conditions that trigger the bug.
