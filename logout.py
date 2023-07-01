```python
from flask import Flask, session, redirect, url_for
from user import current_user

app = Flask(__name__)

@app.route('/logout')
def logout_user():
    session.pop('user_id', None)
    current_user = None
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
```