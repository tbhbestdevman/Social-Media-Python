```python
import getpass
from user import UserSchema
from database import database_connection

def login_user():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    user = database_connection.get_user(username)
    if user and UserSchema.validate_password(user, password):
        global current_user
        current_user = user
        print("Login successful!")
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    login_user()
```