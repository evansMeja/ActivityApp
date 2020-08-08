def user_is_staff(user):
    return user.is_authenticated and user.is_staff 

def user_is_client(user):
    return user.is_authenticated and not user.is_staff
    
def user_is_authenticated(user):
    return user.is_authenticated