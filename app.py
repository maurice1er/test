from flask import Flask,request
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({'ip': request.remote_addr}), 200

if __name__ == '__main__':
	app.run(debug=True,port=5000)