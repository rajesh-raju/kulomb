from flask import Flask
#****************************************************************
from api import *

#****************************************************************


from flask_cors import CORS
app=Flask(__name__)
CORS(app)
#******************************************************************
app.register_blueprint(user_registration_bp,url_prefix = "")
app.register_blueprint(login_bp,url_prefix = "")



if __name__ == '__main__':
	app.debug = True
	app.jinja_env.cache = {}
	app.run()
