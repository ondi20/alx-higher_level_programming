#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Initialize a counter for printed integers
    i = 0  # Initialize an index for iterating through the list
    try:
        while count < x:
            try:
                # Attempt to format and print the element as an integer
                print("{:d}".format(my_list[i]), end=" ")
                count += 1  # Increment the count of printed integers
            except (ValueError, TypeError):
                pass  # Skip non-integer values
            i += 1  # Move to the next element in the list
    except IndexError:
        pass  # Handle the case when x is larger than the list's length
    print()  # Add a new line after printing all integers
    return count