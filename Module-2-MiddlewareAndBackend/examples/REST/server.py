#Simple program using python flask
#HTTP post and get methods are shown below
#Post: The browser tells the server, that it wants to post data to a specified URL
#GET: Browser tells server to get data and send it

from flask import Flask, request

app = Flask(__name__)

@app.route(rule='/read_request', methods=['POST'])
def post_request():
    data = request.json
    if request.method == "POST":
        print(data)
    return "Hello from POST method"

@app.route(rule='/read_request/<id>', methods=['GET'])#data posted on browser
def get_request(id):
        print(id)
        return "Hello Folks!!!"


if __name__ == "__main__":
	app.run(host='localhost', port='4000')
