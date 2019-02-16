from flask import Flask, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # return "Hello, World!"
    print(request.get_json())
    jsondata = request.get_json()
    print(jsondata['test1'])
    return "hi"



if __name__ == '__main__':
    app.run(host = '0.0.0.0')
