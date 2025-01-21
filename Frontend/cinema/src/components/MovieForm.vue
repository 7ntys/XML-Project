<template>
    <form @submit.prevent="submitForm">
      <div>
        <label for="title">Titre :</label>
        <input v-model="form.title" id="title" type="text" placeholder="Titre du film" required />
      </div>
      <div>
        <label for="duration">Durée (en minutes) :</label>
        <input v-model="form.duration" id="duration" type="number" placeholder="Durée" required />
      </div>
      <div>
        <label for="language">Langue :</label>
        <input v-model="form.language" id="language" type="text" placeholder="Langue" required />
      </div>
      <div>
        <label for="description">Description :</label>
        <textarea v-model="form.description" id="description" placeholder="Description du film"></textarea>
      </div>
      <button type="submit">Ajouter le film</button>
    </form>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'MovieForm',
    data() {
      return {
        form: {
          title: '',
          duration: '',
          language: '',
          description: '',
        },
      };
    },
    methods: {
      async submitForm() {
        try {
          await axios.post('/api/movies', this.form);
          this.$emit('movie-added');
        } catch (error) {
          console.error('Erreur lors de l\'ajout du film:', error);
        }
      },
    },
  };
  </script>
  