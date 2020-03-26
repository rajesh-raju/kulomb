from flask import Blueprint,request
import requests
import json

url = 'https://flow-api.fluctuo.com/v1?access_token=eFwW53d4EiCdlmbrs8muiM5gSvOrhPwh'
vehicles_info_bp = Blueprint('vehicles_info',__name__)
@vehicles_info_bp.route('/vehicles_info', methods=['post'])
def vehicles_info():
    try:
        json_obj = request.get_json()
        lat =  json_obj["lat"]
        lng = json_obj["lng"]
    except:
        return json.dumps({"Status": "Error", "Message": "Json Not Specified Properly"})
        
    st = "query ($lat: Float!, $lng: Float!) {vehicles (lat: $lat, lng: $lng) {id,type,attributes,lat,lng,provider {name}}}"
    data = {"query":st,"variables":{"lat":lat,"lng":lng}}
    headerInfo = {'content-type': 'application/json' }
    resp = requests.post(url, data=json.dumps(data) , headers=headerInfo)
    if resp.status_code == 200:
        return json.dumps({"Status":"Success","Message":"Ok","data":resp.json()['data']})
    else:
        return json.dumps({"Status":"error","Message":str(resp.json())})
    
   








