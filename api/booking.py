from flask import Blueprint,request,jsonify
from databaseconfig import databaseconfig
import datetime


booking_bp = Blueprint('booking',__name__)
@booking_bp.route('/booking', methods=['post'])
def booking():
    databaseobj = databaseconfig()
    conn = databaseobj.connect()
    if conn:
        json_obj = request.get_json()
        mycursor = conn.cursor()
        try:
            user_id =  str(json_obj["User_Id"])
            vehicle_attribute = json_obj["Vehicle_Attribute"]
            vehicle_id =  json_obj["Vehicle_Id"]
            start_lat = str(json_obj["Start_Lat"])
            start_lon = str(json_obj["Start_Lon"])
            vehicle_provider = json_obj["Vehicle_Provider"]
            vehicle_type =  json_obj["Vehicle_Type"]
            try:
                query = '''INSERT INTO KA_Booking(User_Id, Vehicle_Attribute, Vehicle_Id,
                           Start_Lat, Start_Lon,  Vehicle_Provider, Vehicle_Type,Booking_Date) 
                           VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'''
                time_stamp = str(datetime.datetime.now()).split(".")[0]
                values = (user_id, vehicle_attribute, vehicle_id, start_lat, start_lon, vehicle_provider, vehicle_type, time_stamp)
                mycursor.execute(query, values)
                conn.commit()
                query = f"SELECT Booking_Id FROM KA_Booking WHERE User_Id='{user_id}' and Vehicle_Id='{vehicle_id}' and Booking_Date='{time_stamp}' "
                res = mycursor.execute(query)
                res = mycursor.fetchall()
                print(res)
                print(time_stamp)
                return jsonify({"Status":"Success","Message":"User Created","User Id":user_id,"Bookin Id":res[0][0]})
            except Exception as err:
                conn.close()
                mycursor.close()
                if str(err).find("foreign key constraint fails")!= -1:
                    return jsonify({"Status": "Error", "Message": "User Id does not exists"})
                return jsonify({"Status": "Error", "Message": "Error In Query " + str(err)})
        except:
            conn.close()
            mycursor.close()
            return jsonify({"Status": "Error", "Message": "Json Not Specified Properly"})
    else:
        return jsonify({"Status":"Error","Message":"Error in connection"}) 


