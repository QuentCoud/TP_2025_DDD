<template>
  <div class="home-view">
    <nav class="navbar">
      <div class="navbar-center">Bienvenue</div>
      <div class="navbar-icon" @click="handleClick">
        <i class="mdi mdi-cog"></i>
      </div>
    </nav>

    <div class="content">
      <p>Test</p>
    </div>
  </div>
</template>

<script setup>
const handleClick = () => {
  alert('Icône cliquée !')
}
</script>

<style scoped>
.navbar {
  position: fixed; /* fixée en haut de l'écran */
  top: 0;
  left: 0;
  right: 0;
  z-index: 10;
  width: 100vw; /* toute la largeur visible */
  display: flex;
  align-items: center;
  justify-content: center;
  height: 60px;
  background-color: #007bff;
  color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.content {
  padding: 2rem;
  padding-top: 80px; /* espace pour éviter d'être masqué par la navbar */
}

.navbar-center {
  font-size: 1.25rem;
  font-weight: bold;
}

.navbar-icon {
  position: absolute;
  right: 1rem;
  cursor: pointer;
  font-size: 1.5rem;
}

.navbar-icon:hover {
  transform: scale(1.1);
}

.content {
  padding: 2rem;
}
</style>
