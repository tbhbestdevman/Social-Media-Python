```python
from database import database_connection, UserSchema, PostSchema
from user import current_user

def list_items_for_sale():
    # Query the database for items listed for sale
    items_for_sale = database_connection.execute("SELECT * FROM marketplace WHERE status='for_sale'")
    return items_for_sale

def list_user_items():
    # Query the database for items listed by the current user
    user_items = database_connection.execute("SELECT * FROM marketplace WHERE user_id=?", (current_user.id,))
    return user_items

def add_item_for_sale(item):
    # Add a new item for sale in the marketplace
    database_connection.execute("INSERT INTO marketplace (user_id, item, status) VALUES (?, ?, 'for_sale')", (current_user.id, item))
    database_connection.commit()

def remove_item_from_sale(item_id):
    # Remove an item from sale in the marketplace
    database_connection.execute("UPDATE marketplace SET status='removed' WHERE id=? AND user_id=?", (item_id, current_user.id))
    database_connection.commit()

def buy_item(item_id):
    # Buy an item from the marketplace
    database_connection.execute("UPDATE marketplace SET status='sold', buyer_id=? WHERE id=?", (current_user.id, item_id))
    database_connection.commit()
```