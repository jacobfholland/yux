from server.modules.app.app import db
from uuid import uuid4
from datetime import datetime
from flask import request
from server.modules.log.models.log import log as LOG


class Base():
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return str(self.__dict__)

    def bind_args(self, json=False, obj=False):
        self.updated_at = datetime.now()
        if obj:
            for key in obj.__dict__:
                setattr(self, key, obj.__dict__[key])
        if json:
            for key in json:
                setattr(self, key, json.get(key))
        if request.data and request.json:
            for arg in request.json:
                setattr(self, arg, request.json.get(arg))

    def create(self, json=False, obj=False):
        self.uuid = str(uuid4())
        self.created_at = datetime.now()
        self.bind_args(json, obj)
        db.session.add(self)
        db.session.commit()
        LOG("info", self, "create", "success", "Record created")
        return self

    def delete(self, id=False):
        if self.id:
            db.session.delete(self)
            db.session.commit()
            LOG("info", self, "delete", "success", "Record deleted")
            return self
        elif id and id.isdigit():
            record = self.get(id)
            if record:
                db.session.delete(record)
                LOG("info", self, "delete", "success", "Record deleted")
                return record
            else:
                LOG("error", self, "delete", "error", "Record does not exist")
                return None
        else:
            LOG("error", self, "delete", "error", "Record does not exist")
        return None

    def delete_all(self):

        records = self.query.all()

        if len(records) > 0:
            for record in records:
                LOG("info", record, "get", "success", "Record retrieved")
                db.session.delete(record)
                db.session.commit()
                LOG("info", record, "delete", "success", "Record deleted")
                # if record.files:
                #     delattr(record, "files")
            return records
        else:
            LOG("error", self, "get", "error", "Records do not exist")
            return None

    def update(self, json=False, id=False):
        if self.id:
            self.bind_args(json)
            db.session.commit()
            LOG("info", self, "update", "success", "Record updated")
            return self
        elif id and id.isdigit():
            record = self.get(id)
            if record:
                record.update(json)
                LOG("info", self, "update", "success", "Record updated")
                return record
            else:
                LOG("error", self, "update", "error", "Record ID not valid")
                return None
        else:
            LOG("error", self, "update", "error", "Record ID not valid")
        return None

    def get(self, id=False):
        if self.id:
            return self
        elif id and id.isdigit():
            obj = self.query.filter_by(id=id).first()
            if obj is not None:
                LOG("info", self, "get", "success", "Record retrieved")
            else:
                LOG("error", self, "get", "error", "Record does not exist")
            return obj
        else:
            LOG("error", self, "get", "error", "Record ID not valid")
            return None

    def get_all(self):
        records = self.query.all()
        if len(records) > 0:
            for record in records:
                LOG("info", record, "get", "success", "Record retrieved")
            return records
        else:
            LOG("error", self, "get", "error", "Records do not exist")
            return None
