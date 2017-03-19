from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route("/api/demo", methods=["GET"])
def api_demo():
    params = request.args
    name = params.get("name")

    return jsonify({'error_code': 0, "message": "User API Home", "name": name})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)