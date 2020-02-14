#using flask_restful
from flask_restful import Resource, Api
import os
import datetime
import ast
import math
from sklearn.externals import joblib
import simplejson as json
from io import StringIO
from flask import Flask, flash, request, redirect, url_for, session, jsonify, abort, render_template_string, send_from_directory, Response
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin

# creating the flask app 
app = Flask(__name__) 

# creating an API object 
api = Api(app) 
CORS(app)

class Hello(Resource): 

	# Corresponds to POST request 
	def post(self): 
		recived_data = request.data
		recived_data = json.dumps(recived_data)
		recived_data = json.loads(recived_data)
		recived_data = ((ast.literal_eval(recived_data)))
		
		aeroplane = int(recived_data['aeroplane'])
		source = int(recived_data['source'])
		destination = int(recived_data['destination'])
		total_stop = int(recived_data['total_stop'])
		date = recived_data['date']
		add_info = int(recived_data['add_info'])
		
		#fetching month and day
		datee = datetime.datetime.strptime(date, "%d/%m/%Y")
		month_value = datee.month
		day = datee.weekday()
		
		#predicting price using trained Model
		trained_model = joblib.load('Trained_Models/Decision_Tree_model.pkl')
		price = trained_model.predict([[aeroplane,month_value,day,source,destination,total_stop,add_info]])		

		return math.ceil(price);

# adding the defined resources along with their corresponding urls 
api.add_resource(Hello, '/')


# driver function 
if __name__ == '__main__':
    app.secret_key = os.urandom(24) 
    app.run(debug=True, host='192.168.225.26',port='3001')






