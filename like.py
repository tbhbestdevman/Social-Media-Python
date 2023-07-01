```python
from database import database_connection, PostSchema
from user import current_user

class Like:
    def __init__(self, post_id):
        self.post_id = post_id
        self.user_id = current_user.id

    def save_to_db(self):
        query = "INSERT INTO likes (post_id, user_id) VALUES (?, ?)"
        params = (self.post_id, self.user_id)
        database_connection.execute(query, params)

    @staticmethod
    def remove_like(post_id):
        query = "DELETE FROM likes WHERE post_id = ? AND user_id = ?"
        params = (post_id, current_user.id)
        database_connection.execute(query, params)

    @staticmethod
    def get_likes(post_id):
        query = "SELECT COUNT(*) FROM likes WHERE post_id = ?"
        params = (post_id,)
        result = database_connection.execute(query, params).fetchone()
        return result[0] if result else 0
```