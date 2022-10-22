from server.modules.log.models.log import log as LOG
import importlib


BLUEPRINTS = [
    {
        "module": "server",
        "route": "server",
    },
    {
        "module": "system",
        "route": "partition",
    },
    {
        "module": "library",
        "route": "library",
    },
    {
        "module": "system",
        "route": "directory",
    },

    {
        "module": "system",
        "route": "file",
    },

    {
        "module": "agent",
        "route": "agent",
    },
    {
        "module": "movie",
        "route": "movie",
    },
]


class Blueprints():
    url_prefix = "/api"

    def app_register_blueprint(self, app, module):
        path = f"server.modules.{module['module']}.routes.{module['route']}"
        blueprint = importlib.import_module(path)
        app.register_blueprint(
            blueprint.blueprint, url_prefix=self.url_prefix)
        LOG("info", "blueprint", "register", "success",
            f"({module['module'].capitalize()}) {module['route'].capitalize()} registered")

    def app_register_blueprints(self, app):
        for module in BLUEPRINTS:
            self.app_register_blueprint(app, module)
