<template>
    <div>
      <h1>Bienvenue sur le site des cinémas parisiens</h1>
      <p>Recherchez les films dans votre ville ou ajoutez un nouveau film.</p>
      <router-link :to="{ name: 'AddMovie' }">Ajouter un film</router-link>
      <router-link :to="{ name: 'CityMovies', params: { city: 'Paris' } }">Voir les films à Paris</router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Home',
  };
  </script>