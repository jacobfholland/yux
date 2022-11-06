from server.modules.app.app import db
from server.modules.base.models.base import Base
from server.modules.system.models.directory import SystemDirectory
from server.modules.agent.models.agent import Agent
from server.modules.server.models.server import Server


class Library(db.Model, Base):
    # FIELDS
    name = db.Column(db.String(40))
    type = db.Column(db.String(10))
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'))
    server_id = db.Column(db.Integer, db.ForeignKey('server.id'))

    # RELATIONSHIPS
    agent = db.relationship("Agent", back_populates="libraries")
    server = db.relationship("Server", back_populates='libraries', lazy=True)
    directories = db.relationship("SystemDirectory", back_populates="library")

    def scan(self, id=False):
        if self.id:
            for directory in self.directories:
                directory.match_files()
            return directory.library

            # self.match_directories(self)
    #     elif id and id.isdigit():
    #         record = self.get(id)
    #         if record:
    #             self.match_directories(record)
    #         else:
    #             # LOG()
    #             return None
    #     else:
    #         # LOG()
    #         return None

    # def match_directories(self, record):
    #     for directory in record.directories:
    #         directory.match_files()
