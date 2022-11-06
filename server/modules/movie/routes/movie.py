from flask import Blueprint, request
from server.modules.base.utils.json import to_json
from server.modules.base.controllers.base import BaseController
from server.modules.movie.models.movie import Movie


blueprint = Blueprint('movie', __name__)
obj = "movie"
base_controller = BaseController()


@blueprint.route("/movie/create", methods=["POST"])
def create():
    return to_json(base_controller.create(obj=obj))


@blueprint.route("/movie/get", methods=["GET"])
def get():
    return to_json(base_controller.get(obj=obj, id=request.args.get("id")))


@blueprint.route("/movie/get/files", methods=["GET"])
def get_files():
    return to_json(base_controller.get(obj=obj, id=request.args.get("id")).files)


@blueprint.route("/movie/get/all", methods=["GET"])
def get_all():
    return to_json(base_controller.get_all(obj=obj))


@blueprint.route("/movie/update", methods=["PATCH"])
def update():
    return to_json(base_controller.update(obj=obj, id=request.args.get("id")))


@blueprint.route("/movie/delete", methods=["DELETE"])
def delete():
    return to_json(base_controller.delete(obj=obj, id=request.args.get("id")))


@blueprint.route("/movie/delete/all", methods=["DELETE"])
def delete_all():
    return to_json(base_controller.delete_all(obj=obj))
