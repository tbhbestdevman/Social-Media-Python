```python
from database import database_connection, UserSchema
from user import current_user

def follow_user(user_to_follow):
    # Check if the user to follow exists in the database
    user_schema = UserSchema()
    user = user_schema.load(database_connection.get_user(user_to_follow))

    if user is None:
        return "User to follow does not exist."

    # Check if the current user is already following the user
    if user_to_follow in current_user.following:
        return "You are already following this user."

    # Add the user to the current user's following list
    current_user.following.append(user_to_follow)

    # Save the current user's data to the database
    database_connection.save_user(current_user)

    return "You are now following " + user_to_follow
```