```python
import database
from post import PostSchema
from user import current_user

def get_feed():
    # Get the list of users that the current user is following
    following_users = database.get_following(current_user)

    # Get the posts from the users that the current user is following
    posts = database.get_posts(following_users)

    # Sort the posts by timestamp in descending order
    sorted_posts = sorted(posts, key=lambda post: post.timestamp, reverse=True)

    # Convert the posts into the PostSchema format
    feed = [PostSchema(post) for post in sorted_posts]

    return feed

def display_feed():
    feed = get_feed()

    # Display the feed
    for post in feed:
        print(f"{post.user.username}: {post.content}")

    return
```