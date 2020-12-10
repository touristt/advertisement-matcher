from flask import Flask, request, jsonify, render_template
import json 
from flask_cors import CORS
from cosine_similarity import get_matches 

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET','POST'])
def getfunc(): 
	if request.method == "GET":
		return render_template('index.html')
	datum = request.get_json()
	return get_matches(datum["ads"], datum["user"])
 
if __name__ == '__main__':
		app.debug = True
		app.run(host="0.0.0.0", port=5000) 