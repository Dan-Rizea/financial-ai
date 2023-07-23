"""documents API"""
from flask import Blueprint, request, jsonify
from financial_ai.handlers import documents_handler

documents_bp = Blueprint('documents', __name__)

@documents_bp.route('/documents', methods=['GET'])
async def get_documents():
    """Gets documents"""
    result = await documents_handler.get_all_documents()
    return jsonify({result})

@documents_bp.route("/documents", methods=['POST'])
async def post_document():    
    """Posts a document"""
    json_data = request.get_json()

    name = json_data.get('name')
    document = json_data.get('document')

    result = await documents_handler.create_async(name, document)
    return jsonify(result)
