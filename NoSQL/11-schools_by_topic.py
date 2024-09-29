#!/usr/bin/env python3
""" 11-main """


def schools_by_topic(mongo_collection, topic):
    """result"""
    return mongo_collection.find({ "topics": topic })
