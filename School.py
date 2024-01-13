# import add
# Importing flask.
from flask import Flask, request, jsonify

Students = [ {"name" : "Harsha" , "class" : "1st" , "Grade" : "A"},
            {"name" : "Harshith" , "class" : "2nd" , "Grade" : "B"},
            {"name" : "Uppar" , "class" : "3rd" , "Grade" : "C"}]

# Create the server
app = Flask(__name__)

# Root

@app.route("/")
def hello():
    print(" I am in hello function")
    return "<H1>Hello World</H1>"


@app.route("/api", methods=['GET', 'POST'])
def api():
    if (request.method == 'GET'):
        return (" You are getting a get request")
    elif (request.method == 'POST'):
        return jsonify("Post Request")


@app.route("/Students", methods=['GET', 'POST'])
def product():
    if (request.method == 'GET'):
        return (Students)
    elif (request.method == 'POST'):

        jsonData = request.get_json()
        print(request.get_json())
        Students.append(jsonData)
        return jsonify("new Student is added")


if (__name__ == "__main__"):
    app.run(debug=True)
