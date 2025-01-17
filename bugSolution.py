def my_function(x):
    try:
        return 1 / x
    except ZeroDivisionError:
        return 0  # Handle the exception gracefully
        # Or raise a more informative exception, or log it
        # print("Error: Cannot divide by zero") 