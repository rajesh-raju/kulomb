from flask import Blueprint,request,jsonify
import requests


url = 'https://flow-api.fluctuo.com/v1?access_token=eFwW53d4EiCdlmbrs8muiM5gSvOrhPwh'
vehicles_info_bp = Blueprint('vehicles_info',__name__)
@vehicles_info_bp.route('/vehicles_info', methods=['post'])
def vehicles_info():
    try:
        json_obj = request.get_json()
        lat =  json_obj["lat"]
        lng = json_obj["lng"]
    except:
        return jsonify({"Status": "Error", "Message": "Json Not Specified Properly"})
        
    st = "query ($lat: Float!, $lng: Float!) {vehicles (lat: $lat, lng: $lng) {id,type,attributes,lat,lng,provider {name}}}"
    data = {"query":st,"variables":{"lat":lat,"lng":lng}}
    headerInfo = {'content-type': 'application/json' }
    resp = requests.post(url, data=jsonify(data) , headers=headerInfo)
    if resp.status_code == 200:
        return jsonify({"Status":"Success","Message":"Ok","data":resp.json()['data']})
    else:
        return jsonify({"Status":"error","Message":str(resp.json())})
    
   








