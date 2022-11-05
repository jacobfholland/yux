from flask import Blueprint, request
from modules.base.utils.json import to_json
from modules.base.controllers.base import BaseController
from modules.system.controllers.file import FileController
from modules.system.models.file import SystemFile


blueprint = Blueprint('system_file', __name__)
obj = "systemfile"
base_controller = BaseController()
file_controller = FileController()


@blueprint.route("/system/file/create", methods=["POST"])
def create():
    return to_json(base_controller.create(obj=obj))


@blueprint.route("/system/file/get", methods=["GET"])
def get():
    return to_json(base_controller.get(obj=obj, id=request.args.get("id")))


@blueprint.route("/system/file/get/all", methods=["GET"])
def get_all():
    return to_json(base_controller.get_all(obj=obj))


@blueprint.route("/system/file/update", methods=["PATCH"])
def update():
    return to_json(base_controller.update(obj=obj, id=request.args.get("id")))


@ blueprint.route("/system/file/delete", methods=["DELETE"])
def delete():
    return to_json(base_controller.delete(obj=obj, id=request.args.get("id")))


@blueprint.route("/system/file/delete/all", methods=["DELETE"])
def delete_all():
    return to_json(base_controller.delete_all(obj=obj))


@blueprint.route("/system/file/match", methods=["POST"])
def match():
    return to_json(file_controller.match(id=request.args.get("id")))


@blueprint.route("/system/file/info", methods=["GET"])
def info():
    return to_json(file_controller.info(id=request.args.get("id")))
