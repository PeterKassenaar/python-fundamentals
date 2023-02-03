# example creating a Python Flask API
# Credits: https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24

# save this as app.py in a new directory if you want to create a standalone app.
from flask import Flask
from flask import jsonify

app = Flask(__name__)  # create an instance of the Flask class

# Simple routes
# We use the route() decorator to tell Flask what URL should trigger our function.


@app.route("/hello")
def hello():
    return "Hello, World !"


@app.route('/about')
def about():
    return "About this app..."

# Using parameters in a route
@app.route('/users/<string:name>/<int:number>')
def users(name: str, number: int):    
    response = 'Your name is {0}, and your number is {1}'.format(
        name.capitalize(),
        number)
    return (response)

# Return JSON Serializable Output.
# The return value from a function in a Flask app should be JSON serializable. 
# You can use jsonify to make your output JSON serializable. 

@app.route('/person/<string:name>')
def person(name:str):
    jsonObj = {
        "name": name.capitalize(),
        "address": "Netherlands"
    }
    return jsonify(jsonObj)


# You can also use jsonify to automatically serialize lists 
# and tuples to JSON Response.
@app.route('/numbers')
def numbers():
    numbers = []
    for i in range (10, 15):
        numbers.append((i,i))
    return jsonify(numbers)

# Before Request:
# You can specify a function which should always execute before
# the request is processed by using app.before_request decorator.
# This is particularly useful when you want to log
# the requests for monitoring purposes.
@app.before_request
def before():
    print("This is executed BEFORE each request.")

# Accessing Request Data
# To access the request data, use the following
from flask import request

@app.route('/req')
def req():
    data = request.args # get arguments from the querystring
    return data

@app.route('/json')
def jsonFn():
    data = request.json # get json data from body and return
    return data

# To look at:Blueprints.
# Blueprints allow us to separate various endpoints into subdomains
# https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24

# *******************************
if __name__ == '__main__':
    # app.run()  # run our Flask app, for options see https://flask.palletsprojects.com/en/2.2.x/api/#flask.Flask.run
    app.run(debug=True, host='0.0.0.0', port=3333)  # run our Flask app
