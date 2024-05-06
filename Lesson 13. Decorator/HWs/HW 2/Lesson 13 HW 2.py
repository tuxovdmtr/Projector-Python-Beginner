# Write a decorator that wraps a function in a try-except block
# and prints an error if any type of error has happened.
# Example:
# @catch_errors
# def some_function_with_risky_operation(data):
#     print(data['key'])


# some_function_with_risky_operation({'foo': 'bar'})
# > Found 1 error during execution of your function: KeyError no such key as foo

# some_function_with_risky_operation({'key': 'bar'})
# > bar

def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e: 
            print(f"Found 1 error during execution of your function: {e.__class__.__name__} no such key as '{list(args[0].keys())[0]}'") 
    return wrapper

@catch_errors
def some_function_with_risky_operation(value):
    print(value['key'])

some_function_with_risky_operation({'keyc': 'bar'})
