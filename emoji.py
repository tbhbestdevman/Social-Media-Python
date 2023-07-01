```python
class Emoji:
    def __init__(self, emoji_id, emoji_name, emoji_image):
        self.emoji_id = emoji_id
        self.emoji_name = emoji_name
        self.emoji_image = emoji_image

    def get_emoji_id(self):
        return self.emoji_id

    def get_emoji_name(self):
        return self.emoji_name

    def get_emoji_image(self):
        return self.emoji_image

def upload_emoji(emoji_name, emoji_image):
    # Connect to the database
    db = database_connection
    # Generate a unique id for the emoji
    emoji_id = db.generate_id()
    # Create a new emoji
    new_emoji = Emoji(emoji_id, emoji_name, emoji_image)
    # Add the new emoji to the database
    db.add_emoji(new_emoji)
    return new_emoji

def get_emoji(emoji_id):
    # Connect to the database
    db = database_connection
    # Get the emoji from the database
    emoji = db.get_emoji(emoji_id)
    return emoji

def delete_emoji(emoji_id):
    # Connect to the database
    db = database_connection
    # Delete the emoji from the database
    db.delete_emoji(emoji_id)
```