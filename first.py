from flask import Flask, request, jsonify
import requests
import base64
import json
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
        f = open(str(uuid4())+".jpg", "w")
        f.write(base64.decodestring(image))

    return jsonify(test)

@app.route('/dictionary', methods=['POST'])
def dictionary():

    app_id = 'b1d811e1'
    app_key = '0ac04920ba47c94716d7acda7781a534'

    language = 'en'

    jsondata = request.get_json()
    word_id = jsondata['word']

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

    print("code {}\n".format(r.status_code))
    #print("text \n" + r.text)
    #print(json.loads(r.text))
    json_data  = json.loads(r.text)
    json_results = json_data['results']
    json_lex = json_results[0]['lexicalEntries'][0]
    json_speech = json_lex['lexicalCategory']
    json_entry = json_lex['entries'][0]['senses'][0]
    json_def = json_entry['definitions'][0]
    #json_example = json_entry['examples']
    #return jsonify(json_entry)
    print({'Speech': json_speech, 'Definitions': json_def})
    return jsonify({'Speech': json_speech, 'Definitions': json_def})


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = '4000')
    #app.run(debug=True)
