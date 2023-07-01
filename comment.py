```python
from database import database_connection, CommentSchema
from user import current_user

def post_comment(post_id, comment_text):
    # Create a new comment
    new_comment = CommentSchema(post_id=post_id, user_id=current_user.id, text=comment_text)

    # Add the comment to the database
    database_connection.session.add(new_comment)
    database_connection.session.commit()

    return new_comment

def get_comments(post_id):
    # Query the database for comments on a specific post
    comments = CommentSchema.query.filter_by(post_id=post_id).all()

    return comments

def delete_comment(comment_id):
    # Query the database for the comment
    comment = CommentSchema.query.get(comment_id)

    # Check if the current user is the author of the comment
    if comment.user_id == current_user.id:
        # Delete the comment
        database_connection.session.delete(comment)
        database_connection.session.commit()
        return True
    else:
        return False

def edit_comment(comment_id, new_text):
    # Query the database for the comment
    comment = CommentSchema.query.get(comment_id)

    # Check if the current user is the author of the comment
    if comment.user_id == current_user.id:
        # Edit the comment
        comment.text = new_text
        database_connection.session.commit()
        return True
    else:
        return False
```