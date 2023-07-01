```python
from database import database_connection, UserSchema, PostSchema
from user import current_user

class Page:
    def __init__(self, page_id, name, owner_id):
        self.page_id = page_id
        self.name = name
        self.owner_id = owner_id
        self.posts = []

    def create_post(self, post_content):
        new_post = PostSchema(post_content, current_user)
        self.posts.append(new_post)
        database_connection.commit()

    def delete_post(self, post_id):
        for post in self.posts:
            if post.post_id == post_id:
                self.posts.remove(post)
                database_connection.commit()
                break

    def get_page_posts(self):
        return self.posts

def create_page(name):
    owner_id = current_user
    page_id = len(database_connection['pages']) + 1
    new_page = Page(page_id, name, owner_id)
    database_connection['pages'].append(new_page)
    database_connection.commit()

def delete_page(page_id):
    for page in database_connection['pages']:
        if page.page_id == page_id:
            database_connection['pages'].remove(page)
            database_connection.commit()
            break

def get_page_by_id(page_id):
    for page in database_connection['pages']:
        if page.page_id == page_id:
            return page
    return None
```