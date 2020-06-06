from flask import Flask, jsonify, abort
from flask import make_response,request
import json
import timestamp

app = Flask(__name__)

Providers = [
                {
                "providerId": 12345 ,
                "data": [ {"name": "Ciroma Adeyemi",
                             "age" : 20,
                            "timestamp" : 1587614026 },
                            {"name":"Samuel Chukwu",
                             "age" : 25,
                             "timestamp": 1587614729 }]
                }
            ]


@app.route('/user/api/', methods=['GET'])
def on_get():
    return jsonify({
                    "status" : 200,
                    "message": {"providers": Providers}
                    }),200

''' Data can be created here specifically with strings,integer and timestamps '''

@app.route('/user/api/create', methods=['POST'])
def on_create():
    provider = {  "name":  request.get_json()['name'],
                  "age" :  request.get_json()['age'],
                  "timestamp" : timestamp()
                }
    print(provider)
    if type(provider['name']) != str or type(provider['age']) != int:
        return jsonify({ "status": 300,
                         "message": "Enter a valid data type"}),300
    Providers[0]['data'].append(provider)
    print(Providers)
    return jsonify({ "status": 201,
                     "message": "added successful",
                     "data":Providers
                     }), 201


@app.route('/user/api/filter/<providerId>', methods=['POST'])
def search(providerId):
        providerId = providerId
        name = request.args.get('name')
        age = request.args.get('age')
        ts = request.args.get('timestamp')

        nameRule = name.split(":")[0]
        nameValue = name.split(":")[1]
#     return jsonify({"status" : 200,"message" : "search found"})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({
        "status": 404,
        "error": "Not found"}), 404)




if __name__ == "__main__":
    app.run(debug=True)