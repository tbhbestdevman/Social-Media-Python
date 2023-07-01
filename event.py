```python
from datetime import datetime
from database import database_connection, UserSchema, EventSchema

class Event:
    def __init__(self, title, description, location, date_time, created_by):
        self.title = title
        self.description = description
        self.location = location
        self.date_time = date_time
        self.created_by = created_by

    def create_event(self):
        new_event = EventSchema(title=self.title, description=self.description, location=self.location, date_time=self.date_time, created_by=self.created_by)
        database_connection.session.add(new_event)
        database_connection.session.commit()

    def delete_event(self, event_id):
        event = EventSchema.query.get(event_id)
        if event:
            database_connection.session.delete(event)
            database_connection.session.commit()

    def update_event(self, event_id, title=None, description=None, location=None, date_time=None):
        event = EventSchema.query.get(event_id)
        if event:
            event.title = title if title else event.title
            event.description = description if description else event.description
            event.location = location if location else event.location
            event.date_time = date_time if date_time else event.date_time
            database_connection.session.commit()

    def get_event(self, event_id):
        event = EventSchema.query.get(event_id)
        return event

    def get_all_events(self):
        events = EventSchema.query.all()
        return events
```