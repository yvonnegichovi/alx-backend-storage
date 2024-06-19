#!/usr/bin/env python3
"""
This module writes strings to Redis
"""

import redis
import uuid
from typing import Union


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
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
