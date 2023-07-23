"""Initialize routes"""
from flask import Blueprint
from financial_ai.routes.economic_activities import economic_activities_bp
from financial_ai.routes.documents_route import documents_bp

# Create a Blueprint for the routes
routes_bp = Blueprint('routes', __name__)

routes_bp.register_blueprint(economic_activities_bp)
routes_bp.register_blueprint(documents_bp)
