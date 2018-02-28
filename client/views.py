from flask import Blueprint, render_template, jsonify
from models.models import Client
from models.database import db_session


client = Blueprint('client', __name__,
                   template_folder='templates',
                   static_folder='static',
                   static_url_path='/clients/static',
                   url_prefix='/clients')


@client.route('/home')
def client_home():
    return render_template('clients.html', title='Clients')


@client.route('/api/index')
def client_index():
    return jsonify([c.serialize for c in Client.query.all()])


@client.route('/api/<string:name>')
def client_id(name):
    raise NotImplemented


@client.route('/api/new')
def new_client():
    raise NotImplemented


@client.route('/api/<string:name>/edit')
def edit_client(name):
    raise NotImplemented


@client.route('/api/<string:name>/delete')
def delete_client(name):
    raise NotImplemented