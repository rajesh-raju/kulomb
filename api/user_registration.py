from flask import Blueprint,request,jsonify
from databaseconfig import databaseconfig
import datetime


user_registration_bp = Blueprint('user_reg',__name__)
@user_registration_bp.route('/user_registration', methods=['post'])
def user_reg():
    databaseobj = databaseconfig()
    conn = databaseobj.connect()
    if conn:
        json_obj = request.get_json()
        mycursor = conn.cursor()
        #mycursor.execute('SELECT * FROM KA_UserRegistration')
        #myresult = mycursor.fetchall()
        try:
            fst_name =  json_obj["First_Name"]
            lst_name = json_obj["Last_Name"]
            passwrd =  json_obj["Password"]
            mobile_no = str(json_obj["Mobile_No"])
            email = json_obj["Email"]
            pref_lang = json_obj["Pref_Language"]
            alter_mobile_no =  str(json_obj["Alterante_Mobile_No"])
            try:
                query = f'SELECT MOBILE_NUMBER, EMAIL FROM KA_UserRegistration'
                mycursor.execute(query)
                res = mycursor.fetchall()
                mob_num = [i[0].strip() for i in res]
                eml = [i[1].strip() for i in res]    
                if mobile_no.strip() in mob_num:
                    return jsonify({"Status": "Error", "Message": "This mobile number has already registered"})
                elif email.strip() in eml:
                    return jsonify({"Status": "Error", "Message": "This email has already registered"})
                query = f'INSERT INTO KA_UserRegistration(PASSWORD,First_Name,Last_Name,Mobile_Number,\
                                                        Email,PrefLanguage,AlternateMobile_Number,CreatedDate)\
                                                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
                values = (passwrd, fst_name, lst_name, mobile_no, email, pref_lang, alter_mobile_no, str(datetime.datetime.now()))
                mycursor.execute(query, values)
                conn.commit()
                return jsonify({"Status":"Success","Message":"User Created"})
            except Exception as err:
                conn.close()
                mycursor.close()
                return jsonify({"Status": "Error", "Message": "Error In Query " + err})
        except:
            conn.close()
            mycursor.close()
            return jsonify({"Status": "Error", "Message": "Json Not Specified Properly"})
    else:
        return jsonify({"Status":"Error","Message":"Error in connection"}) 


