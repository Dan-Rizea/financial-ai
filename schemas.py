from app import ma
from models import CAENCodeStore

class CAENCodeStoreSchema(ma.Schema):
    class Meta:
        fields = ('id', 'CAEN', 'name')

CAENcodestore_schema = CAENCodeStoreSchema(strict=True)