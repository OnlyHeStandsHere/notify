from flask import Flask, render_template, request, url_for, jsonify
from models.database import db_session
from models.models import User
from users.views import users
from clients.views import client

app = Flask(__name__)
app.register_blueprint(users)
app.register_blueprint(client)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
