<template>
    <div>
      <h1>Détails du film</h1>
      <div v-if="isLoading">Chargement des détails...</div>
      <div v-else-if="movie">
        <p><strong>Titre :</strong> {{ movie.title }}</p>
        <p><strong>Durée :</strong> {{ movie.duration }} minutes</p>
        <p><strong>Langue :</strong> {{ movie.language }}</p>
        <p><strong>Description :</strong> {{ movie.description }}</p>
      </div>
      <div v-else>
        <p>Film introuvable.</p>
      </div>
      <router-link to="/">Retour à l'accueil</router-link>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'MovieDetails',
    data() {
      return {
        isLoading: true, // Indicateur de chargement
        movie: null, // Détails du film
      };
    },
    created() {
      this.fetchMovieDetails();
    },
    methods: {
      async fetchMovieDetails() {
        try {
          // Récupère l'ID du film depuis les paramètres de la route
          const movieId = this.$route.params.id;
  
          // Requête pour récupérer les détails du film
          const response = await axios.get(`/api/movies/${movieId}`);
          this.movie = response.data;
        } catch (error) {
          console.error('Erreur lors de la récupération des détails du film :', error);
        } finally {
          this.isLoading = false; // Fin du chargement
        }
      },
    },
  };
  </script>
  