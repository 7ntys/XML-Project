<template>
    <div>
      <h1>Ajouter un nouveau film</h1>
      <MovieForm @movie-added="handleMovieAdded" />
    </div>
  </template>
  
  <script>
  import MovieForm from '../components/MovieForm.vue';
  
  export default {
    name: 'AddMovie',
    components: {
      MovieForm,
    },
    methods: {
      handleMovieAdded() {
        alert('Film ajouté avec succès !');
        this.$router.push({ name: 'Home' });
      },
    },
  };
  </script>
  