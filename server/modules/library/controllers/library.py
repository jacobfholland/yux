from modules.base.controllers.base import BaseController
from modules.library.models.library import Library


class LibraryController(BaseController):
    obj = "library"

    def get_directories(self, id):
        library = Library().get(id=id)
        if library:
            return library.directories
        else:
            return None

    def scan(self, id):
        library = Library().get(id=id)
        return library.scan()
