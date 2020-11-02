from flask import jsonify, request
from myapp import app,db
from myapp.db_models import Resource



@app.route('/users/<string:ipp>', methods=['GET'])
def get_resource(ipp):
    db_res = Resource.query.filter_by(ip=ipp).first()
    if db_res:
        if db_res.availability:
            db_res.availability = False
            db.session.commit()
            return jsonify({'ip': db_res.ip, 'username': db_res.username, 'password': db_res.password})
        else:
            return "Resource is locked", 423
    else:
        return "Uninitialized resource requested", 400


@app.route('/users', methods=['POST'])
def release_resource():
    content = request.get_json()
    ip = content['Ip']
    db_res = Resource.query.filter_by(ip=ip).first()
    if db_res.availability:
        return ip + ' was already available', 200
    else:
        db_res.availability = True
        db.session.commit()
        return ip + ' resource is now available.', 200
