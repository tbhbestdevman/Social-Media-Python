```python
import database
from post import PostSchema

def get_trending_posts():
    # Connect to the database
    database_connection = database.connect()

    # Query to get the top 10 posts with the most likes
    query = """
    SELECT * FROM posts
    ORDER BY likes DESC
    LIMIT 10
    """

    # Execute the query
    result = database_connection.execute(query)

    # Convert the result into Post objects
    trending_posts = [PostSchema(post) for post in result]

    return trending_posts

def display_trending_posts():
    # Get the trending posts
    trending_posts = get_trending_posts()

    # Display the trending posts in the 'post-container' section
    for post in trending_posts:
        print(f"Post ID: {post.id}, Likes: {post.likes}, Content: {post.content}")

if __name__ == "__main__":
    display_trending_posts()
```