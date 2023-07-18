"""Main starting point"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from financial_ai.routes import routes_bp
from config import Config

# Init app
app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)

app.register_blueprint(routes_bp)

# Run server
if __name__ == '__main__':
    app.run(debug=True)
    