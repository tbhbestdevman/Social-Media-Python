```python
from database import database_connection
from user import current_user
from post import PostSchema
from notification import notify_user

def share_post(post_id, user_id=None):
    """
    Function to share a post.
    """
    # If no user_id is provided, use the current user
    if user_id is None:
        user_id = current_user.id

    # Fetch the post from the database
    post = database_connection.get_post(post_id)

    # Check if the post exists
    if post is None:
        raise Exception("Post not found")

    # Create a new post with the same content, but marked as a share
    new_post = PostSchema(
        user_id=user_id,
        content=post.content,
        is_share=True,
        original_post_id=post.id
    )

    # Save the new post to the database
    database_connection.save_post(new_post)

    # Notify the original poster that their post has been shared
    notify_user(post.user_id, f"Your post has been shared by {current_user.username}")

    return new_post
```