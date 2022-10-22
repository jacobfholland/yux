from server.modules.agent.models.agent import Agent
from server.modules.library.models.library import Library
from server.modules.server.models.server import Server
from server.modules.system.models.directory import SystemDirectory
from server.modules.movie.models.movie import Movie
from server.app import Application
from server.modules.system.models.file import SystemFile


class BaseController():

    def registered_models(self):
        return [
            ("server", Server()),
            ("systemdirectory", SystemDirectory()),
            ("systemfile", SystemFile()),
            ("library", Library()),
            ("movie", Movie()),
            ("agent", Agent()),
        ]

    def validate_model(self, obj):
        for model in self.registered_models():
            if model[0] == obj:
                return model[1]
        return None

    def create(self, obj, json=False):
        obj = self.validate_model(obj)
        if obj:
            return obj.create(json=json)
        else:
            return None

    def get(self, obj, id):
        obj = self.validate_model(obj)
        if obj:
            return obj.get(id=id)
        else:
            return None

    def get_all(self, obj):
        obj = self.validate_model(obj)
        if obj:
            return obj.get_all()
        else:
            return None

    def delete(self, obj, id):
        obj = self.validate_model(obj)
        if obj:
            record = obj.get(id=id)
            if record:
                return record.delete()
            else:
                return obj.delete()
        else:
            return None

    def delete_all(self, obj):
        obj = self.validate_model(obj)
        if obj:
            return obj.delete_all()
        else:
            return None

    def update(self, obj, id, json=False):
        obj = self.validate_model(obj)
        if obj:
            record = obj.get(id=id)
            if record is not None:
                return record.update(json=json)
            else:
                return obj.update(id=id)
        else:
            return None
