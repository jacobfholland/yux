from datetime import datetime
import json


def serialize(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return {k: v for k, v in obj.__dict__.items() if not k.startswith('_')}


def to_json(obj):
    json_str = json.dumps(obj, default=serialize)
    return json_str


def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__,
                      sort_keys=True, indent=4)
