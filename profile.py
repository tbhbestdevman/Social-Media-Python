```python
from database import database_connection, UserSchema
from user import current_user

def get_profile(user_id):
    user_data = database_connection.get(UserSchema, user_id)
    return user_data

def update_profile(user_id, new_data):
    user_data = database_connection.get(UserSchema, user_id)
    for key, value in new_data.items():
        if key in user_data:
            user_data[key] = value
    database_connection.update(UserSchema, user_id, user_data)

def delete_profile(user_id):
    database_connection.delete(UserSchema, user_id)

def view_current_user_profile():
    return get_profile(current_user.id)

def update_current_user_profile(new_data):
    return update_profile(current_user.id, new_data)

def delete_current_user_profile():
    return delete_profile(current_user.id)
```