from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Sandeep Talukdar", "email": "stalukdar.2003@gmail.com"},
    {"id": 2, "name": "Mrinmoy Roy", "email": "mroy.2013@gmail.com"},
]

#Get all users
@app.route("/users",methods=["GET"])
def get_users():
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)