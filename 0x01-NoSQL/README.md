# 0x01. NoSQL

## Project Overview
This project covers the basics of NoSQL databases with a focus on MongoDB. By the end of this project, you should be able to understand the differences between SQL and NoSQL databases, explain the benefits of NoSQL, and perform basic CRUD operations using MongoDB.

### Resources
- [NoSQL Databases Explained](https://example.com)
- [What is NoSQL?](https://example.com)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://example.com)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://example.com)
- [Aggregation](https://example.com)
- [Introduction to MongoDB and Python](https://example.com)
- [mongo Shell Methods](https://example.com)
- [Mongosh](https://example.com)

### Learning Objectives
By the end of this project, you should be able to explain:
- What NoSQL means
- The differences between SQL and NoSQL
- What ACID means
- What document storage is
- The different types of NoSQL databases
- The benefits of NoSQL databases
- How to query, insert, update, and delete information from a NoSQL database
- How to use MongoDB

### Requirements

#### MongoDB Command Files
- Files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2).
- All files should end with a new line.
- The first line of all files should be a comment: `// my comment`.
- A `README.md` file is mandatory.
- The length of files will be tested using `wc`.

#### Python Scripts
- Files will be interpreted/compiled on Ubuntu 18.04 LTS using Python3 (version 3.7) and PyMongo (version 3.10).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- Code should use the `pycodestyle` style (version 2.5.*).
- The length of files will be tested using `wc`.
- All modules should have documentation.
- All functions should have documentation.
- Code should not execute when imported (use `if __name__ == "__main__":`).

### More Info

#### Install MongoDB 4.2 on Ubuntu 18.04
```sh
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
$ sudo service mongod status
$ mongo --version
$ pip3 install pymongo
```

### Tasks

#### 0. List all databases
Write a script that lists all databases in MongoDB.
```sh
$ cat 0-list_databases | mongo
```
File: `0-list_databases`

#### 1. Create a database
Write a script that creates or uses the database `my_db`.
```sh
$ cat 1-use_or_create_database | mongo
```
File: `1-use_or_create_database`

#### 2. Insert document
Write a script that inserts a document in the collection `school` with the attribute `name` set to "Holberton school".
```sh
$ cat 2-insert | mongo my_db
```
File: `2-insert`

#### 3. All documents
Write a script that lists all documents in the collection `school`.
```sh
$ cat 3-all | mongo my_db
```
File: `3-all`

#### 4. All matches
Write a script that lists all documents with `name="Holberton school"` in the collection `school`.
```sh
$ cat 4-match | mongo my_db
``}
File: `4-match`

#### 5. Count
Write a script that displays the number of documents in the collection `school`.
```sh
$ cat 5-count | mongo my_db
``}
File: `5-count`

#### 6. Update
Write a script that adds a new attribute to a document in the collection `school`. Update only documents with `name="Holberton school"` to add the attribute `address` with the value "972 Mission street".
```sh
$ cat 6-update | mongo my_db
``}
File: `6-update`

#### 7. Delete by match
Write a script that deletes all documents with `name="Holberton school"` in the collection `school`.
```sh
$ cat 7-delete | mongo my_db
``}
File: `7-delete`

#### 8. List all documents in Python
Write a Python function that lists all documents in a collection.
```python
def list_all(mongo_collection):
    """List all documents in a collection."""
    return list(mongo_collection.find())
```
File: `8-all.py`

#### 9. Insert a document in Python
Write a Python function that inserts a new document in a collection based on kwargs.
```python
def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection."""
    return mongo_collection.insert_one(kwargs).inserted_id
``}
File: `9-insert_school.py`

#### 10. Change school topics
Write a Python function that changes all topics of a school document based on the name.
```python
def update_topics(mongo_collection, name, topics):
    """Update topics of a school document."""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
``}
File: `10-update_topics.py`

#### 11. Where can I learn Python?
Write a Python function that returns the list of schools having a specific topic.
```python
def schools_by_topic(mongo_collection, topic):
    """Return list of schools having a specific topic."""
    return list(mongo_collection.find({'topics': topic}))
``}
File: `11-schools_by_topic.py`

#### 12. Log stats
Write a Python script that provides some stats about Nginx logs stored in MongoDB.
```python
def log_stats(mongo_collection):
    """Provide stats about Nginx logs."""
    num_logs = mongo_collection.count_documents({})
    print(f"{num_logs} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = mongo_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")
    status_check = mongo_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_check} status check")
```
File: `12-log_stats.py`

### Repository Structure
```plaintext
alx-backend-storage/
└── 0x01-NoSQL
    ├── 0-list_databases
    ├── 1-use_or_create_database
    ├── 2-insert
    ├── 3-all
    ├── 4-match
    ├── 5-count
    ├── 6-update
    ├── 7-delete
    ├── 8-all.py
    ├── 9-insert_school.py
    ├── 10-update_topics.py
    ├── 11-schools_by_topic.py
    └── 12-log_stats.py
```
