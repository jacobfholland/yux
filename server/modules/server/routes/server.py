from flask import Blueprint, request
from modules.base.utils.json import to_json
from modules.base.controllers.base import BaseController
from modules.server.controllers.server import ServerController
from modules.server.models.server import Server

blueprint = Blueprint('server', __name__)
obj = "server"
server_controller = ServerController()
base_controller = BaseController()


@blueprint.route("/server/create", methods=["POST"])
def create():
    return to_json(server_controller.create(obj=obj))


@blueprint.route("/server/get", methods=["GET"])
def get():
    return to_json(base_controller.get(obj=obj, id=request.args.get("id")))


@blueprint.route("/server/get/all", methods=["GET"])
def get_all():
    return to_json(base_controller.get_all(obj=obj))


@blueprint.route("/server/update", methods=["PATCH"])
def update():
    return to_json(base_controller.update(obj=obj, id=request.args.get("id")))


@blueprint.route("/server/delete", methods=["DELETE"])
def delete():
    return to_json(base_controller.delete(obj=obj, id=request.args.get("id")))


@blueprint.route("/server/delete/all", methods=["DELETE"])
def delete_all():
    return to_json(base_controller.delete_all(obj=obj))
