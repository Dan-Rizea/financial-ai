"""economic-activities API"""
from flask import Blueprint, request, jsonify
from financial_ai.handlers import process_economic_activities, import_chunk_pdfs

economic_activities_bp = Blueprint('economic_activities', __name__)

@economic_activities_bp.route('/economic-activities', methods=['GET'])
async def get_economic_activities():
    """Gets economic activities"""
    json_data = request.get_json()
    result = await process_economic_activities.get_economic_category(json_data.get('prompt'))
    return jsonify({"output": result})

@economic_activities_bp.route("/economic-activities/embeddings", methods=['GET'])
async def get_embeddings():    
    """Embeds and gets CAEN codes VERY INEFFICIENT"""
    json_data = request.get_json()
    result = await import_chunk_pdfs.embed_search_pdf(json_data.get('prompt'))
    return jsonify({"output": result})
