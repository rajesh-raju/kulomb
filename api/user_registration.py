from flask import Blueprint,request
from databaseconfig import databaseconfig
import json


user_registration_bp = Blueprint('user_reg',__name__)
@user_registration_bp.route('/user_registration', methods=['post'])
def user_reg():
    databaseobj = databaseconfig()
    conn = databaseobj.connect()
    print(conn)
    if conn:
        jsonObj = request.get_json()
        return 'pass'

    else:
        return json.dumps({"Status":"Error","Message":"Error in connection"}) 


