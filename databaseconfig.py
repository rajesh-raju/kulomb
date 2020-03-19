import mysql.connector

class databaseconfig:
	def connect(self):
		try:
			cnx = mysql.connector.connect(host= '35.238.119.235',
                              database='KULOMB_DB',
                              user='root',
                              password='kulomb123',
                              port=3306,
                              connect_timeout=1000 )
			return cnx
		except:
			return 0
