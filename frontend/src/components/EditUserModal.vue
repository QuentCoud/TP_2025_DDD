<template>
  <div class="modal-backdrop" @click.self="close">
    <div class="modal-content">
      <h2>Modifier l'utilisateur : {{ editedUser.username }}</h2>
      
      <form @submit.prevent="save">
        <div class="form-group">
          <label>Nom d'utilisateur</label>
          <input v-model="editedUser.username"/>
        </div>
        <div class="form-group">
          <label>Mot de passe</label>
          <input v-model="editedUser.password"/>
        </div>
        <div class="form-group">
          <label>Rôle</label>
          <select v-model="editedUser.role">
            <option disabled value="">-- Choisissez un rôle --</option>
            <option v-for="role in roles" :key="role" :value="role">
              {{ role }}
            </option>
          </select>
        </div>
        <div class="form-group">
          <label>Pays</label>
          <select v-model="editedUser.country">
            <option disabled value="">-- Choisissez un pays --</option>
            <option v-for="country in countries" :key="country.code" :value="country.code">
              {{ country.name }}
            </option>
          </select>
        </div>
        <div class="form-group">
          <label>Style musical</label>
          <select v-model="editedUser.style">
            <option disabled value="">-- Choisissez un style --</option>
            <option v-for="style in styles" :key="style" :value="style">
              {{ style }}
            </option>
          </select>
        </div>
        <div class="modal-actions">
          <button type="button" class="cancel-btn" @click="close">Annuler</button>
          <button type="submit" class="save-btn">Enregistrer</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { reactive, toRefs } from 'vue'
import { styles, countries, roles } from '@/const.js' 

const props = defineProps({
  user: {
    type: Object,
    required: true,
  },
  show: {
    type: Boolean,
    required: true,
  }
})

const emit = defineEmits(['close', 'save'])

// Copie locale de l'utilisateur pour pouvoir éditer sans modifier directement l'original
const editedUser = reactive({ ...props.user })

const close = () => {
  emit('close')
}

const save = () => {
  emit('save', { ...editedUser })
}
</script>

<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
}

.modal-content {
  background-color: #f9f9f9;
  padding: 2rem;
  border-radius: 12px;
  border: 1px solid black;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  width: 90%;
  max-width: 500px;
  font-family: 'Roboto', sans-serif;
}

h2 {
  text-align: center;
  margin-bottom: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 1rem;
}

label {
  margin-bottom: 0.5rem;
  font-weight: bold;
  color: #333;
}

input {
  padding: 0.75rem 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

input:focus {
  border-color: #007bff;
  outline: none;
}

select {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s;
  background-color: white;
}

select:focus {
  border-color: #007bff;
  outline: none;
}

.modal-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 1.5rem;
}

.save-btn, .cancel-btn {
  padding: 0.75rem 1rem;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  font-size: 1rem;
}

.save-btn {
  background-color: #007bff;
  color: white;
}

.save-btn:hover {
  background-color: #0056b3;
}

.cancel-btn {
  background-color: #ccc;
}

.cancel-btn:hover {
  background-color: #999;
}
</style>
