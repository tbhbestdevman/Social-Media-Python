```python
from database import database_connection
from user import UserSchema

class Notification:
    def __init__(self, user_id, message):
        self.user_id = user_id
        self.message = message

    def save_to_db(self):
        database_connection.insert('notifications', self.__dict__)

    @classmethod
    def get_notifications(cls, user_id):
        return database_connection.find('notifications', {"user_id": user_id})

def notify_user(user_id, message):
    notification = Notification(user_id, message)
    notification.save_to_db()

def get_user_notifications(user_id):
    return Notification.get_notifications(user_id)
```