from server.modules.base.controllers.base import BaseController
from flask import current_app


class ServerController(BaseController):

    def create(self, obj, json=False):
        json = {
            "platform_name": current_app.config["IP_ADDRESS"],
            "platform_system": current_app.config["PLATFORM_SYSTEM"],
            "platform_release": current_app.config["PLATFORM_RELEASE"],
            "platform_machine": current_app.config["PLATFORM_MACHINE"],
            "ip_address": current_app.config["IP_ADDRESS"],
            "port": current_app.config["PORT"]
        }
        return super().create(obj, json)
