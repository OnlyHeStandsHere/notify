from sqlalchemy import Column, Integer, String
from models.database import Base
from passlib.hash import sha512_crypt
import string
import secrets


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone = Column(String(30), unique=False, nullable=True)
    pw_hash = Column(String(200), nullable=True)

    def __init__(self, first_name, last_name, email, phone, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        if password:
            self.pw_hash = self.hash_pw(password)
        else:
            self.pw_hash = password

    def __repr__(self):
        return '<User %r>' % (self.name)

    def get_salt(self):
        options = string.ascii_letters + string.digits
        return ''.join(secrets.choice(options) for i in range(10))

    def hash_pw(self, password):
        head_salt = self.get_salt()
        tail_salt = self.get_salt()
        pw_string = ''.join([head_salt, password, tail_salt])
        my_hash = sha512_crypt.encrypt(pw_string)
        return '{}|{}|{}'.format(head_salt, my_hash, tail_salt)

    @staticmethod
    def verify_pw(password_hash, password):
        pw_hash_list = password_hash.split('|')
        pw_string = ''.join([pw_hash_list[0], password, pw_hash_list[-1]])
        return sha512_crypt.verify(pw_string, pw_hash_list[1])

    @property
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone
        }


class Client(Base):

    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return '<User %r>' % (self.name)

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

