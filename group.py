```python
from database import database_connection, UserSchema, PostSchema
from user import current_user

class Group:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.members = []
        self.posts = []

    def add_member(self, user):
        if user not in self.members:
            self.members.append(user)

    def remove_member(self, user):
        if user in self.members:
            self.members.remove(user)

    def create_post(self, content):
        new_post = PostSchema(content=content, author=current_user)
        self.posts.append(new_post)
        database_connection.session.add(new_post)
        database_connection.session.commit()

    def delete_post(self, post):
        if post in self.posts:
            self.posts.remove(post)
            database_connection.session.delete(post)
            database_connection.session.commit()

def create_group(name, description):
    new_group = Group(name, description)
    database_connection.session.add(new_group)
    database_connection.session.commit()
    return new_group
```