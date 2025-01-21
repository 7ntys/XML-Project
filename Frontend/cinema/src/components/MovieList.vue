<template>
  <div>
    <h1>Films à {{ city }}</h1>
    <ul>
      <li v-for="movie in movies" :key="movie.id">
        <router-link :to="`/movies/${movie.id}`">{{ movie.title }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      city: 'Paris', // Peut être dynamique avec une barre de recherche
      movies: [],
    };
  },
  created() {
    this.fetchMovies();
  },
  methods: {
    async fetchMovies() {
      try {
        const response = await axios.get(`/api/movies?city=${this.city}`);
        this.movies = response.data;
      } catch (error) {
        console.error('Erreur lors de la récupération des films', error);
      }
    },
  },
};
</script>
