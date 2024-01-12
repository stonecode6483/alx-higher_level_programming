#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element with another in a new list.
    Args:
    my_list (list): The initial list.
    search: The element to replace in the list.
    replace: The new element.

    Returns:
    list: A new list with specified replacements.
    """
    #Create a new list to store the modified elements
    new_list = []

    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
            return new_list
