from flask import Flask

uppar = Flask(__name__)

@uppar.route('/')
def welcome():
  return "Hello! , welcome"

if __name__ ==  "__main__":
 uppar.run()