# example creating a Python Flask API

# save this as app.py
from flask import Flask
# from flask_restful import Resource, Api, reqparse # pip install flask_restful

app = Flask(__name__) # create an instance of the Flask class
# api = Api(app)

# class Users(Resource):
#     # methods go here
#     def get(self):
#         # data = pd.read_csv('users.csv')  # read CSV
#         # data = data.to_dict()  # convert dataframe to dictionary
#         return {'data': 'Hello Users 456'}, 200  # return data and 200 OK code

# class Locations(Resource):
#     # methods go here
#     pass

# api.add_resource(Users, '/users')  # '/users' is our entry point
# api.add_resource(Locations, '/locations')  # '/locations' is our entry point

# We use the route() decorator to tell Flask what URL should trigger our function.
@app.route("/")
def hello():
    return "Hello, World !"

if __name__ == '__main__':
    app.run(debug=True)  # run our Flask app