# Answers: Performance Pattern

## Practice Exercise Solutions

### 1. Memory Usage Issue

**Good Prompt:**
```
Current Problem: CSV processor uses 2GB RAM to process 100MB file

Target: Process same file using under 200MB RAM

Bottleneck: Loading entire file into memory at once, creating objects for every row that aren't garbage collected

Current code:
- csv_processor.py reads all rows into a list before processing
- Creates new dictionary objects for each row that accumulate in memory
- No streaming or batch processing
```

### 2. Startup Time Issue

**Good Prompt:**
```
Current Problem: Program takes 10 seconds to load before it can start processing files

Target: Reduce startup time to under 2 seconds

Bottleneck: Loading unnecessary modules and initialising large data structures at startup

Current code:
- csv_processor.py imports heavy libraries not needed immediately
- Pre-loads configuration and lookup tables that could be lazy-loaded
- Initialises GUI components even in command-line mode
```

### 3. Large File Handling

**Good Prompt:**
```
Current Problem: Program crashes with "MemoryError" on files larger than 50MB

Target: Handle files up to 1GB without crashing

Bottleneck: Trying to load entire file into memory instead of processing in chunks

Current code:
- csv_processor.py uses pandas.read_csv() which loads everything at once
- No streaming or chunked processing
- All calculations done on full dataset rather than incrementally
```

## Key Takeaways

- **Current Problem**: Include specific measurements (time, memory, file sizes)
- **Target**: Set realistic, measurable goals
- **Bottleneck**: Identify the exact cause, not just symptoms
- Use real numbers from testing your code - don't guess! 