from server.modules.app.app import db
from server.modules.base.models.base import Base


class Movie(db.Model, Base):
    adult = db.Column(db.Boolean(), default=False)
    backdrop_path = db.Column(db.String(32))
    budget = db.Column(db.BigInteger)
    homepage = db.Column(db.String(255))
    imdb_id = db.Column(db.String(15))
    original_language = db.Column(db.String(2))
    original_title = db.Column(db.String(255))
    overview = db.Column(db.String())
    popularity = db.Column(db.Float)
    poster_path = db.Column(db.String(32))
    release_date = db.Column(db.DateTime)
    revenue = db.Column(db.BigInteger)
    runtime = db.Column(db.Integer)
    status = db.Column(db.String(32))
    tagline = db.Column(db.String())
    title = db.Column(db.String(255))
    sort_title = db.Column(db.String(255))
    year = db.Column(db.Integer)
    vote_average = db.Column(db.Float)
    vote_count = db.Column(db.Integer)

    files = db.relationship(
        "SystemFile", back_populates="movie", lazy=True)
