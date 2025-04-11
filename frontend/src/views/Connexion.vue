<template>
  <div class="auth-wrapper">
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
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

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
      router.push({ name: 'Home' })
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
.auth-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* prend toute la colonne centrale */
}

.auth {
  max-width: 400px;
  margin: 5rem auto;
  padding: 2rem;
  background-color: #f9f9f9;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  font-family: 'Roboto', sans-serif;
}

.auth h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #333;
}

.auth form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.auth input {
  padding: 0.75rem 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.auth input:focus {
  border-color: #007bff;
  outline: none;
}

.auth button {
  padding: 0.75rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.auth button:hover {
  background-color: #0056b3;
}

.auth p {
  text-align: center;
  margin-top: 1rem;
  font-size: 0.95rem;
  color: #555;
}

.auth p[style*="cursor"] {
  color: #007bff;
  text-decoration: underline;
  cursor: pointer;
}

.auth p[style*="color: red"] {
  color: red;
  font-weight: bold;
}
</style>
