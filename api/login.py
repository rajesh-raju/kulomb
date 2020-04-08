from flask import Blueprint,request,jsonify
from databaseconfig import databaseconfig


login_bp = Blueprint('login',__name__)
@login_bp.route('/login', methods=['post'])
def login():
    databaseobj = databaseconfig()
    conn = databaseobj.connect()
    if conn:
        json_obj = request.get_json()
        mycursor = conn.cursor()
        try:
            mob_r_eml =  str(json_obj["Mobile/Email"])
            passwrd =  json_obj["Password"]
            try:
                query = f"SELECT UserId FROM KA_UserRegistration WHERE (Mobile_Number = '{mob_r_eml}' \
                or Email = '{mob_r_eml}') AND PASSWORD = '{passwrd}'"
                mycursor.execute(query)
                res = mycursor.fetchall()
                if len(res) == 0:
                    return jsonify({"Status":"Error","Message":"Credentials Does Not Match"})    
                else:
                    return jsonify({"Status":"Success","Message":"Login Successful","Data":{"User_ID":res[0][0]}})
                
            except Exception as err:
                conn.close()
                mycursor.close()
                return jsonify({"Status": "Error", "Message": "Error In Query " + str(err)})
        except Exception as err:
            conn.close()
            mycursor.close()
            return jsonify({"Status": "Error", "Message": "Json Not Specified Properly"})
    else:
        return jsonify({"Status":"Error","Message":"Error in connection"}) 


