#!/usr/bin/env python3
""" Helper function to get pagination
"""


def index_range(page, page_size):
    """
    function that gets starting result No and
    end Result number for pagination
    """
    return ((page - 1) * page_size, page * page_size)
