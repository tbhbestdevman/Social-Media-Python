```python
from database import database_connection, UserSchema
from user import current_user

def add_friend(user_id):
    friend = database_connection.get_user(user_id)
    if not friend:
        return "User not found"
    current_user.friends.append(friend)
    database_connection.update_user(current_user)
    return "Friend added successfully"

def remove_friend(user_id):
    friend = database_connection.get_user(user_id)
    if not friend:
        return "User not found"
    if friend in current_user.friends:
        current_user.friends.remove(friend)
        database_connection.update_user(current_user)
        return "Friend removed successfully"
    return "User is not a friend"

def get_friends_list():
    return current_user.friends

def is_friend(user_id):
    friend = database_connection.get_user(user_id)
    if not friend:
        return "User not found"
    return friend in current_user.friends
```