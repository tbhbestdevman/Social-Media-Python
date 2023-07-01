```python
import datetime
from database import database_connection

class Ad:
    def __init__(self, ad_id, advertiser, content, start_date, end_date):
        self.ad_id = ad_id
        self.advertiser = advertiser
        self.content = content
        self.start_date = start_date
        self.end_date = end_date

    def is_active(self):
        current_date = datetime.date.today()
        return self.start_date <= current_date <= self.end_date

def create_ad(advertiser, content, start_date, end_date):
    ad_id = database_connection.insert_ad(advertiser, content, start_date, end_date)
    return Ad(ad_id, advertiser, content, start_date, end_date)

def get_ad(ad_id):
    ad_data = database_connection.get_ad(ad_id)
    return Ad(*ad_data)

def delete_ad(ad_id):
    database_connection.delete_ad(ad_id)

def update_ad(ad_id, content=None, start_date=None, end_date=None):
    database_connection.update_ad(ad_id, content, start_date, end_date)
    return get_ad(ad_id)
```