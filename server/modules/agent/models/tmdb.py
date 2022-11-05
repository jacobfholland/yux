from requests import JSONDecodeError
from config.config import Config
import tmdbsimple as tmdb
from modules.movie.models.movie import Movie
from modules.log.models.log import log as LOG


class TMDB():

    def __init__(self) -> None:
        tmdb.API_KEY = Config.TMDB_KEY
        self.id = "tmdb"
        super().__init__()

    def search(self, file, library_type):
        if file.title():
            if library_type == "movie":
                search = self.execute_search_movie(file)
            else:
                search = None
            if search and search.get("results"):
                LOG("info", self, "query", "success",
                    f"Results retrieved for {file.file_name}")
                return search.get("results")
            else:
                LOG("error", "agent", "query", "error",
                    f"Results not found for {file.file_name} (title: {file.title()})")
                return None
        else:
            return None

    def sort_results(self, results, key):
        return sorted(results, key=lambda x: x[key])

    def execute_search_movie(self, file):
        try:
            search = tmdb.Search().movie(
                query=file.title(),
                year=file.year()
            )
            if not search["results"]:
                search = tmdb.Search().movie(
                    query=file.title()
                )
            return search
        except:
            search = None

    def match(self, file, library_type):
        if file.type == "video":
            results = self.search(file, library_type=library_type)
            if results:
                # TODO Do a Title similarity comparison. Meet 80% threshold or more
                if library_type == "movie":
                    return self.match_movie(file, results)
                elif library_type == "episode":
                    return self.match_episode(file, results)
                else:
                    return None
            else:
                LOG("error", self, "match", "error",
                    f"Match not found for {file.title()} ({file.type})")
                return None
        else:
            return None

    def match_episode(self, file, results):
        return None

    def match_movie(self, file, results):
        match = results[0]
        LOG("info", self, "match", "success",
            f"Match found for {file.title()} ({file.type})")
        try:
            match = tmdb.Movies(match["id"]).info()
        except:
            return None
        existing = Movie.query.filter_by(id=match["id"]).first()
        match["sort_title"] = self.sort_title(match)
        match["year"] = self.year(match)
        if not existing:
            record = Movie().create(json=match)
        else:
            record = existing
            record.update(json=match)
        if not file.movie_id:
            json = {"movie_id": match["id"]}
            file.update(json=json)
        return record

    def sort_title(self, match):
        if match.get("title"):
            if match.get("title").split(" ")[0] == "The":
                sort_title = match.get("title").replace("The ", "")
            else:
                sort_title = match.get("title")
            return sort_title
        else:
            return None

    def year(self, match):
        if match["release_date"]:
            year = match["release_date"].split("-")[0]
            return int(year)
        else:
            return None
