#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None  # Return None if the dictionary is empty

    best_key = None
    best_value = float('-inf')  # Initialize with negative infinity to ensure any value is greater

    for key, value in a_dictionary.items():
        if value > best_value:
            best_key = key
            best_value = value

    return best_key
"""
# Example usage:
my_dict = {'Alice': 95, 'Bob': 87, 'Charlie': 92, 'David': 98}
result = best_score(my_dict)
print(result)  # This will output 'David' (the key with the biggest integer value)
"""