from flask import Flask, request, jsonify, 
import base64
from uuid import uuid4


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # return "Hello, World!"
   # print(request.get_json())

    jsondata = request.get_json()
    print(jsondata['title'])
    print(len(jsondata['images']))
    test='rabbit is running on the grass'

    images = jsondata['images']

    for image in images:
        f = open(str(uuid.uuid4())+".jpg", "w")
        f.write(base64.decodestring(image))

    return jsonify(test)



if __name__ == '__main__':
    app.run(host = '0.0.0.0')
