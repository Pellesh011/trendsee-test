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
            <span class="text-secondary menu-text body-medium">Главная</span>

          </a>
        </li>
        <li class="sub-menu-item">
          <a href="/" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/video.svg" alt="Icon">
            </span>
            <span class="text-secondary  menu-text body-medium">Видео</span>

          </a>
        </li>
        <li class="sub-menu-item">
          <a href="/" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/search.svg" alt="Icon">
            </span>
            <span class="text-secondary menu-text  body-medium">Шпионаж</span>

          </a>
        </li>
        <li class="sub-menu-item">
          <a href="/" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/radar.svg" alt="Icon">
            </span>
            <span class="text-secondary menu-text  body-medium">Контент радар</span>
            <span class="background-brand-subtle text-brand badger caption text-lh-caption bold ">123</span>
          </a>
        </li>

        <li class="sub-menu"><a>Работа с соцсетями</a></li>
        <li class="sub-menu-item">
          <a href="/crosspost" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/cross-posting.svg" alt="Icon">
            </span>
            <span class="text-secondary menu-text  body-medium">Кросс-постинг</span>
          </a>
        </li>
        <li class="sub-menu-item">
          <a href="/bots" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/chat-bots.svg" alt="Icon">
            </span>
            <span class="text-secondary  menu-text body-medium">Чат боты</span>
          </a>
        </li>
        <li class="sub-menu"><a>Инструменты</a></li>
        <li class="sub-menu-item">
          <a href="/ai" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/ai-scenarios.svg" alt="Icon">
            </span>
            <span class="text-secondary  menu-text body-medium">ИИ-сценарный</span>
          </a>
        </li>

        <li class="sub-menu-item">
          <a href="/carousel" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/carusel.svg" alt="Icon">
            </span>
            <span class="text-secondary menu-text  body-medium">Карусели</span>
          </a>
        </li>
        <li class="sub-menu-item">
          <a href="/analyze-video" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/an-video.svg" alt="Icon">
            </span>
            <span class="text-secondary menu-text  body-medium">Анализ видео</span>
          </a>
        </li>
        <li class="sub-menu-item">
          <a href="/analyze-profile" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/an-prof.svg" alt="Icon">
            </span>
            <span class="text-secondary  menu-text body-medium">Анализ профиля</span>
          </a>
        </li>
        <li class="sub-menu-item">
          <a href="/draft" class="horizontal-align">
            <span class="icon  icon-16">
              <img src="@/assets/images/icons/chernovik.svg" alt="Icon">
            </span>
            <span class="text-secondary  menu-text body-medium">Черновик</span>
            <span class="background-tertiary badger caption text-lh-caption bold text-secondary">скоро</span>
          </a>
        </li>
      </ul>
    </nav>
    <div class="layout bg-white">
      <div class="tokens horizontal-align">
        <span class="body-small italic bold">Токены</span>
        <span class="background-tertiary body-small text-lh-caption bold flex-content-right">1 245 / 4 497</span>
      </div>
      <div class="tokens-slide-bar mt-5">
        <div class="tokens-slide-bar-full">
          <div class="tokens-slide-bar-filled"></div>
        </div>
      </div>
      <div class="horizontal-align mt-10">
        <span class="text-tertiary body-small body-medium">Creative +</span>
        <span class="icon-7-13  flex-content-right">
          <a href="">
            <img src="@/assets/images/icons/right.svg" alt="Icon">
          </a>
        </span>
      </div>

    </div>


  </div>
</template>

<script setup lang="ts">
// Moved from src/components/Sidebar.vue
</script>

<style scoped>
.tokens-slide-bar {
  width: 100%;
  height: 10px;
}

.tokens-slide-bar-full {
  border: 1px solid transparent;
  border-radius: 8px;
  height: 100%;
  background-color: var(--backgroud-tertiary, #E6E8EA);
}

.tokens-slide-bar-filled {
  width: 40%;
  border: 1px solid transparent;
  border-radius: 8px;
  height: 100%;
  background-color: var(--text-brand-medium, #E6E8EA);
}

.sidebar .sub-menu-item .menu-text {
  margin-left: 10px;
}

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

.sidebar nav ul li {
  padding: 4px 10px;
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
}

.text-lh-sm {
  line-height: 21px;
}

.icon img {
  width: 19.52px;
  height: 19.52px;
  object-fit: contain;
}

.text-primary {
  color: black;
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
