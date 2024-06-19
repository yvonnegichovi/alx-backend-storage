#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

# Test cases to demonstrate the functionality of get, get_str, and get_int
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value

# Additional tests for get_str and get_int
key = cache.store("hello")
print(cache.get_str(key))  # should print 'hello'

key = cache.store(123)
print(cache.get_int(key))  # should print 123
