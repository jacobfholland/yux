from modules.agent.models.tmdb import TMDB
from modules.base.controllers.base import BaseController
from modules.system.models.file import SystemFile


class FileController(BaseController):

    def match(self, id):
        file = SystemFile().get(id)
        if file:
            agent = file.directory.library.agent
            agent.match(file, library_type=file.directory.library.type)
            delattr(file, "directory")
            return file
        else:
            return None

    def info(self, id):
        file = SystemFile().get(id)
        if file:
            return file.info()
        else:
            return None
