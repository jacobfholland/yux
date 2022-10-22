from flask import Blueprint, request
from server.modules.agent.models.agent import Agent
from server.modules.base.utils.json import to_json
from server.modules.base.controllers.base import BaseController


blueprint = Blueprint('agent', __name__)
obj = "agent"
# agent_controller = AgentController()
base_controller = BaseController()


@blueprint.route("/agent/create", methods=["POST"])
def create():
    return to_json(base_controller.create(obj=obj))


@blueprint.route("/agent/get", methods=["GET"])
def get():
    return to_json(base_controller.get(obj=obj, id=request.args.get("id")))


@blueprint.route("/agent/get/all", methods=["GET"])
def get_all():
    return to_json(base_controller.get_all(obj=obj))


@blueprint.route("/agent/update", methods=["PATCH"])
def update():
    return to_json(base_controller.update(obj=obj, id=request.args.get("id")))


@blueprint.route("/agent/delete", methods=["DELETE"])
def delete():
    return to_json(base_controller.delete(obj=obj, id=request.args.get("id")))
