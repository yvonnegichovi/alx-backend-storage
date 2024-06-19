#!/usr/bin/env python3
"""
This module writes strings to Redis
"""

import redis
import uuid
from typing import Union, Callable, Optional


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
