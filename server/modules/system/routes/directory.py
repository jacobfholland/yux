from flask import Blueprint
from server.modules.base.utils.json import to_json
from server.modules.base.controllers.base import BaseController
from server.modules.system.controllers.directory import SystemDirectoryController
from flask import request
from server.modules.system.models.directory import SystemDirectory


blueprint = Blueprint('system_directory', __name__)
obj = "systemdirectory"
base_controller = BaseController()
system_directory_controller = SystemDirectoryController()


@blueprint.route("/system/directory/create", methods=["POST"])
def create():
    return to_json(base_controller.create(obj=obj))


@blueprint.route("/system/directory/get", methods=["GET"])
def get():
    return to_json(base_controller.get(obj=obj, id=request.args.get("id")))


@blueprint.route("/system/directory/get/all", methods=["GET"])
def get_all():
    return to_json(base_controller.get_all(obj=obj))


@blueprint.route("/system/directory/get/files", methods=["GET"])
def get_files():
    return to_json(system_directory_controller.get(obj=obj, id=request.args.get("id")).files)


@blueprint.route("/system/directory/files/create", methods=["POST", "GET"])
def create_files():
    return to_json(system_directory_controller.create_files(id=request.args.get("id")))


@blueprint.route("/system/directory/files/match", methods=["POST", "GET"])
def match_files():
    return to_json(system_directory_controller.match_files(id=request.args.get("id")))


@blueprint.route("/system/directory/update", methods=["PATCH"])
def update():
    return to_json(base_controller.update(obj=obj, id=request.args.get("id")))


@blueprint.route("/system/directory/delete", methods=["DELETE"])
def delete():
    return to_json(base_controller.delete(obj=obj, id=request.args.get("id")))


@blueprint.route("/system/directory/delete/all", methods=["DELETE"])
def delete_all():
    return to_json(base_controller.delete_all(obj=obj))
