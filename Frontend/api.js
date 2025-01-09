// CRUD Operations for Cinemas and Movies

const BASE_URL = "http://127.0.0.1:8000";

// Create Cinema
async function createCinema(cinemaData) {
  try {
    const response = await fetch(`${BASE_URL}/cinemas`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(cinemaData),
    });
    if (response.ok) {
      const newCinema = await response.json();
      console.log("Cinema created:", newCinema);
      return newCinema;
    } else {
      throw new Error("Failed to create cinema");
    }
  } catch (error) {
    console.error(error);
  }
}

// Read Cinemas
async function getCinemas(city = "") {
  try {
    const response = await fetch(`${BASE_URL}/cinemas/${city}`);
    if (response.ok) {
      const cinemas = await response.json();
      console.log("Cinemas:", cinemas);
      return cinemas;
    } else {
      throw new Error("Failed to fetch cinemas");
    }
  } catch (error) {
    console.error(error);
  }
}

// Create Movie for a Cinema
async function createMovie(cinemaId, movieData) {
  try {
    const response = await fetch(`${BASE_URL}/movies/${cinemaId}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(movieData),
    });
    if (response.ok) {
      const newMovie = await response.json();
      console.log("Movie created:", newMovie);
      return newMovie;
    } else {
      throw new Error("Failed to create movie");
    }
  } catch (error) {
    console.error(error);
  }
}

// Read Movies for a Cinema
async function getMovies(cinemaId) {
  try {
    const response = await fetch(`${BASE_URL}/movies/${cinemaId}`);
    if (response.ok) {
      const movies = await response.json();
      console.log("Movies:", movies);
      return movies;
    } else {
      throw new Error("Failed to fetch movies");
    }
  } catch (error) {
    console.error(error);
  }
}

/*
// Example Usage
(async () => {
  // Example Cinema Data
  const cinemaData = {
    name: "Cinéma Galaxy",
    city: "Marseille",
    address: "1 rue des Etoiles",
    movies: [],
  };

  // Example Movie Data
  const movieData = {
    title: "Les Etoiles Perdues",
    duration: 130,
    language: "Français",
    subtitles: false,
    director: "Luc Besson",
    main_actors: ["Jean Reno", "Natalie Portman"],
    age_minimum: 16,
    screenings: [
      {
        start_date: "2025-02-01",
        end_date: "2025-02-15",
        days: ["Monday", "Wednesday", "Saturday"],
        time: "20:30",
      },
    ],
  };

  // Create Cinema
  const newCinema = await createCinema(cinemaData);

  // Get Cinemas by City
  const cinemas = await getCinemas("Marseille");

  // Add Movie to a Cinema
  if (newCinema) {
    const newMovie = await createMovie(newCinema.id, movieData);

    // Get Movies for the Cinema
    const movies = await getMovies(newCinema.id);
  }
})();
*/