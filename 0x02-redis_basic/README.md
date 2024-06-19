# 0x02. Redis Basic
Back-end | Redis
## Resources
- Redis Crash Course Tutorial
- Redis Commands
- Redis Python Client
- How to Use Redis With Python

## Learning Objectives
- Understand how to use Redis for basic operations.
- Learn how to use Redis as a simple cache.

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- Files should end with a new line.
- A README.md file at the root of the project folder is mandatory.
- The first line of all files should be exactly #!/usr/bin/env python3.
- Code should follow the pycodestyle style (version 2.5).
- All modules should have documentation.
- All classes should have documentation.
- All functions and methods should have documentation.
- All functions and coroutines must be type-annotated.

## Installation
- To install Redis on Ubuntu 18.04:

'''sh
Copy code
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
'''
Using Redis in a Container
Redis server is stopped by default. Start it with:

sh
Copy code
$ service redis-server start
Tasks
0. Writing Strings to Redis
Create a Cache class:

Initialize a private Redis client instance _redis.
Flush the instance using flushdb.
Create a store method:

Takes a data argument.
Generates a random key and stores the data in Redis.
Returns the key.
python
Copy code
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
Repo:

GitHub repository: alx-backend-storage
Directory: 0x02-redis_basic
File: exercise.py
1. Reading from Redis and Recovering Original Type
Create a get method:

Takes a key string and an optional Callable argument fn.
Converts the data back to the desired format using fn.
Implement get_str and get_int methods:

Automatically parametrize Cache.get with the correct conversion function.
python
Copy code
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
Repo:

GitHub repository: alx-backend-storage
Directory: 0x02-redis_basic
File: exercise.py
2. Incrementing Values
Create a count_calls decorator:

Takes a method Callable argument.
Increments a count each time the method is called.
Decorate Cache.store with count_calls:

python
Copy code
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
Repo:

GitHub repository: alx-backend-storage
Directory: 0x02-redis_basic
File: exercise.py
3. Storing Lists
Create a call_history decorator:

Stores the history of inputs and outputs for a function.
Decorate Cache.store with call_history:

python
Copy code
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))
Repo:

GitHub repository: alx-backend-storage
Directory: 0x02-redis_basic
File: exercise.py
4. Retrieving Lists
Implement a replay function:

Displays the history of calls of a function.
python
Copy code
cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
Expected Output:

css
Copy code
Cache.store was called 3 times:
Cache.store(*('foo',)) -> <generated_key>
Cache.store(*('bar',)) -> <generated_key>
Cache.store(*(42,)) -> <generated_key>
Repo:

GitHub repository: alx-backend-storage
Directory: 0x02-redis_basic
File: exercise.py
5. Implementing an Expiring Web Cache and Tracker
Create a get_page function:

Fetches HTML content of a URL and caches it with a 10-second expiration.
Use requests module:

File: web.py

Repo:

GitHub repository: alx-backend-storage
Directory: 0x02-redis_basic
File: web.py
