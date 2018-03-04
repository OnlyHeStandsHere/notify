from flask import Blueprint, render_template, jsonify, request
from models.models import User
from models.database import db_session
from .validate import validate_user_form


users = Blueprint('users', __name__,
                  template_folder='templates',
                  static_folder='static',
                  static_url_path='/users/static',
                  url_prefix='/users')





@users.route('/index', methods=['GET'])
def user_index():
    return render_template('user_index.html', title="Users")


@users.route('/api/index', methods=['GET'])
def api_user_index():
    return jsonify([u.serialize for u in User.query.all()])


@users.route('/api/new', methods=['POST'])
def new_user():
    return_data = {'errors': [], 'message': [], 'data': {}}
    try:
        data = request.get_json(force=True)
    except Exception as e:
        return_data['errors'].append('There was a problem with the request. Please try again')
        return_data['errors'].append(e.args)
        return jsonify(return_data)

    validate_user_form(data, return_data)

    #check to see if validation returned any errors
    if return_data['errors']:
        print('there were errors')
        return jsonify(return_data)

    # if no errors go ahead and create the user
    user = User(first_name=return_data['data']['first_name'],
                last_name=return_data['data']['last_name'],
                phone=return_data['data']['phone'],
                email=return_data['data']['email'])

    db_session.add(user)
    db_session.commit()



    return jsonify({'message': 'this worked'})