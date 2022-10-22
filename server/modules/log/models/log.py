import logging
from flask import request
from server import app


def log(
    log_level,
    obj,
    action,
    status,
    content,
):
    msg = bind_model(obj)
    msg = bind_action(msg, action)
    msg = bind_status(msg, status)
    msg = bind_object_id(msg, obj)
    msg = bind_message(msg, content)
    bind_log_level(log_level, msg)


def bind_model(obj):
    if isinstance(obj, str):
        return "[" + obj.upper() + "]"
    else:
        return "[" + type(obj).__name__.upper() + "]"


def bind_action(msg, action):
    msg += "[" + action.upper() + "]"
    return msg


def bind_status(msg, status, error=False):
    if status == "success":
        msg += "[SUCCESS]"
    elif status == "error" or status == "exception" and error:
        msg += "[ERROR]"
    elif status == "warn":
        msg += "[WARN]"
    return msg


def bind_object_id(msg, obj):
    if not isinstance(obj, str):
        if obj.id:
            msg += "(id:" + str(obj.id) + "): "
        elif request.args.get("id"):
            msg += "(id:" + str(request.args["id"]) + "): "
        else:
            msg += ": "
        return msg
    else:
        msg += ": "
        return msg


def bind_message(msg, content):
    msg += content
    return msg


def bind_log_level(log_level, msg):
    if log_level == "info":
        logging.info(msg)
    if log_level == "error":
        logging.error(msg)
    if log_level == "warn":
        logging.warn(msg)
