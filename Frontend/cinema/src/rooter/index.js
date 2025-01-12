import Vue from 'vue';
import VueRouter from 'vue-router';

import Home from '../views/Home.vue';
import CityMovies from '../views/CityMovies.vue';
import AddMovie from '../views/AddMovie.vue';
import MovieDetails from '../components/MovieDetails.vue';


Vue.use(VueRouter);

const routes = [
  { path: '/', component: Home },
  { path: '/movies/:city', component: CityMovies },
  { path: '/add-movie', component: AddMovie },
  { path: '/movies/:id', component: MovieDetails },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;