from financial_ai.models.documents_model import Documents, db

async def get_all_async():
    return await Documents.query.all()

async def create_async(name, document):
    new_document = Documents(name=name, document=document)

    try:
        created_document = db.session.add(new_document)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        return {'error': 'Failed to add the document to the database.', 'details': str(e)}, 500

    return created_document


