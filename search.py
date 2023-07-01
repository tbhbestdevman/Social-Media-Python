```python
import database

def search_content(query, database_connection):
    # Connect to the database
    conn = database_connection.connect()

    # Create a cursor object
    cur = conn.cursor()

    # Execute the query
    cur.execute("SELECT * FROM posts WHERE content LIKE ?", ('%' + query + '%',))

    # Fetch all the matching rows
    results = cur.fetchall()

    # Close the connection
    conn.close()

    # Return the results
    return results
```