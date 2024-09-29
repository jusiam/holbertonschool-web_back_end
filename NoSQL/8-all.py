#!/usr/bin/env python3
""" List all documents in Python"""


def list_all(mongo_collection):
    """results"""
    documents = mongo_collection.find()
    return documents
