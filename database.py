```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a database in RAM
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database_connection = create_connection()

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        email text NOT NULL,
                                        password text NOT NULL
                                    ); """

    sql_create_posts_table = """CREATE TABLE IF NOT EXISTS posts (
                                    id integer PRIMARY KEY,
                                    user_id integer NOT NULL,
                                    content text NOT NULL,
                                    timestamp text NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES users (id)
                                );"""

    if database_connection is not None:
        create_table(database_connection, sql_create_users_table)
        create_table(database_connection, sql_create_posts_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```