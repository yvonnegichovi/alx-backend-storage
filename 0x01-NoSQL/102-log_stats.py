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

    check = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(check))

    # Aggregate to get the top 10 most present IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = collection.aggregate(pipeline)

    print("IPs:")
    for ip in top_ips:
        print("\t{}: {}".format(ip['_id'], ip['count']))


if __name__ == "__main__":
    log_stats()
