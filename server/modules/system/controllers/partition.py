import glob
import os
from flask import request
import psutil
from modules.base.controllers.base import BaseController
from modules.log.models.log import log as LOG


class PartitionController(BaseController):

    def get_all(self):
        partitions = psutil.disk_partitions(all=True)
        records = []
        id = 1
        for partition in partitions:
            if (
                partition[2] == "cifs" or
                partition[2] == "ntfs" or
                partition[2] == "ext3" or
                partition[2] == "ext4"
            ):
                data = {
                    "id": id,
                    "device": partition[0],
                    "mount_point": partition[1],
                    "fstype": partition[2],
                    "opts": partition[3],
                    "maxfile": partition[4],
                    "maxpath": partition[5]
                }
                records.append(data)
                id += 1

        if records is not []:
            LOG("info", "partition", "get", "success", "Partitions retrieved")
            return records
        else:
            return None

    def get_directories(self):
        if request.data and request.json:
            directories = []
            for path in glob.glob(request.json.get("path") + "/**"):
                if os.path.isdir(path):
                    if "$RECYCLE.BIN" not in path:
                        directories.append(path)
            LOG("info", "partition", "get", "success", "Directories retrieved")
            return directories
        else:
            return None
