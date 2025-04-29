<template>
  <div class="home-view">
    <nav class="navbar">
      <div class="navbar-center">Profile</div>
      <div class="navbar-icon" @click="toggleMenu">
        <i class="mdi mdi-cog"></i>
        <div v-if="showMenu" class="dropdown-menu">
          <div @click="goToHome">Artiste matching</div>
          <div @click="goToProfile">Profile</div>
          <div @click="logout">Déconnexion</div>
        </div>
      </div>
    </nav>

    <div class="content">
      <div class="card">
        <h2 class="card-title">Editez votre profile</h2>
        <h3>Nom d'utilisateur</h3>
        <input 
          v-model="form.user.username"
          style="width: 92%;"
        />
        <h3 v-if="currentUser.user.role == 'artist'">Followers</h3>
        <input 
          v-if="currentUser.user.role == 'artist'"
          v-model="form.followers"
          style="width: 92%;"
        />
        <h3 v-if="currentUser.user.role == 'ConcertOwner'">Capacité</h3>
        <input 
          v-if="currentUser.user.role == 'ConcertOwner'"
          v-model="form.capacity"
          style="width: 92%;"
        />
        <h3 v-if="currentUser.user.role == 'artist'">Genre musical</h3>
        <div v-if="currentUser.user.role == 'artist'" class="search-bar">
          <select v-model="form.genre">
            <option disabled value="">-- Choisissez un genre --</option>
            <option v-for="genre in genres" :key="genre" :value="genre">
              {{ genre["name"] }}
            </option>
          </select>
        </div>
        <h3>Localisation</h3>
        <div class="search-bar">
          <select v-model="form.user.country">
            <option disabled value="">-- Choisissez un pays --</option>
            <option v-for="country in countries" :key="country.code" :value="country.code">
              {{ country["name"] }}
            </option>
          </select>
        </div>
        <button @click="updateUserProfile">Valider</button>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { genres, countries } from '@/const.js' 
import { useUser } from '@/stores/user'
import axios from 'axios'

const userStore = useUser()

const router = useRouter()
const showMenu = ref(false)
const form = ref({
  username: '',
  country: '',
  genre: '',
  followers: '',
  capacity: '',
})

const currentUser = userStore.getCurrentUser

if (currentUser) {
  let parsedGenre = ''
  try {
    parsedGenre = JSON.parse(currentUser.genre.replace(/'/g, '"'))
  } catch (e) {
    console.warn('Impossible de parser le genre', currentUser.genre)
  }
  
  Object.assign(form.value, {
    user: {
      username: currentUser.user.username || '',
      country: currentUser.user.country || '',
      role: currentUser.user.role || '',
    },
    genre: parsedGenre,
    followers: currentUser.followers || '',
    capacity: currentUser.capacity || '',
  })
}

const updateUserProfile = async () => {
  try {
    const token = localStorage.getItem('access')

    if (!token) {
      console.error("Token d'accès non trouvé")
      return
    }

    const response = await axios.post(
      'http://localhost:8000/api/me',
      form.value,
      {
        headers: {
          Authorization: `Bearer ${token}`
        }
      }
    )

    userStore.setUser(response.data)

    alert('Profil mis à jour avec succès !')
  } catch (error) {
    console.error('Erreur lors de la mise à jour du profil :', error)
    alert('Échec de la mise à jour du profil')
  }
}


const toggleMenu = () => {
  showMenu.value = !showMenu.value
}

const goToHome = () => {
  router.push({ name: 'Home' })
}

const goToProfile = () => {
  router.push({ name: 'Profile' })
}

const logout = () => {
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
  userStore.clearUser()
  router.push({ name: 'Connexion' })
}
</script>
<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 10;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 60px;
  background-color: #007bff;
  color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
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

.dropdown-menu {
  position: absolute;
  top: 60px;
  right: 1rem;
  background-color: white;
  color: black;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
  z-index: 20;
}

.dropdown-menu div {
  padding: 10px 15px;
  cursor: pointer;
}

.dropdown-menu div:hover {
  background-color: #f1f1f1;
}

.content {
  padding: 2rem;
  padding-top: 80px;
  display: flex;
  justify-content: center;
}
.card {
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 12px;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  border: 1px solid black;
}

.card-title {
  color: rgb(0, 0, 0);
  margin-bottom: 1rem;
  text-align: center;
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


input {
  padding: 0.5rem 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 6px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
