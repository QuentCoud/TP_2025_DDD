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
    <div v-if="searchResults.length > 0" class="results">
        <h3>Pays avec les meilleurs scores pour ce genre :</h3>
        <ul>
          <li v-for="country in searchResults" :key="country.code">
            {{ country.name }} — Score : {{ country[selectedGenre.code] ?? 'N/A' }}
          </li>
        </ul>
      </div>
  </div>
</template>

<script setup>
import { genres } from '@/const.js' 
import axios from 'axios'
import { ref } from 'vue'

const searchResults = ref([])
const selectedGenre = ref('')

const search = async () => {
  if (!selectedGenre.value) {
    alert('Veuillez sélectionner un genre musical.')
    return
  }

  try {
    const token = localStorage.getItem('access')
    const response = await axios.get(
      `http://localhost:8000/api/countries?genres=${selectedGenre.value.name}`,
      {
        headers: {
          Authorization: `Bearer ${token}`
        }
      }
    )
    searchResults.value = response.data
    console.log('Résultats de la recherche :', searchResults.value)
  } catch (error) {
    console.error('Erreur lors de la recherche de pays :', error)
    alert('Erreur lors de la recherche.')
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
