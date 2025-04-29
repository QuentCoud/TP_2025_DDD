<template>
  <div class="card">
    <h2 class="card-title">Sélectionnez un pays</h2>
    <div class="search-bar">
      <select v-model="selectedCountryCode">
        <option disabled value="">-- Choisissez un pays --</option>
        <option v-for="country in countries" :key="country.code" :value="country.code">
          {{ country["name"] }}
        </option>
      </select>
      <button @click="search">Rechercher</button>
      <div v-if="searchResults.length > 0" class="results">
      <h3>Artistes trouvés :</h3>
      <ul>
        <li v-for="artist in searchResults" :key="artist.user.id">
          {{ artist.user.username }} - Genre : {{ artist.genre }}
        </li>
      </ul>
    </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { countries } from '@/const.js' 
import axios from 'axios'
const searchResults = ref([])


const selectedCountryCode = ref('')

const search = async () => {
  if (!selectedCountryCode.value) {
    alert('Veuillez sélectionner un pays.')
    return
  }

  try {
    const token = localStorage.getItem('access')
    const response = await axios.get(
      `http://localhost:8000/api/artist/search?country=${selectedCountryCode.value}`,
      {
        headers: {
          Authorization: `Bearer ${token}`
        }
      }
    )

    searchResults.value = response.data
  } catch (error) {
    console.error('Erreur lors de la recherche d’artistes :', error)
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
  box-shadow: 0 0 10px rgba(0,0,0,0.3);
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
