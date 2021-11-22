from .db import db


class Clients(db.Document):
    ip = db.StringField(required=True, unique=True)
    max_request = db.IntField(min_value=-1)
    cant_request = db.IntField(min_value=0, default=0)
