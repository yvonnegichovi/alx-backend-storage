#!/usr/bin/env python3
"""
This script that handles pymongo commands
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    The method inserts a new document in a collection based on kwargs
    pymongo collection: mongo_collection
    return the new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
