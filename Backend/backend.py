from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
app = FastAPI()

# Mock database (JSON structure in memory)
# Charger la base de données depuis un fichier JSON
def load_db():
    with open("../BDD/db.json", "r") as file:
        return json.load(file)

# Sauvegarder les modifications dans le fichier JSON
def save_db(data):
    with open("../BDD/db.json", "w") as file:
        json.dump(data, file, indent=4)

# Charger la base au démarrage
db = load_db()
# Pydantic models
class Screening(BaseModel):
    start_date: str
    end_date: str
    days: List[str]
    time: str

class Movie(BaseModel):
    id: Optional[int]
    title: str
    duration: int
    language: str
    subtitles: bool
    director: str
    main_actors: List[str]
    age_minimum: int
    screenings: List[Screening]

class Cinema(BaseModel):
    id: Optional[int]
    name: str
    city: str
    address: str
    movies: List[Movie]

# API endpoints

@app.get("/cinemas", response_model=List[Cinema])
def get_cinemas():
    # Fetches the list of all cinemas from the database.
    # Use case: Display all cinemas regardless of city.
    return db["cinemas"]

@app.get("/cinemas/{city}", response_model=List[Cinema])
def get_cinemas_by_city(city: str):
    # Fetches cinemas located in a specific city.
    # Use case: User searches for cinemas in their city (e.g., "Paris").
    cinemas = [cinema for cinema in db["cinemas"] if cinema["city"].lower() == city.lower()]
    if not cinemas:
        raise HTTPException(status_code=404, detail="No cinemas found in this city.")
    return cinemas

@app.get("/movies/{cinema_id}", response_model=List[Movie])
def get_movies(cinema_id: int):
    # Fetches all movies for a specific cinema by its ID.
    # Use case: Display the list of movies available in a selected cinema.
    cinema = next((cinema for cinema in db["cinemas"] if cinema["id"] == cinema_id), None)
    if not cinema:
        raise HTTPException(status_code=404, detail="Cinema not found.")
    return cinema["movies"]

@app.post("/cinemas", response_model=Cinema)
def create_cinema(cinema: Cinema):
    # Adds a new cinema to the database.
    # Use case: A cinema owner registers their cinema with the platform.
    cinema.id = len(db["cinemas"]) + 1
    db["cinemas"].append(cinema.dict())
    return cinema

@app.post("/movies/{cinema_id}", response_model=Movie)
def add_movie(cinema_id: int, movie: Movie):
    # Adds a new movie to a specific cinema by its ID.
    # Use case: A cinema owner adds a new movie to their cinema's schedule.
    cinema = next((cinema for cinema in db["cinemas"] if cinema["id"] == cinema_id), None)
    if not cinema:
        raise HTTPException(status_code=404, detail="Cinema not found.")
    movie.id = len(cinema["movies"]) + 1
    cinema["movies"].append(movie.dict())
    return movie

@app.put("/movies/{cinema_id}/{movie_id}", response_model=Movie)
def update_movie(cinema_id: int, movie_id: int, updated_movie: Movie):
    # Updates the details of an existing movie in a specific cinema by its ID.
    # Use case: A cinema owner updates information about a movie, such as its schedule or details.
    cinema = next((cinema for cinema in db["cinemas"] if cinema["id"] == cinema_id), None)
    if not cinema:
        raise HTTPException(status_code=404, detail="Cinema not found.")
    movie = next((movie for movie in cinema["movies"] if movie["id"] == movie_id), None)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found.")

    # Update movie details
    movie.update(updated_movie.dict())
    return movie