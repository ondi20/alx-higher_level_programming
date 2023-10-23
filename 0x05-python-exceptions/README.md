0x05-Python_Exceptions
**Difference between Errors and Exceptions:**

1. **Errors:** Errors are typically issues that occur at a more fundamental level in the program, such as syntax errors, name errors, or even system errors like running out of memory. These are often fatal and can lead to the termination of the program.

2. **Exceptions:** Exceptions, on the other hand, are events that occur during the execution of a program but are not necessarily fatal. They are used to handle abnormal or unexpected situations, allowing the program to recover gracefully from these issues.

**What are Exceptions and How to Use Them:**

- Exceptions are objects in Python that represent errors or unexpected events. They are used to handle and manage abnormal situations in code.
- Exceptions are raised when an error occurs. To use them, you need to raise exceptions when an exceptional condition is encountered in your code and handle them using try-except blocks.

**When to Use Exceptions:**

You should use exceptions when:

1. Dealing with potentially error-prone code.
2. Handling exceptional situations like input validation or file I/O errors.
3. Ensuring your program can gracefully recover from unexpected errors.

**How to Correctly Handle an Exception:**

To handle an exception in code:

1. Wrap the potentially problematic code within a `try` block.
2. Provide one or more `except` blocks to catch specific exception types.
3. Add optional `finally` blocks for code that should run whether or not an exception is raised.

Here's a basic example in Python:

```python
try:
    # code that might raise an exception
    result = 10 / 0  # ZeroDivisionError
except ZeroDivisionError:
    # handle the specific exception
    print("You can't divide by zero.")
except Exception as e:
    # handle other exceptions
    print(f"An error occurred: {e}")
finally:
    # optional cleanup code
    print("Cleanup, whether or not an exception was raised.")
```

**Purpose of Catching Exceptions:**

Catching exceptions allows you to:

1. Prevent program crashes.
2. Provide meaningful error messages to users.
3. Log errors for debugging.
4. Implement alternate behavior when errors occur.
5. Clean up resources, like closing files or network connections.

**How to Raise a Built-in Exception:**

You can raise a built-in exception in Python using the `raise` statement. For example:

```python
x = -5
if x < 0:
    raise ValueError("x cannot be negative")
```

This code will raise a `ValueError` exception with the specified message.

**When to Implement a Clean-up Action After an Exception:**

You should implement clean-up actions (e.g., closing files, releasing resources) after an exception when your program uses resources that need to be properly managed. This ensures that resources are not leaked and your program behaves gracefully in the presence of errors. The `finally` block is commonly used for such clean-up operations. For example:

```python
file = None
try:
    file = open("example.txt", "r")
    # perform file operations
except FileNotFoundError:
    print("File not found")
finally:
    if file is not None:
        file.close()  # Ensure the file is closed, even if an exception occurred.
```

In this example, the file will be closed in the `finally` block, whether or not an exception occurred during file operations.