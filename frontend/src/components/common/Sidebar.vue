<template>
  <div class="sidebar">
    <div class="logo">
      <img src="https://via.placeholder.com/200x50/4267B2/FFFFFF?text=Trendsee" alt="Trendsee Logo" />
    </div>
    <nav>
      <ul>
        <li><a href="/">Поиск контента</a></li>
        <li><a href="/">Главная</a></li>
        <li><a href="/video">Видео</a></li>
        <li><a href="/spy">Шпионаж</a></li>
        <li><a href="/radar">Контент radar</a></li>
        <li><a href="/social">Работа с соцсетями</a></li>
        <li><a href="/crosspost">Кросс-постинг</a></li>
        <li><a href="/bots">Чат боты</a></li>
        <li><a href="/tools">Инструменты</a></li>
        <li><a href="/ai">ИИ-сценарный</a></li>
        <li><a href="/carousel">Карусели</a></li>
        <li><a href="/analyze-video">Анализ видео</a></li>
        <li><a href="/analyze-profile">Анализ профиля</a></li>
        <li><a href="/draft">Черновик</a></li>
      </ul>
    </nav>
    <div class="tokens">
      <p>Токены: <span>1 245 / 4 497</span></p>
    </div>
  </div>
</template>

<script setup lang="ts">
// Moved from src/components/Sidebar.vue
</script>

<style scoped>
.sidebar {
  width: 250px;
  background-color: #f5f5f5;
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.sidebar nav ul {
  list-style-type: none;
  padding: 0;
  flex: 1;
}

.sidebar nav ul li a {
  display: block;
  padding: 10px;
  text-decoration: none;
  color: #333;
  border-radius: 4px;
}

.sidebar nav ul li a:hover {
  background-color: #ddd;
}

.tokens {
  padding-top: 20px;
  font-size: 14px;
}

.logo img {
  width: 100%;
  margin-bottom: 20px;
}
</style>

