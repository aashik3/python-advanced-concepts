from functools import lru_cache

# LRU Cache decorator
def lru_cache_decorator(maxsize=None):
    def decorator(func):
        memoized = lru_cache(maxsize)(func)
        memoized.cache_clear = func.cache_clear  # Add cache_clear method to the decorated function
        return memoized
    return decorator

# Example function to be memoized with LRU cache
@lru_cache_decorator(maxsize=3)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the memoized function
print(fibonacci(5))  # Calls the function and caches the results
print(fibonacci(3))  # Fetches the result from cache
print(fibonacci(2))  # Fetches the result from cache
print(fibonacci(4))  # Calls the function and caches the results

# Clear the cache
fibonacci.cache_clear()

# Test again after clearing the cache
print(fibonacci(5))  # Calls the function and caches the results
print(fibonacci(3))  # Fetches the result from cache
