```python
import database
from user import UserSchema
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = UserSchema(username=data['username'], email=data['email'], password=hashed_password)
    database_connection = database.get_db_connection()
    database_connection.add(new_user)
    database_connection.commit()
    return jsonify({'message': 'New user created!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
```