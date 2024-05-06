# Write a decorator that ensures a function is only called by users with a specific role.
# Each function should have an user_type with a string type in kwargs.
# Example:
# @is_admin
# def show_customer_receipt(user_type: str):
#     # Some very dangerous operation

# show_customer_receipt(user_type='user')
# > ValueError: Permission denied

# show_customer_receipt(user_type='admin')
# > function pass as it should be

def is_admin(func):
    def wrapper(**kwargs):
        if kwargs.get("user_type") == "admin":
            print("Access granted")
            return func(**kwargs)
        else:
            raise ValueError("Permission denied")        
    return wrapper

@is_admin
def show_customer_receipt(user_type: str):
    print("Customer receipt shown")


show_customer_receipt(user_type='admin')