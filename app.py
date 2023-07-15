from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config
from economic_activities_logic import process_economic_activities


# Init app
app = Flask(__name__)
# Map route
@app.route('/', methods=['GET'])
async def get():
    jsonData = request.get_json()
    result = await process_economic_activities.get_economic_category(jsonData.get('prompt'))
    return jsonify({"output": result})


# Init database
app.config.from_object(Config)
db = SQLAlchemy(app)
# Init Marshmallow
ma = Marshmallow(app)


# Get an economic activity
@app.route('/agent', methods=['GET'])
async def get_codes(prompt):
    name = request.json['name']


# Run server
if __name__ == '__main__':
    app.run(debug=True)