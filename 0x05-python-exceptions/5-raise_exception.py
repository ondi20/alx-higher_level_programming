#!/usr/bin/python3
def raise_exception():
    try:
        # Attempt an operation that causes a TypeError
        result = "string" + 42  # Adding a string and an integer
    except TypeError as te:
        print(f"TypeError: {te}")