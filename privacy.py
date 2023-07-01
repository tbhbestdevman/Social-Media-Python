```python
from database import database_connection, UserSchema

def update_privacy_settings(user_id, new_settings):
    """
    Function to update the privacy settings of a user.
    """
    user = UserSchema.objects(id=user_id).first()
    if user:
        user.privacy_settings = new_settings
        user.save()
        return True
    return False

def get_privacy_settings(user_id):
    """
    Function to get the privacy settings of a user.
    """
    user = UserSchema.objects(id=user_id).first()
    if user:
        return user.privacy_settings
    return None

def check_privacy_settings(user_id, setting):
    """
    Function to check a specific privacy setting of a user.
    """
    user = UserSchema.objects(id=user_id).first()
    if user:
        return user.privacy_settings.get(setting)
    return None
```