"""Main starting point"""
from flask import Flask
from financial_ai.routes import api_bp, html_bp
from config import Config

# Init app
app = Flask(__name__)
app.config.from_object(Config)

#app.register_blueprint(api_bp)
app.register_blueprint(html_bp)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Run server
if __name__ == '__main__':
    app.run(debug=True)
    