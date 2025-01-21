<template>
    <div>
      <h1>Films dans la ville : {{ city }}</h1>
      <MovieList :movies="movies" />
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import MovieList from '../components/MovieList.vue';
  
  export default {
    name: 'CityMovies',
    components: {
      MovieList,
    },
    data() {
      return {
        city: this.$route.params.city,
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
          console.error('Erreur lors de la récupération des films:', error);
        }
      },
    },
  };
  </script>