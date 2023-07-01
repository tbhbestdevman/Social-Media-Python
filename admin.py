```python
from database import database_connection
from user import UserSchema
from post import PostSchema
from comment import CommentSchema
from message import MessageSchema
from notification import NotificationSchema

class Admin:
    def __init__(self, current_user):
        self.current_user = current_user

    def check_admin(self):
        if self.current_user.is_admin:
            return True
        else:
            return False

    def delete_user(self, user_id):
        if self.check_admin():
            user = UserSchema.objects(id=user_id).first()
            if user:
                user.delete()
                return "User deleted successfully"
            else:
                return "User not found"
        else:
            return "You are not authorized to perform this action"

    def delete_post(self, post_id):
        if self.check_admin():
            post = PostSchema.objects(id=post_id).first()
            if post:
                post.delete()
                return "Post deleted successfully"
            else:
                return "Post not found"
        else:
            return "You are not authorized to perform this action"

    def delete_comment(self, comment_id):
        if self.check_admin():
            comment = CommentSchema.objects(id=comment_id).first()
            if comment:
                comment.delete()
                return "Comment deleted successfully"
            else:
                return "Comment not found"
        else:
            return "You are not authorized to perform this action"

    def delete_message(self, message_id):
        if self.check_admin():
            message = MessageSchema.objects(id=message_id).first()
            if message:
                message.delete()
                return "Message deleted successfully"
            else:
                return "Message not found"
        else:
            return "You are not authorized to perform this action"

    def delete_notification(self, notification_id):
        if self.check_admin():
            notification = NotificationSchema.objects(id=notification_id).first()
            if notification:
                notification.delete()
                return "Notification deleted successfully"
            else:
                return "Notification not found"
        else:
            return "You are not authorized to perform this action"
```