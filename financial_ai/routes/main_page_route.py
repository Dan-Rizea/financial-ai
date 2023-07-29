"""main_page HTML"""
from flask import Blueprint, render_template, request
from financial_ai.handlers import retriever_handler

main_page_bp = Blueprint('documents', __name__)

@main_page_bp.route('/', methods=['POST', 'GET'])
async def render_main_page():
    """Gets documents"""
    if request.method == 'POST':
        processed_activity = await retriever_handler.retrieve_embedded_data(request.form['content'])
        return processed_activity
    else:
        return render_template('index.html')
