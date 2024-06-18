#!/usr/bin/env python3
"""
This Python script uses pymongo to execute MongoDB commands
"""

from pymongo import MongoClient


def log_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    num_logs = collection.count_documents({})
    print("{} logs".format(num_logs))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    check = collection.count_documents({"methods": "GET", "path": "/status"})
    print("{} status check".format(check))


if __name__ == "__main__":
    log_stats()
