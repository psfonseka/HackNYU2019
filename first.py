from flask import Flask, request, jsonify
import base64


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # return "Hello, World!"
   # print(request.get_json())

    jsondata = request.get_json()
    print(jsondata['title'])
    print(len(jsondata['images']))
    test='rabbit is running on the grass'

    f = open("out.jpg", "w")
    images = jsondata['images']
    f.write(base64.decodestring(images[0]))

    return jsonify(test)



if __name__ == '__main__':
    app.run(host = '0.0.0.0')
