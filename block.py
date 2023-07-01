```python
from database import database_connection
from user import UserSchema

def block_user(current_user, user_to_block):
    """
    Function to block a user.
    """
    # Check if the user exists in the database
    user = UserSchema.objects(id=user_to_block).first()
    if not user:
        return {"error": "User not found"}

    # Add the user to the current user's block list
    current_user.blocked_users.append(user_to_block)
    current_user.save()

    return {"success": "User blocked successfully"}

def unblock_user(current_user, user_to_unblock):
    """
    Function to unblock a user.
    """
    # Check if the user is in the current user's block list
    if user_to_unblock in current_user.blocked_users:
        current_user.blocked_users.remove(user_to_unblock)
        current_user.save()
        return {"success": "User unblocked successfully"}

    return {"error": "User not found in block list"}
```