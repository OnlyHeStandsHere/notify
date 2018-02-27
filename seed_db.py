from models.models import User, Client
from models.database import db_session

def seed_users():
    user1 = User('joe', 'shmoe', 'joe@email.com', '123-123-4321', 'password')
    user2 = User('jane', 'shmoe', 'jane@email.com', '123-123-4321', 'password')
    user3 = User('foo', 'bar', 'foo@email.com', '123-123-4321', 'password')
    user4 = User('chuck', 'norris', 'chuck@email.com', '123-123-4321', 'password')
    user5 = User('donald', 'duck', 'donald@email.com', '123-123-4321', 'password')

    db_session.add(user1)
    db_session.add(user2)
    db_session.add(user3)
    db_session.add(user4)
    db_session.add(user5)

    db_session.commit()

def seed_clients():
    client1 = Client('Big Client')
    client2 = Client('Little Client')
    client3 = Client('Chad')

    db_session.add(client1)
    db_session.add(client2)
    db_session.add(client3)

    db_session.commit()
