<template>
  <div class="sidebar">
    <div class="logo">
      <div class="panel">
        <div class=""><img src="@/assets/images/logo.svg" alt="Trendsee Logo" /></div>
        <div class=""><img src="@/assets/images/icons/toggle-side-menu.svg" alt="Trendsee Logo" /></div>
      </div>
      
    </div>
    <nav>
      <ul class="side-menu">
        <li class="sub-menu"><a class="heading-6">Поиск контента</a></li>
        <li class="sub-menu-item">
          <a href="/" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/home.svg" alt="Icon">
            </span>
            <span class="text-secondary  body-medium">Главная</span>

          </a>
        </li>
        <li class="sub-menu-item">
          <a href="/" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/video.svg" alt="Icon">
            </span>
            <span class="text-secondary  body-medium">Видео</span>

          </a>
        </li>
        <li class="sub-menu-item">
          <a href="/" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/search.svg" alt="Icon">
            </span>
            <span class="text-secondary  body-medium">Шпионаж</span>

          </a>
        </li>
        <li class="sub-menu-item">
          <a href="/" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/radar.svg" alt="Icon">
            </span>
            <span class="text-secondary  body-medium">Контент радар</span>
            <span class="background-brand-subtle text-brand badger caption bold ">123</span>
          </a>
        </li>

        <li class="sub-menu"><a >Работа с соцсетями</a></li>
        <li class="sub-menu-item">
          <a href="/crosspost" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/cross-posting.svg" alt="Icon">
            </span>
            <span class="text-secondary  body-medium">Кросс-постинг</span>
          </a>
        </li>
        <li class="sub-menu-item">
          <a href="/bots" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/chat-bots.svg" alt="Icon">
            </span>
            <span class="text-secondary  body-medium">Чат боты</span>
          </a>
        </li>
        <li class="sub-menu"><a >Инструменты</a></li>
        <li class="sub-menu-item">
          <a href="/ai" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/ai-scenarios.svg" alt="Icon">
            </span>
            <span class="text-secondary  body-medium">ИИ-сценарный</span>
          </a>
        </li>

        <li class="sub-menu-item">
          <a href="/carousel" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/carusel.svg" alt="Icon">
            </span>
            <span class="text-secondary  body-medium">Карусели</span>
          </a>
        </li>
        <li class="sub-menu-item">
          <a href="/analyze-video" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/an-video.svg" alt="Icon">
            </span>
            <span class="text-secondary  body-medium">Анализ видео</span>
          </a>
        </li>
        <li class="sub-menu-item">
          <a href="/analyze-profile" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/an-prof.svg" alt="Icon">
            </span>
            <span class="text-secondary  body-medium">Анализ профиля</span>
          </a>
        </li>
        <li class="sub-menu-item">
          <a href="/draft" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/chernovik.svg" alt="Icon">
            </span>
            <span class="text-secondary  body-medium">Черновик</span>
            <span class="background-tertiary badger caption bold text-secondary">скоро</span>
          </a>
        </li>


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
  min-width: 300px;
  background-color: #f5f5f5;
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.sidebar nav ul {
  list-style-type: none;
  padding: 0px;
  flex: 1;
}
.sidebar nav ul li{
  padding: 4px 0px;
}
.sidebar nav ul li a {

  padding: 0px;
  text-decoration: none;
  color: #333;
  border-radius: 4px;
}
.sidebar .side-menu {
  margin-top: 0px;
}

.sidebar .sub-menu {
  padding: 5px 0px;
}

.sidebar .sub-menu a {
  color: var(--text-tertiary, #83939C);
}

.sidebar .sub-menu-item .badger {
  margin-left: 20px;
  border-radius: 16px;
}


.horizontal-align {
  display: flex;
  align-items: center;
  padding: 15px 20px;

  text-decoration: none;
  width: fit-content;
}

.tokens {
  padding-top: 20px;
  font-size: 14px;
}

.logo img {
  width: 100%;
  margin-bottom: 5px;
}


.icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  margin-right: 10px;
}

.icon img {
  width: 19.52px;
  height: 19.52px;
  object-fit: contain;
}

.text-secondary {
  color: #666;
  font-size: 16px;
}

.badger {
  font-size: 12px;
  font-weight: bold;
  padding: 4px 8px;
  border-radius: 12px;
  min-width: 20px;
  text-align: center;
}


</style>
