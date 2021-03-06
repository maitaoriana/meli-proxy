from bson.objectid import ObjectId

from .db import db


class PathRules(db.EmbeddedDocument):
    oid = db.ObjectIdField(required=True, default=ObjectId)
    path = db.StringField(required=True)
    max_request = db.IntField(min_value=0)
    cant_request = db.IntField(min_value=0, default=0)


class Clients(db.Document):
    ip = db.StringField(required=True, unique=True)
    max_request = db.IntField(min_value=0)
    cant_request = db.IntField(min_value=0, default=0)
    rules = db.EmbeddedDocumentListField("PathRules")
