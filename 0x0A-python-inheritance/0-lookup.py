#!usr/bin/python3
"""
Module to provide a lookup function.
"""
def lookup(obj):
    """
    Return a list of availble  attributes  and method  of an object.

    Parameters:
    -obj (object): The object to look up.

    Returns:
    -list: A list of attributes and methods.
    """
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) or attr.startswith("__")]
