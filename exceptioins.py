class CustomException(Exception):
    pass

x = 3

try:
    raise CustomException("This is a custom exception message.")
    #raise Exception("An error occurred")  # Example exception
    #print(x)
    # if not type(x) is str:
    #     raise TypeError("x must be a string")
except NameError as e:
    print("Variable x is not defined.")
except ZeroDivisionError as e:
    print("Division by zero is not allowed.")
except Exception as e:
    print(e)
else:
    print("No exceptions occurred.")
finally:
    print("Execution completed.")