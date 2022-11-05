from flask import Blueprint
from modules.base.utils.json import to_json
from modules.base.controllers.base import BaseController
from modules.library.controllers.library import LibraryController
from modules.library.models.library import Library
from modules.system.controllers.directory import SystemDirectoryController
from flask import request


blueprint = Blueprint('library', __name__)
obj = "library"
base_controller = BaseController()
library_controller = LibraryController()


@blueprint.route("/library/create", methods=["POST"])
def create():
    return to_json(base_controller.create(obj=obj))


@blueprint.route("/library/get", methods=["GET"])
def get():
    return to_json(base_controller.get(obj=obj, id=request.args.get("id")))


@blueprint.route("/library/get/all", methods=["GET"])
def get_all():
    return to_json(base_controller.get_all(obj=obj))


@blueprint.route("/library/update", methods=["PATCH"])
def update():
    return to_json(base_controller.update(obj=obj, id=request.args.get("id")))


@blueprint.route("/library/delete", methods=["DELETE"])
def delete():
    return to_json(base_controller.delete(obj=obj, id=request.args.get("id")))


@blueprint.route("/library/delete/all", methods=["DELETE"])
def delete_all():
    return to_json(base_controller.delete_all(obj=obj))


@blueprint.route("/library/get/directories", methods=["GET"])
def add_files():
    return to_json(library_controller.get_directories(id=request.args.get("id")))


@blueprint.route("/library/scan", methods=["POST"])
def scan():
    return to_json(library_controller.scan(id=request.args.get("id")))
