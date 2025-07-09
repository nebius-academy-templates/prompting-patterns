# Scenario E: Learning Pattern

## Step 1: Test the Cache System

First, see the cache in action:

```bash
python cache_system.py
```

**What you'll see:**
- Cache storing user data, products, and sessions
- Items being retrieved (cache hits)
- Least Recently Used (LRU) eviction when cache is full
- Items expiring after 5 seconds
- Cache statistics

**What to notice:**
- How LRU eviction works
- When items expire vs when they're evicted
- Cache hit vs cache miss messages

## Step 2: The Learning Formula
**Concept + Questions + Examples**

### Example Prompt
```
Concept: Cache eviction policies in my cache system

Questions:
1. When should I use LRU vs FIFO vs Random eviction?
2. How does cache size affect performance?
3. What are the trade-offs between memory usage and hit rates?

Examples: 
Show me practical scenarios using my cache_system.py:
- Web page caching (frequent access patterns)
- Database query caching (mixed access patterns)  
- Image thumbnail caching (large objects, infrequent access)
```

### Why This Pattern Works
- **Concept**: Specific topic you want to understand
- **Questions**: Targeted questions about what confuses you
- **Examples**: Real scenarios using your actual code

## Step 3: Your Turn to Practice

After watching the cache demo, write learning prompts for:

1. **Threading safety** - How to make cache thread-safe
2. **Memory management** - When cache uses too much RAM
3. **Performance monitoring** - How to measure cache effectiveness

*Check answers.md when you're done!* 