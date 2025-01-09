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
    return db["cinemas"]

@app.get("/cinemas/{city}", response_model=List[Cinema])
def get_cinemas_by_city(city: str):
    cinemas = [cinema for cinema in db["cinemas"] if cinema["city"].lower() == city.lower()]
    if not cinemas:
        raise HTTPException(status_code=404, detail="No cinemas found in this city.")
    return cinemas

@app.get("/movies/{cinema_id}", response_model=List[Movie])
def get_movies(cinema_id: int):
    cinema = next((cinema for cinema in db["cinemas"] if cinema["id"] == cinema_id), None)
    if not cinema:
        raise HTTPException(status_code=404, detail="Cinema not found.")
    return cinema["movies"]

@app.post("/cinemas", response_model=Cinema)
def create_cinema(cinema: Cinema):
    cinema.id = len(db["cinemas"]) + 1
    db["cinemas"].append(cinema.dict())
    return cinema

@app.post("/movies/{cinema_id}", response_model=Movie)
def add_movie(cinema_id: int, movie: Movie):
    cinema = next((cinema for cinema in db["cinemas"] if cinema["id"] == cinema_id), None)
    if not cinema:
        raise HTTPException(status_code=404, detail="Cinema not found.")
    movie.id = len(cinema["movies"]) + 1
    cinema["movies"].append(movie.dict())
    return movie
