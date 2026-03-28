<template>
  <div class="login-page">
    <div class="login-card">
      <h1>Login</h1>
      <p>Enter your username to login</p>
      
      <form @submit.prevent="handleLogin" class="login-form">
        <div class="input-group">
          <input 
            v-model="loginData.name" 
            type="text" 
            placeholder="Username"
            required
            :disabled="loading"
          />
        </div>
        <button type="submit" :disabled="loading || !loginData.name">
          {{ loading ? 'Logging in...' : 'Login' }}
        </button>
      </form>
      
      <p v-if="error" class="error">{{ error }}</p>
      <p v-else-if="success" class="success">Logged in successfully! Redirecting...</p>
      
      <div class="links">
        <router-link to="/">Skip / Home</router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useApi } from '@/composables/useApi';

const router = useRouter();
const { login: apiLogin, loading, error } = useApi();

const loginData = ref({ name: '' });
const success = ref(false);

const handleLogin = async () => {
  const result = await apiLogin(loginData.value.name);
  if (result) {
    success.value = true;
    setTimeout(() => router.push('/'), 1000);
  }
};
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.login-card {
  background: white;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.1);
  max-width: 400px;
  width: 100%;
  text-align: center;
}

h1 {
  margin: 0 0 10px;
  color: #333;
  font-size: 28px;
}

p {
  color: #666;
  margin-bottom: 30px;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.input-group input {
  width: 100%;
  padding: 15px;
  border: 2px solid #e1e5e9;
  border-radius: 12px;
  font-size: 16px;
  transition: border-color 0.3s;
  box-sizing: border-box;
}

.input-group input:focus {
  outline: none;
  border-color: #667eea;
}

button {
  padding: 15px;
  background: linear-gradient(45deg, #667eea, #764ba2);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s;
}

button:hover:not(:disabled) {
  transform: translateY(-2px);
}

button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.error {
  color: #e74c3c;
  margin: 10px 0;
}

.success {
  color: #27ae60;
  margin: 10px 0;
}

.links {
  margin-top: 20px;
}

.links a {
  color: #667eea;
  text-decoration: none;
  font-size: 14px;
}

.links a:hover {
  text-decoration: underline;
}
</style>

