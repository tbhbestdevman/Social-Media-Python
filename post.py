```python
from database import database_connection, PostSchema
from user import current_user

def create_post(content, image=None, video=None):
    new_post = PostSchema()
    new_post.user_id = current_user.id
    new_post.content = content
    new_post.image = image
    new_post.video = video

    database_connection.session.add(new_post)
    database_connection.session.commit()

    return new_post

def get_post(post_id):
    post = database_connection.session.query(PostSchema).filter_by(id=post_id).first()
    return post

def update_post(post_id, content=None, image=None, video=None):
    post = get_post(post_id)
    if post.user_id == current_user.id:
        if content:
            post.content = content
        if image:
            post.image = image
        if video:
            post.video = video

        database_connection.session.commit()

    return post

def delete_post(post_id):
    post = get_post(post_id)
    if post.user_id == current_user.id:
        database_connection.session.delete(post)
        database_connection.session.commit()

def get_user_posts(user_id):
    posts = database_connection.session.query(PostSchema).filter_by(user_id=user_id).all()
    return posts
```