# Author: Lindsey Michelle Slagle
# GitHub username: Lswaggerty
# Date: 11/26/2024
# Description: Cataloging data for movies and streaming services

class Movie:
    """Represent a movie with title, genre, director, and year."""

    def __init__(self, title, genre, director, year):
        """Initialize Movie with title, genre, director, and year."""
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """Return the movie title."""
        return self._title

    def get_genre(self):
        """Return the movie genre."""
        return self._genre

    def get_director(self):
        """Return the movie director."""
        return self._director

    def get_year(self):
        """Return the movie year."""
        return self._year


class StreamingService:
    """Represent a streaming service with a name and a catalog of movies."""

    def __init__(self, name):
        """Initialize StreamingService with a name and an empty catalog."""
        self._name = name
        self._catalog = {}

    def get_name(self):
        """Return the streaming service name."""
        return self._name

    def get_catalog(self):
        """Return the movie catalog."""
        return self._catalog

    def add_movie(self, movie):
        """Add a Movie object to the catalog."""
        self._catalog[movie.get_title()] = movie

    def delete_movie(self, title):
        """Delete a movie from the catalog by its title."""
        if title in self._catalog:
            del self._catalog[title]


class StreamingGuide:
    """Represent a guide containing multiple streaming services."""

    def __init__(self):
        """Initialize StreamingGuide with an empty list of streaming services."""
        self._streaming_services = []

    def add_streaming_service(self, streaming_service):
        """Add a StreamingService object to the guide."""
        self._streaming_services.append(streaming_service)

    def delete_streaming_service(self, name):
        """Delete a streaming service by its name."""
        self._streaming_services = [
            service for service in self._streaming_services if service.get_name() != name
        ]

    def where_to_watch(self, title):
        """Return a list of where to watch a movie."""
        result = []
        for service in self._streaming_services:
            catalog = service.get_catalog()
            if title in catalog:
                movie = catalog[title]
                if not result:
                    result.append(f"{movie.get_title()} ({movie.get_year()})")
                result.append(service.get_name())
        return result if result else None
