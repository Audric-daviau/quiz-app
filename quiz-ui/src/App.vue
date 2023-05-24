<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="app-container">
    <header>
      <div class="header-content">
        <img alt="Vue logo" class="logo" src="@/assets/Logo_One_piece.svg" width="250" height="90" />

        <nav>
          <RouterLink class="nav-link" to="/">Home</RouterLink>
          <RouterLink class="nav-link" to="/admin">Admin</RouterLink>
        </nav>
      </div>
    </header>

    <main class="app-main">
      <router-view />
    </main>
  </div>
</template>

<style scoped>
header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  line-height: 1.5;
  padding: 1rem;
  z-index: 1;
  background-color: rgba(255, 255, 255, 0); /* Set the desired background color */
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  margin-right: 1rem;
}

nav {
  display: flex;
}

nav .nav-link {
  display: inline-block;
  padding: 0.5rem 1rem;
  color: white; /* Set the text color to white */
  background-color: transparent; /* Set the desired background color */
  text-decoration: none;
  transition: background-color 0.3s ease;
  font-size: 2rem;
}

nav .nav-link:hover {
  text-decoration: underline;
}

nav a.router-link-exact-active {
  text-decoration: underline;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }

}
</style>
