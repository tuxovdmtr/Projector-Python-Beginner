# Optional: Create a decorator that will check types.
# It should take a function with arguments and validate inputs with annotations.
# It should work for all possible functions.
# Don`t forget to check the return type as well
# Example:

# @check_types
# def add(a: int, b: int) -> int:
#     return a + b

# add(1, 2)
# > 3

# add("1", "2")
# > TypeError: Argument a must be int, not str

def check_type(func):  
    def wrapper(*args):
        for arg in args:
            if type(arg) is int:
                continue
            else:
                raise TypeError(f"{arg} is a {type(arg).__name__} type. Enter an integer.")
        return func(*args)
    return wrapper    
    
@check_type
def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))
add(1, "2")
add(True, "2")
add([1, 2], 2)