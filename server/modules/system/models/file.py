from modules.app.app import db
from modules.base.models.base import Base
import ffmpeg
from modules.movie.models.movie import Movie


class SystemFile(db.Model, Base):
    # FIELDS
    path = db.Column(db.String(4351))
    file_name = db.Column(db.String(255))
    type = db.Column(db.String(10))
    extension = db.Column(db.String(4))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    directory_id = db.Column(db.Integer, db.ForeignKey('system_directory.id'))

    # RELATIONSHIPS
    movie = db.relationship('Movie', back_populates='files', lazy=True)
    directory = db.relationship("SystemDirectory", back_populates="files")

    def info(self):
        try:
            return ffmpeg.probe(self.path)
        except ffmpeg.Error as e:
            return e.stderr

    def split_name(self):
        self.file_name = self.file_name.replace("-", ".")
        self.file_name = self.file_name.replace(" ", ".")
        self.file_name = self.file_name.replace("(", "")
        self.file_name = self.file_name.replace(")", "")
        self.file_name = self.file_name.replace("[", "")
        self.file_name = self.file_name.replace("]", "")
        return self.file_name.split(".")

    def core_delimiter(self):
        if self.year():
            return str(self.year())
        elif self.resolution():
            return self.resolution()
        elif self.source():
            return self.source()
        if self.encode():
            return self.encode()
        else:
            return None

    def title(self):
        core_delimiter = self.core_delimiter()
        if core_delimiter:
            core_delimiter_index = self.split_name().index(core_delimiter)
            title = self.split_name()[:core_delimiter_index]
            title = " ".join(title)
            return title
        else:
            return None

    def year(self):
        years = []
        for chunk in self.split_name():
            if chunk.isdigit() and len(chunk) == 4:
                if chunk not in [
                    "240", "360", "480", "576", "720", "1080", "4k"
                ]:
                    years.append(chunk)
        if years:
            return int(years[-1])
        else:
            return None

    def resolution(self):
        resolutions = []
        for chunk in self.split_name():
            replaced_chunk = chunk.lower()
            replaced_chunk = replaced_chunk.replace("p", "").replace("i", "")
            if replaced_chunk.isdigit() and replaced_chunk in [
                "240", "360", "480", "576", "720", "1080", "4k"
            ]:
                resolutions.append(chunk)
        if resolutions:
            return resolutions[-1]
        else:
            return None

    def source(self):
        sources = []
        for chunk in self.split_name():
            if "web" in chunk.lower():
                sources.append(chunk)
            elif "bluray" in chunk.lower() or chunk.lower() == "blu":
                sources.append(chunk)
            elif "dvd" in chunk.lower():
                sources.append(chunk)
            elif "tv" in chunk.lower():
                sources.append(chunk)
            elif "vhs" in chunk.lower():
                sources.append(chunk)
        if sources:
            return sources[-1]
        else:
            return None

    def encode(self):
        split_name = self.split_name()
        for chunk in split_name:
            if "264" in chunk.lower() or "265" in chunk.lower():
                index = split_name.index(chunk)
                if split_name[index - 1] == "h":
                    return split_name[index - 1]
                return chunk
            elif "xvid" in chunk.lower():
                return chunk
            elif "divx" in chunk.lower():
                return chunk
