from flask import request
from flask import Flask, request, jsonify
from myenv.day3.database import *

app = Flask(__name__)

# Ensure database is ready
init_db()

# Endpoint to add a user
@app.route("/add_user", methods=["POST"])
def add_user_api():
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    user_id = add_user(name)
    return jsonify({"message": "User added", "id": user_id}), 201
 
# Endpoint to delete a user
@app.route("/delete_user", methods=["POST"])
def delete_user_api():
    data = request.get_json()
    user_id = data.get("id")
    if not user_id:
        return jsonify({"error": "ID is required"}), 400
    delete_user(user_id)
    return jsonify({"message": f"User {user_id} deleted"}), 200
 
# Endpoint to get all users
@app.route("/get_users", methods=["GET"])
def get_users_api():
    users = get_all_users()
    # Convert list of tuples to a list of dictionaries for JSON
    user_list = [{"id": u[0], "name": u[1]} for u in users]
    return jsonify(user_list), 200
 
if __name__ == "__main__":
    app.run(debug=True) 

    
#@app.route("/", methods=["GET"])

#def hi():
    #return {"message": "Hi!"}, 200

#@app.route("/newuser", methods=["POST"])
#def NewUser():

    #data = request.get_json()
    #return {"message": f"Hi, {data['name']}!"}, 200

#if __name__ == "__main__":

    #app.run(debug=True)
