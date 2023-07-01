```python
class Theme:
    def __init__(self, name, background_color, text_color, accent_color):
        self.name = name
        self.background_color = background_color
        self.text_color = text_color
        self.accent_color = accent_color

    def apply_theme(self, user):
        user.theme = self.name
        # Update user theme in the database
        database_connection.update_user_theme(user, self.name)

    def remove_theme(self, user):
        user.theme = None
        # Update user theme in the database
        database_connection.update_user_theme(user, None)

def change_theme(user, theme):
    if user.theme:
        current_theme = Theme(user.theme)
        current_theme.remove_theme(user)
    new_theme = Theme(theme)
    new_theme.apply_theme(user)

def get_theme(user):
    return user.theme
```