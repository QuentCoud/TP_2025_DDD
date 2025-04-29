<template>
  <div class="card">
    <h2 class="card-title">Sélectionnez votre genre musical</h2>
    <div class="search-bar">
      <select v-model="selectedGenre">
        <option disabled value="">-- Choisissez un genre --</option>
        <option v-for="genre in genres" :key="genre" :value="genre">
          {{ genre["name"] }}
        </option>
      </select>
      <button @click="search">Rechercher</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { genres } from '@/const.js' 

const selectedGenre = ref('')

const search = () => {
  if (selectedGenre.value) {
    // TODO : Implement the API call to search for country by genre
  } else {
    alert('Veuillez sélectionner un genre musical.')
  }
}
</script>

<style scoped>
.card {
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 12px;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  text-align: center;
  border: 1px solid black;
}

.card-title {
  color: rgb(0, 0, 0);
  margin-bottom: 1rem;
}

.search-bar {
  display: flex;
  gap: 1rem;
}

.search-bar select {
  flex: 1;
  padding: 0.5rem;
  border-radius: 6px;
  border: 1px solid #ccc;
  background-color: white;
  color: black;
}

.search-bar button {
  padding: 0.5rem 1rem;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 6px;
  cursor: pointer;
}

.search-bar button:hover {
  background-color: #0056b3;
}
</style>
