```python
import os
from database import database_connection

class Sticker:
    def __init__(self, sticker_id, sticker_url):
        self.sticker_id = sticker_id
        self.sticker_url = sticker_url

    def save_to_database(self):
        query = "INSERT INTO stickers (sticker_id, sticker_url) VALUES (?, ?)"
        database_connection.execute(query, (self.sticker_id, self.sticker_url))

    @staticmethod
    def get_sticker(sticker_id):
        query = "SELECT * FROM stickers WHERE sticker_id = ?"
        result = database_connection.execute(query, (sticker_id,))
        return result.fetchone()

    @staticmethod
    def delete_sticker(sticker_id):
        query = "DELETE FROM stickers WHERE sticker_id = ?"
        database_connection.execute(query, (sticker_id,))

    @staticmethod
    def update_sticker(sticker_id, new_url):
        query = "UPDATE stickers SET sticker_url = ? WHERE sticker_id = ?"
        database_connection.execute(query, (new_url, sticker_id))
```