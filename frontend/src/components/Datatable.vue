<template>
  <div class="table-wrapper">
    <div class="table-card">
      <h2>Liste des utilisateurs</h2>

      <table>
        <thead>
          <tr>
            <th>Username</th>
            <th>Rôle</th>
            <th>Pays</th>
            <th>Genre</th>
            <th>Followers</th>
            <th>Capacité</th>
            <th>Adresse</th>
            <th>Modifier</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(user, index) in users" :key="index">
            <td>{{ user.user.username }}</td>
            <td>{{ user.user.role }}</td>
            <td>{{ getCountryName(user.user.country) }}</td>
            <td>{{ user.genre?.name }}</td>
            <td>{{ user.followers || '' }}</td>
            <td>{{ user.capacity || '' }}</td>
            <td>{{ user.adress }}</td>
            <td>
              <button class="edit-btn" @click="openModal(user, index)">
                <i class="mdi mdi-pencil"></i>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <EditUserModal
      v-if="showModal"
      :user="selectedUser"
      :show="showModal"
      @close="closeModal"
      @save="saveUser"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { countries, genres } from '@/const.js' 
import EditUserModal from './EditUserModal.vue'
import axios from 'axios'

const users = ref([])
const showModal = ref(false)
const selectedUser = ref({})
const selectedIndex = ref(null)
const accessToken = localStorage.getItem('access')

const fetchUsers = async () => {
  try {
    const res = await axios.get('http://localhost:8000/api/user', {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    })
    users.value = res.data.map(user => {
      let genreObj = null

      if (typeof user.genre === 'string') {
        try {
          const parsed = JSON.parse(user.genre.replace(/'/g, '"'))
          genreObj = parsed
        } catch {
          genreObj = genres.find(g => g.code === user.genre) || { code: user.genre, name: user.genre }
        }
      } else if (typeof user.genre === 'object') {
        genreObj = user.genre
      }

      return {
        ...user,
        genre: genreObj,
      }
    })
  } catch (e) {
    console.error('Erreur lors du chargement des utilisateurs :', e)
  }
}

onMounted(() => {
  fetchUsers()
})

const openModal = (user, index) => {
  selectedUser.value = { ...user }
  selectedIndex.value = index
  showModal.value = true
}

const closeModal = () => {
  showModal.value = false
}

const getCountryName = (code) => {
  return countries.find(c => c["code"] === code)?.["name"] || code
}

const saveUser = (updatedUser) => {
  let genreObj = null

  if (typeof updatedUser.genre === 'string') {
    genreObj = genres.find(g => g.code === updatedUser.genre) || { code: updatedUser.genre, name: updatedUser.genre }
  } else if (typeof updatedUser.genre === 'object') {
    genreObj = updatedUser.genre
  }

  updatedUser.genre = genreObj

  if (selectedIndex.value !== null) {
    users.value[selectedIndex.value] = updatedUser
  }
  closeModal()
}
</script>

<style scoped>
.table-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
}

.table-card {
  max-width: 1000px;
  width: 90%;
  padding: 2rem;
  background-color: #f9f9f9;
  border-radius: 12px;
  border: 1px solid black;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  font-family: 'Roboto', sans-serif;
}

.table-card h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #333;
}

table {
  width: 100%;
  border-collapse: collapse;
}

thead {
  background-color: #007bff;
  color: white;
}

th, td {
  padding: 0.75rem;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

tbody tr:hover {
  background-color: #f1f1f1;
}

.edit-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.2rem;
  transition: transform 0.2s;
}

.edit-btn:hover {
  transform: scale(1.2);
}
</style>
