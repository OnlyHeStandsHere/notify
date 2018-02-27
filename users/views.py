from flask import Blueprint, render_template, jsonify
from models.models import User
from models.database import db_session

users = Blueprint('users', __name__,
                  template_folder='templates',
                  static_folder='static',
                  static_url_path='/users/static',
                  url_prefix='/users')


@users.route('/index', methods=['GET'])
def user_index():
    return render_template('index.html', title="Users")


@users.route('/api/index', methods=['GET'])
def api_user_index():
    return jsonify([u.serialize for u in User.query.all()])


@users.route('/new', methods=['GET'])
def new_user():
    return render_template('form.html', title='New User')