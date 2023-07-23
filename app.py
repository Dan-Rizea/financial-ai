"""Main starting point"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from financial_ai.routes import routes_bp
from flask_migrate import Migrate
from config import Config

# Init app
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(routes_bp)

# Run server
if __name__ == '__main__':
    app.run(debug=True)
    