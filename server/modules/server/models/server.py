from modules.app.app import db
from modules.base.models.base import Base
# from modules.library.models.library import Library


class Server(db.Model, Base):
    # FIELDS
    name = db.Column(db.String(80))
    platform_name = db.Column(db.String(80))
    platform_system = db.Column(db.String(80))
    platform_release = db.Column(db.String(80))
    platform_machine = db.Column(db.String(80))
    ip_address = db.Column(db.String(15))
    port = db.Column(db.Integer())

    # RELATIONSHIPS
    libraries = db.relationship("Library", back_populates="server", lazy=True)
