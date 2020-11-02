from myapp import db
from flask_sqlalchemy import event

class Resource(db.Model):
    ip = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    availability = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"Resource('{self.ip}', '{self.username}', '{self.password}')"


@event.listens_for(Resource.__table__, 'after_create')
def create_departments(*args, **kwargs):
    for x in range(1, 20):
        _ip = '127.0.5.{}'.format(x)
        _name = 'Omri{}'.format(x)
        _password = 'password{}'.format(x)
        resource = Resource(ip=_ip, username=_name, password=_password)
        db.session.add(resource)
    db.session.commit()