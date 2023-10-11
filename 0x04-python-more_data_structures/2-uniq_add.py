#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Initialize an empty set to store unique integers
    unique_integers = set()
    
    # Initialize a variable to keep track of the sum
    total = 0
    
    # Iterate through the list
    for num in my_list:
        # Check if the integer is not in the set of unique integers
        if num not in unique_integers:
            # Add the integer to the set and to the total sum
            unique_integers.add(num)
            total += num
    
    return total
"""
# Example usage:
my_list = [1, 2, 2, 3, 4, 4, 5]
result = uniq_add(my_list)
print(result)  # This will output 15 (1 + 2 + 3 + 4 + 5)
"""