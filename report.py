```python
from database import database_connection
from user import current_user

def report_content(content_id, report_reason):
    """
    Function to report a content. It takes content_id and report_reason as parameters.
    """
    report_query = "INSERT INTO reports (content_id, reporter_id, report_reason) VALUES (?, ?, ?)"
    database_connection.execute(report_query, (content_id, current_user.id, report_reason))

    # Notify the admin about the report
    notify_admin(content_id, report_reason)

def notify_admin(content_id, report_reason):
    """
    Function to notify the admin about a report. It takes content_id and report_reason as parameters.
    """
    notification_message = f"Content with ID: {content_id} has been reported for {report_reason}."
    notification_query = "INSERT INTO notifications (user_id, message) VALUES (?, ?)"
    database_connection.execute(notification_query, (1, notification_message))  # Assuming admin's user_id is 1
```
