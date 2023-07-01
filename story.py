```python
from database import database_connection, UserSchema, PostSchema
from user import current_user

class Story:
    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id

    def create_story(self):
        user = database_connection.query(UserSchema).get(self.user_id)
        post = database_connection.query(PostSchema).get(self.post_id)

        if user and post:
            new_story = {
                'user_id': self.user_id,
                'post_id': self.post_id,
                'created_at': datetime.datetime.now()
            }
            database_connection.add(new_story)
            database_connection.commit()
            return True
        return False

    def view_story(self):
        story = database_connection.query(Story).filter_by(user_id=self.user_id).first()
        if story:
            return story
        return None

    def delete_story(self):
        story = database_connection.query(Story).filter_by(user_id=self.user_id).first()
        if story:
            database_connection.delete(story)
            database_connection.commit()
            return True
        return False

def create_story(user_id, post_id):
    story = Story(user_id, post_id)
    return story.create_story()

def view_story(user_id):
    story = Story(user_id, None)
    return story.view_story()

def delete_story(user_id):
    story = Story(user_id, None)
    return story.delete_story()
```