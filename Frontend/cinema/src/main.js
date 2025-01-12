import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')

import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:8081'; // Adresse de l'API