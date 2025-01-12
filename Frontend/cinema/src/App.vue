<template>
  <div id="app">
    <header>
      <nav>
        <router-link :to="{ name: 'Home' }">Accueil</router-link>
        <router-link :to="{ name: 'AddMovie' }">Ajouter un Film</router-link>
      </nav>
    </header>
    <main>
      <router-view />
    </main>
    <footer>
      <p>&copy; 2025 Cinéma App</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
/* Style global */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
  color: #333;
}

header {
  background-color: #333;
  color: #fff;
  padding: 10px;
}

header nav {
  display: flex;
  justify-content: space-around;
}

header nav a {
  color: #fff;
  text-decoration: none;
  font-size: 16px;
}

header nav a:hover {
  text-decoration: underline;
}

main {
  padding: 20px;
}

footer {
  text-align: center;
  padding: 10px;
  background-color: #333;
  color: #fff;
}
</style>