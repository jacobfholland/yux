from server.modules.app.app import db
from server.modules.agent.models.tmdb import TMDB
from server.modules.base.models.base import Base


AGENTS = [
    {
        "name": "tmdb",
        "model": TMDB()
    }
]


class Agent(db.Model, Base):
    # FIELDS
    name = db.Column(db.String(20))
    type = db.Column(db.String(20))

    # RELATIONSHIPS
    libraries = db.relationship("Library", back_populates="agent")

    def match(self, file, library_type):
        for agent in AGENTS:
            if self.name == agent["name"]:
                return agent["model"].match(file, library_type)
        return None
