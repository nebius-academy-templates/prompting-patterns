#!/usr/bin/env python3
"""
Simple Cache System - For Learning About Classes
===============================================

This is a basic cache implementation to demonstrate object-oriented concepts.
Perfect for learning about classes, methods, and data structures.

Practice Challenge: Use the "Learning" prompt pattern to understand how it works
"""

import time
from typing import Any, Optional

class SimpleCache:
    """A basic cache implementation with size limits and expiration"""
    
    def __init__(self, max_size: int = 100, default_ttl: int = 300):
        """
        Initialize the cache
        
        Args:
            max_size: Maximum number of items to store
            default_ttl: Default time-to-live in seconds
        """
        self.max_size = max_size
        self.default_ttl = default_ttl
        self._data = {}  # Stores the actual cached values
        self._timestamps = {}  # Stores when items were added
        self._access_order = []  # For LRU (Least Recently Used) eviction
    
    def put(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """
        Store a value in the cache
        
        Args:
            key: The cache key
            value: The value to store  
            ttl: Time-to-live override (optional)
        """
        # Use default TTL if none provided
        if ttl is None:
            ttl = self.default_ttl
        
        current_time = time.time()
        
        # Remove expired items first
        self._cleanup_expired()
        
        # If cache is full, remove least recently used item
        if len(self._data) >= self.max_size and key not in self._data:
            self._evict_lru()
        
        # Store the new item
        self._data[key] = value
        self._timestamps[key] = {
            'created': current_time,
            'expires': current_time + ttl,
            'last_accessed': current_time
        }
        
        # Update access order
        if key in self._access_order:
            self._access_order.remove(key)
        self._access_order.append(key)
        
        print(f"Cached '{key}' (expires in {ttl}s)")
    
    def get(self, key: str) -> Optional[Any]:
        """
        Retrieve a value from the cache
        
        Args:
            key: The cache key
            
        Returns:
            The cached value or None if not found/expired
        """
        if key not in self._data:
            print(f"Cache miss: '{key}' not found")
            return None
        
        current_time = time.time()
        
        # Check if item has expired
        if current_time > self._timestamps[key]['expires']:
            print(f"Cache miss: '{key}' has expired")
            self._remove_key(key)
            return None
        
        # Update last accessed time and access order
        self._timestamps[key]['last_accessed'] = current_time
        self._access_order.remove(key)
        self._access_order.append(key)
        
        print(f"Cache hit: '{key}'")
        return self._data[key]
    
    def delete(self, key: str) -> bool:
        """
        Remove an item from the cache
        
        Args:
            key: The cache key
            
        Returns:
            True if item was removed, False if not found
        """
        if key in self._data:
            self._remove_key(key)
            print(f"Deleted '{key}' from cache")
            return True
        else:
            print(f"Cannot delete '{key}': not found in cache")
            return False
    
    def clear(self) -> None:
        """Remove all items from the cache"""
        self._data.clear()
        self._timestamps.clear()
        self._access_order.clear()
        print("Cache cleared")
    
    def stats(self) -> dict:
        """Get cache statistics"""
        current_time = time.time()
        expired_count = 0
        
        for key, timestamp_data in self._timestamps.items():
            if current_time > timestamp_data['expires']:
                expired_count += 1
        
        return {
            'total_items': len(self._data),
            'max_size': self.max_size,
            'expired_items': expired_count,
            'utilization': len(self._data) / self.max_size * 100
        }
    
    def _cleanup_expired(self) -> None:
        """Remove all expired items from cache"""
        current_time = time.time()
        expired_keys = []
        
        for key, timestamp_data in self._timestamps.items():
            if current_time > timestamp_data['expires']:
                expired_keys.append(key)
        
        for key in expired_keys:
            self._remove_key(key)
            print(f"Auto-removed expired key: '{key}'")
    
    def _evict_lru(self) -> None:
        """Remove the least recently used item"""
        if self._access_order:
            lru_key = self._access_order[0]
            self._remove_key(lru_key)
            print(f"Evicted LRU key: '{lru_key}'")
    
    def _remove_key(self, key: str) -> None:
        """Helper method to remove a key from all data structures"""
        self._data.pop(key, None)
        self._timestamps.pop(key, None)
        if key in self._access_order:
            self._access_order.remove(key)

def demo_cache_usage():
    """Demonstrate how the cache works"""
    print("Simple Cache System Demo")
    print("=" * 30)
    
    # Create a cache with small size and short TTL for demo
    cache = SimpleCache(max_size=3, default_ttl=5)
    
    # Store some values
    cache.put("user:123", {"name": "Alice", "email": "alice@example.com"})
    cache.put("user:456", {"name": "Bob", "email": "bob@example.com"})
    cache.put("product:789", {"name": "Widget", "price": 29.99})
    
    # Retrieve values
    user_data = cache.get("user:123")
    print(f"Retrieved user data: {user_data}")
    
    # Add another item (should evict LRU)
    cache.put("session:abc", {"token": "xyz789", "expires": "2024-12-31"})
    
    # Try to get evicted item
    cache.get("user:456")  # Should be cache miss
    
    # Show cache stats
    stats = cache.stats()
    print(f"\nCache stats: {stats}")
    
    # Wait for expiration demo
    print("\nWaiting 6 seconds for items to expire...")
    time.sleep(6)
    
    # Try to access expired items
    cache.get("user:123")  # Should be expired
    
    # Clean up
    cache.clear()

if __name__ == "__main__":
    demo_cache_usage() 