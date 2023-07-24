"""Main starting point"""
from flask import Flask
from financial_ai.routes import routes_bp
from config import Config

# Init app
app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(routes_bp)

# Run server
if __name__ == '__main__':
    app.run(debug=True)
    