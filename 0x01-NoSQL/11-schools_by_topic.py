#!/usr/bin/env python3
"""
This python script uses pymongo to execute MongoDB commands
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return the list of school having a specific topic

    Args:
        - mongo_collection: pymongo collection object
        - topic: will be topic searched

    Return:
        - list of school having a specific topic
    """
    topic = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return list(mongo_collection.find(topic))
