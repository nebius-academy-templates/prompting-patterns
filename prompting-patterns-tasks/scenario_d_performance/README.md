# Scenario D: Performance Pattern

## Step 1: Test the slow CSV processor

First, see how painfully slow this program is:

```bash
python csv_processor.py
```

**What it does:** 
- Creates 2000 rows of test sales data
- Processes the CSV file 
- Generates a sales report

**How long it takes:** 15-20 seconds (way too slow!)

**Watch for these slow parts:**
- Loading the CSV (lots of delays)
- Calculating totals (multiple passes through the data)
- Finding top products (terrible bubble sort!)
- Writing the report (one line at a time)

## Step 2: The performance formula
**Current problem + target + bottleneck**

### Example prompt
```
Current problem: CSV processor takes 30 seconds for 10MB file

Target: Process same file in under 5 seconds

Bottleneck: Reading file line by line and processing each row individually

Current code:
- csv_processor.py processes one row at a time
- No caching of repeated calculations
- Creates new objects for every row
```

### Why this pattern works
- **Current problem**: Describes the performance issue with measurable data.
- **Target**: Sets a clear goal with numbers.
- **Bottleneck**: Identifies where the slowdown happens.

## Step 3: Try it yourself

After running the script and observing the slow processing, write performance prompts for:

1. **Current slowness**: Fix the immediate performance issues.
2. **Memory usage**: Program uses too much RAM.
3. **Large file handling**: Crashes on files over 50MB.
