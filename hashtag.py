```python
from database import database_connection, PostSchema

class Hashtag:
    def __init__(self, tag):
        self.tag = tag

    def get_posts(self):
        query = "SELECT * FROM posts WHERE content LIKE %s"
        cursor = database_connection.cursor()
        cursor.execute(query, ('%' + self.tag + '%',))
        posts = cursor.fetchall()
        return [PostSchema(post) for post in posts]

def create_hashtag(tag):
    return Hashtag(tag)
```