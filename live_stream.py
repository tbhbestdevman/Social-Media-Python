```python
import datetime
from database import database_connection
from user import current_user

class LiveStream:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.start_time = None
        self.end_time = None
        self.streamer = current_user

    def start_live_stream(self):
        self.start_time = datetime.datetime.now()
        query = "INSERT INTO live_streams (title, description, start_time, streamer) VALUES (?, ?, ?, ?)"
        database_connection.execute(query, (self.title, self.description, self.start_time, self.streamer))
        database_connection.commit()
        print(f"Live stream '{self.title}' has started.")

    def end_live_stream(self):
        self.end_time = datetime.datetime.now()
        query = "UPDATE live_streams SET end_time = ? WHERE title = ? AND streamer = ?"
        database_connection.execute(query, (self.end_time, self.title, self.streamer))
        database_connection.commit()
        print(f"Live stream '{self.title}' has ended.")

    def get_live_stream_info(self):
        query = "SELECT * FROM live_streams WHERE title = ? AND streamer = ?"
        result = database_connection.execute(query, (self.title, self.streamer)).fetchone()
        return result
```