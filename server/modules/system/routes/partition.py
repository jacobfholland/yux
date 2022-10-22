from flask import Blueprint, request
from server.modules.base.utils.json import to_json
from server.modules.system.controllers.partition import PartitionController

blueprint = Blueprint('partition', __name__)
partition_controller = PartitionController()


@blueprint.route("/partition/get/all", methods=["GET"])
def get_all():
    return to_json(partition_controller.get_all())


@blueprint.route("/partition/get/directories", methods=["GET"])
def get_directories():
    return to_json(partition_controller.get_directories())
