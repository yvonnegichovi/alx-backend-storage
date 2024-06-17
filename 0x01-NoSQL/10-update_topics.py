#!/usr/bin/env python3
"""
This script uses pymongo to deliver MongoDB executions
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    pymongo collection: mongo_collection
    name: school name to update
    topics: list of topics approached in the school
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )
