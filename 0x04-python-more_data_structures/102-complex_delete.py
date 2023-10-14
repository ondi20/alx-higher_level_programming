#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = []  # Create a list to store keys to be deleted

    # Find keys with the specified value and store them in the list
    for key, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(key)

    # Delete the keys with the specified value
    for key in keys_to_delete:
        del a_dictionary[key]
"""
# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
complex_delete(my_dict, 2)

print(my_dict)  # Output: {'a': 1, 'd': 3}
"""