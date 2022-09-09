from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPDigestAuth
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from config import config

# Routes
from routes import User
from routes import Bill

app = Flask(__name__)
app.config['SECRET_KEY'] = "root"
auth = HTTPBasicAuth()
CORS(app, resources={"*": {"origins": "http://localhost:9300"}})


users = {
    "juan": generate_password_hash("123") 
} 

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/login', methods=['GET','POST'])
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())

def page_not_found(error):
    return "<h1>Not found page</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(User.main, url_prefix='/users')
    app.register_blueprint(Bill.main, url_prefix='/bills')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()