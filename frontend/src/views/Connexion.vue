<template>
  <div class="auth">
    <h2>{{ isLogin ? "Connexion" : "Inscription" }}</h2>
    
    <form @submit.prevent="submit">
      <input v-model="username" placeholder="Nom d'utilisateur" required />
      <input type="password" v-model="password" placeholder="Mot de passe" required />
      <button type="submit">{{ isLogin ? "Se connecter" : "S'inscrire" }}</button>
    </form>
    
    <p @click="toggleMode" style="cursor: pointer;">
      {{ isLogin ? "Pas de compte ? Inscris-toi ici" : "Déjà un compte ? Connecte-toi ici" }}
    </p>
    
    <p v-if="error" style="color: red;">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const isLogin = ref(true)
const username = ref('')
const password = ref('')
const error = ref('')

const toggleMode = () => {
  isLogin.value = !isLogin.value
  error.value = ''
}

const submit = async () => {
  try {
    error.value = ''
    if (isLogin.value) {
      const res = await axios.post('http://localhost:8000/api/token/', {
        username: username.value,
        password: password.value,
      })
      localStorage.setItem('access', res.data.access)
      localStorage.setItem('refresh', res.data.refresh)
      alert('Connecté !')
    } else {
      await axios.post('http://localhost:8000/api/register/', {
        username: username.value,
        password: password.value,
      })
      alert('Inscription réussie, connecte-toi !')
      isLogin.value = true
    }
  } catch (e) {
    error.value = e.response?.data?.detail || e.response?.data?.error || 'Erreur inconnue'
  }
}
</script>

<style scoped>
.auth {
  max-width: 400px;
  margin: auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>
