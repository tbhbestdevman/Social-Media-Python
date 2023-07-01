```python
from database import database_connection, PostSchema, UserSchema

class Tag:
    def __init__(self, name):
        self.name = name

    def get_posts(self):
        posts = database_connection.get_posts_by_tag(self.name)
        return posts

    def get_users(self):
        users = database_connection.get_users_by_tag(self.name)
        return users

def create_tag(name):
    new_tag = Tag(name)
    database_connection.add_tag(new_tag)
    return new_tag

def search_tag(name):
    tag = database_connection.get_tag(name)
    return tag

def delete_tag(name):
    database_connection.delete_tag(name)
```