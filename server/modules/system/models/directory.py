import glob
import os
from modules.log.models.log import log as LOG
from modules.app.app import db
from modules.base.models.base import Base
from modules.system.models.file import SystemFile

EXTENSIONS = {
    "video": ["mkv"],
    "subtitle": ["srt"],
    "audio": ["mp3"],
    "image": ["png", "jpg"]
}


class SystemDirectory(db.Model, Base):
    # FIELDS
    path = db.Column(db.String(4315))
    library_id = db.Column(db.Integer, db.ForeignKey('library.id'))

    # RELATIONSHIPS
    library = db.relationship("Library", back_populates="directories")
    files = db.relationship("SystemFile", back_populates="directory")

    def raw_files(self):
        files = []
        for path in glob.glob(self.path + "/**", recursive=True):
            if os.path.isfile(path) and "$RECYCLE.BIN" not in path:
                files.append(path)
        return files

    def get_type(self, path):
        extension = path.split(".")[-1]
        if "$RECYCLE.BIN" not in path:
            if extension in EXTENSIONS["video"]:
                type = "video"
            elif extension in EXTENSIONS["subtitle"]:
                type = "subtitle"
            elif extension in EXTENSIONS["audio"]:
                type = "audio"
            elif extension in EXTENSIONS["image"]:
                type = "image"
            else:
                return None
            return type
        else:
            return None

    def get_files(self):
        files = []
        for path in self.raw_files():
            file_name = path.split("/")[-1]
            type = self.get_type(path)
            if type and file_name and path:
                file = {
                    "path": path,
                    "file_name": file_name,
                    "type": type,
                    "directory_id": self.id,
                    "extension": path.split(".")[-1],
                }
                files.append(file)
        return files

    def create_files(self, id=False):
        if self.id:
            files = self.get_files()
        elif id and id.isdigit():
            record = self.get(id)
            if record:
                files = record.get_files()
            else:
                LOG("error", self, "createfiles",
                    "error", "Record does not exist")
                files = None
        else:
            files = None
            LOG("error", self, "createfiles", "error", "Record ID not valid")

        if files:
            for file in files:
                existing = SystemFile.query.filter_by(
                    path=file["path"]).first()
                if not existing:
                    file = SystemFile().create(json=file)
                # else:
                #     file = existing.update(json=file)
            LOG("info", self, "createfiles", "success",
                "Files created successfully")
            if self.id:
                return self.files
            elif self.get(id):
                return self.get(id).files
            else:
                return None
        else:
            LOG("error", self, "createfiles", "error",
                "File records do not exist")
        return None

    def match_files(self, id=False):
        if self.id:
            agent = self.library.agent
            if not self.files:
                self.create_files(self.id)
            for file in self.files:
                agent.match(file, library_type=self.library.type)
            return self.files
        elif id and id.isdigit():
            record = self.get(id)
            if record:
                return self.iterate_files(record)
            else:
                LOG("error", self, "match", "error", "Record does not exist")
                return None
        else:
            LOG("error", self, "match", "error", "Record ID not valid")
        return None

    def iterate_files(self, record):
        agent = record.library.agent
        if not record.files:
            record.create_files(record.id)
        for file in record.files:
            agent.match(file, library_type=record.library.type)
        return record.files
