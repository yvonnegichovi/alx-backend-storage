#!/usr/bin/env python3
"""
This module writes strings to Redis
"""

import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """
    Implements a system to count how many times methods of the
    Cache class are called
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Increments the call count using INCR
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ':inputs'
        output_key = method.__qualname__ + ':outputs'
        
        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


class Cache:
    """
    creates a class Cache where that includes initialization of instances
    """
    def __init__(self):
        """
        Initializes private instance redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates random keys, store the input data in Redis using random key

        Args:
            - data
        Return:
            - key(string)
        """
        keys = str(uuid.uuid4())
        self._redis.set(keys, data)
        return keys

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        This method converts the data back to the desired format
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Automatically parametrize Cache.get
        with the correct conversion function
        """
        value = self.get(key, lambda x: x.decode('utf-8'))
        return value

    def get_int(self, key: str) -> Optional[int]:
        """
        Automatically parametrize Cache.get                             with the correct conversion function
        """
        value = self.get(key, int)
        return value
