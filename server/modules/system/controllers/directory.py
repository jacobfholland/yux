from curses.ascii import isdigit
from modules.base.controllers.base import BaseController
from modules.system.models.directory import SystemDirectory
from modules.log.models.log import log as LOG


class SystemDirectoryController(BaseController):

    def create_files(self, id):
        return SystemDirectory().create_files(id)

    def match_files(self, id):
        return SystemDirectory().match_files(id)
