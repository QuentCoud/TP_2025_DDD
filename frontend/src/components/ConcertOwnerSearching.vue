<template>
  <div class="card">
    <h2 class="card-title">Sélectionnez un pays</h2>
    <div class="search-bar">
      <select v-model="selectedCountryCode">
        <option disabled value="">-- Choisissez un pays --</option>
        <option v-for="country in countries" :key="country.code" :value="country.code">
          {{ country.name }}
        </option>
      </select>
      <button @click="search">Rechercher</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const countries = [
  { code: 'FR', name: 'France' },
  { code: 'DE', name: 'Allemagne' },
  { code: 'IT', name: 'Italie' },
  { code: 'ES', name: 'Espagne' },
  { code: 'BE', name: 'Belgique' },
  { code: 'NL', name: 'Pays-Bas' },
  { code: 'PT', name: 'Portugal' },
  { code: 'SE', name: 'Suède' },
  { code: 'FI', name: 'Finlande' },
  { code: 'PL', name: 'Pologne' },
  { code: 'CZ', name: 'République tchèque' },
  { code: 'AT', name: 'Autriche' },
  { code: 'GR', name: 'Grèce' },
  { code: 'IE', name: 'Irlande' },
  { code: 'DK', name: 'Danemark' },
  { code: 'HU', name: 'Hongrie' },
  { code: 'RO', name: 'Roumanie' },
  { code: 'BG', name: 'Bulgarie' },
  { code: 'SK', name: 'Slovaquie' },
  { code: 'SI', name: 'Slovénie' },
  { code: 'HR', name: 'Croatie' },
  { code: 'EE', name: 'Estonie' },
  { code: 'LV', name: 'Lettonie' },
  { code: 'LT', name: 'Lituanie' },
  { code: 'LU', name: 'Luxembourg' },
  { code: 'CY', name: 'Chypre' },
  { code: 'MT', name: 'Malte' }
]

const selectedCountryCode = ref('')

const search = () => {
  if (selectedCountryCode.value) {
    alert(`Code pays sélectionné : ${selectedCountryCode.value}`)
  } else {
    alert('Veuillez sélectionner un pays.')
  }
}
</script>

<style scoped>
.card {
  background-color: #1e1e1e;
  padding: 2rem;
  border-radius: 12px;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 0 10px rgba(0,0,0,0.3);
  text-align: center;
}

.card-title {
  color: white;
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
