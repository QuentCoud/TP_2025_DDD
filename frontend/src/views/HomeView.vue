<template>
  <div class="home-view">
    <nav class="navbar">
      <div class="navbar-center">Artiste matching</div>
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
      <ArtistSearching v-if="currentUser.role == 'Artist'"/>
      <ConcertOwnerSearching v-if="currentUser.role == 'ConcertOwner'"/>
      <AdminCrud v-if="currentUser.role == 'Admin'"/>
    </div>
  </div>
</template>
<script setup>
import ArtistSearching from '@/components/ArtistSearching.vue'
import ConcertOwnerSearching from '@/components/ConcertOwnerSearching.vue'
import AdminCrud from '@/components/AdminCrud.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUser } from '@/stores/user.js'

const userStore = useUser()

const currentUser = userStore.getCurrentUser

const router = useRouter()
const showMenu = ref(false)

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
</style>
