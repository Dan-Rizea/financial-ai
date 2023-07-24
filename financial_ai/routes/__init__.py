"""Initialize routes"""
from flask import Blueprint
from financial_ai.routes.economic_activities import economic_activities_bp
from financial_ai.routes.documents_route import documents_bp
from financial_ai.routes.main_page_route import main_page_bp

# Create a Blueprint for the api
api_bp = Blueprint('api', __name__)

api_bp.register_blueprint(economic_activities_bp)
api_bp.register_blueprint(documents_bp)

# Create a Blueprint for the html
html_bp = Blueprint('html', __name__)

html_bp.register_blueprint(main_page_bp)
