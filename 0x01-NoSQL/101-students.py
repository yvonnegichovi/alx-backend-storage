#!/usr/bin/env python3
"""
Python script that performs MongoDB functions
"""


def top_students(mongo_collection):
    """
    Returns all the students sorted by average score

    Args:
        - mongo_collection: pymongo collection
    Returns:
        - all students sorted by average score
    The top must be ordered
    Average score must be part of each item returns with key = averageScore
    """
    pipeline = [
        {
            '$addFields': {
                'averageScore': { '$avg': '$topics.score' }
            }
        },
        {
            '$sort': { 'averageScore': -1 }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
