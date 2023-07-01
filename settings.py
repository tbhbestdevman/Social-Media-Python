```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration settings for the app
app_config = {
    "SECRET_KEY": os.getenv("SECRET_KEY"),
    "DATABASE_URI": os.getenv("DATABASE_URI"),
    "MAIL_SERVER": os.getenv("MAIL_SERVER"),
    "MAIL_PORT": os.getenv("MAIL_PORT"),
    "MAIL_USE_TLS": os.getenv("MAIL_USE_TLS"),
    "MAIL_USERNAME": os.getenv("MAIL_USERNAME"),
    "MAIL_PASSWORD": os.getenv("MAIL_PASSWORD"),
    "RECAPTCHA_PUBLIC_KEY": os.getenv("RECAPTCHA_PUBLIC_KEY"),
    "RECAPTCHA_PRIVATE_KEY": os.getenv("RECAPTCHA_PRIVATE_KEY"),
    "GOOGLE_CLIENT_ID": os.getenv("GOOGLE_CLIENT_ID"),
    "GOOGLE_CLIENT_SECRET": os.getenv("GOOGLE_CLIENT_SECRET"),
    "FACEBOOK_CLIENT_ID": os.getenv("FACEBOOK_CLIENT_ID"),
    "FACEBOOK_CLIENT_SECRET": os.getenv("FACEBOOK_CLIENT_SECRET"),
    "TWITTER_CLIENT_ID": os.getenv("TWITTER_CLIENT_ID"),
    "TWITTER_CLIENT_SECRET": os.getenv("TWITTER_CLIENT_SECRET"),
}

def update_settings(new_settings):
    """
    Function to update settings.
    """
    global app_config
    app_config.update(new_settings)
    return app_config
```