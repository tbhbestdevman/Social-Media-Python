```python
from database import database_connection, UserSchema

current_user = None

def create_user(username, password, email):
    new_user = UserSchema(username=username, password=password, email=email)
    database_connection.session.add(new_user)
    database_connection.session.commit()
    return new_user

def login_user(username, password):
    global current_user
    user = database_connection.session.query(UserSchema).filter_by(username=username).first()
    if user and user.password == password:
        current_user = user
        return True
    return False

def logout_user():
    global current_user
    current_user = None

def update_settings(new_settings):
    global current_user
    if current_user:
        for key, value in new_settings.items():
            setattr(current_user, key, value)
        database_connection.session.commit()

def reset_password(old_password, new_password):
    global current_user
    if current_user and current_user.password == old_password:
        current_user.password = new_password
        database_connection.session.commit()
        return True
    return False

def verify_email(verification_code):
    global current_user
    if current_user and current_user.verification_code == verification_code:
        current_user.email_verified = True
        database_connection.session.commit()
        return True
    return False

def block_user(user_id):
    global current_user
    if current_user:
        blocked_user = database_connection.session.query(UserSchema).get(user_id)
        if blocked_user:
            current_user.blocked_users.append(blocked_user)
            database_connection.session.commit()

def follow_user(user_id):
    global current_user
    if current_user:
        followed_user = database_connection.session.query(UserSchema).get(user_id)
        if followed_user:
            current_user.following.append(followed_user)
            database_connection.session.commit()
```