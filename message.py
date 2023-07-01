```python
from database import database_connection, MessageSchema
from user import current_user

def send_message(receiver_id, content):
    # Create a new message
    new_message = MessageSchema()
    new_message.sender_id = current_user.id
    new_message.receiver_id = receiver_id
    new_message.content = content

    # Save the message to the database
    database_connection.session.add(new_message)
    database_connection.session.commit()

    return new_message
```