from financial_ai.repositories.documents_repository import get_all_async, create_async

async def get_all_documents():
    """Get all documents"""
    try:
        all_documents = await get_all_async()
        documents_data = [
            {'id': doc.id, 'name': doc.name, 'document': doc.document}
            for doc in all_documents
        ]

        return documents_data, 200

    except Exception as e:
        return {'error': 'Failed to fetch documents from the database.', 'details': str(e)}, 500

async def post_document(name, document):
    """Upload a document"""

    if not name or not document:
        return{'error': 'Title and content are required fields.'}, 400

    return await create_async(name=name, document=document), 201

