<template>
  <div class="sidebar">
    <div class="logo">
      <div class="panel">
        <div class=""><img src="@/assets/images/logo.svg" alt="Trendsee Logo" /></div>
        <div class=""><img src="@/assets/images/icons/toggle-side-menu.svg" class="in" alt="Trendsee Logo" /></div>
      </div>

    </div>
    <nav>
      <ul class="side-menu">
        <li class="sub-menu"><a class="heading-6">Поиск контента</a></li>
        <NavMenuItem iconSrc="src/assets/images/icons/home.svg" label="Главная" href="/" />
        <NavMenuItem iconSrc="src/assets/images/icons/video.svg" label="Видео" href="/" />
        <NavMenuItem iconSrc="src/assets/images/icons/search.svg" label="Шпионаж" href="/" />
        <NavMenuItem 
          iconSrc="src/assets/images/icons/radar.svg" 
          label="Контент радар" 
          href="/" 
          :badge="{text: '123', class: 'background-brand-subtle text-brand badger caption text-lh-caption bold'}" 
        />

        <li class="sub-menu"><a>Работа с соцсетями</a></li>
        <NavMenuItem iconSrc="src/assets/images/icons/cross-posting.svg" label="Кросс-постинг" href="/crosspost" />
        <NavMenuItem iconSrc="src/assets/images/icons/chat-bots.svg" label="Чат боты" href="/bots" />
        <li class="sub-menu"><a>Инструменты</a></li>
        <NavMenuItem iconSrc="src/assets/images/icons/ai-scenarios.svg" label="ИИ-сценарный" href="/ai" />
        <NavMenuItem iconSrc="src/assets/images/icons/carusel.svg" label="Карусели" href="/" />
        <NavMenuItem iconSrc="src/assets/images/icons/an-video.svg" label="Анализ видео" href="/" />
        <NavMenuItem iconSrc="src/assets/images/icons/an-prof.svg" label="Анализ профиля" href="/" />
        <NavMenuItem 
          iconSrc="src/assets/images/icons/chernovik.svg" 
          label="Черновик"
          href="/" 
          :badge="{text: 'скоро', class: 'background-tertiary badger caption text-lh-caption bold text-secondary'}"/>
      </ul>
    </nav>
    <div class="layout bg-white">
      <div class="tokens horizontal-align">
        <span class="icon  icon-16">
          <img src="@/assets/images/icons/fire.svg" alt="Icon">
        </span>
        <span class="body-small italic bold">Токены</span>
        <span class="body-small text-lh-caption bold flex-content-right">1 245 / 4 497</span>
      </div>
      <div class="tokens-slide-bar mt-5">
        <div class="tokens-slide-bar-full">
          <div class="tokens-slide-bar-filled"></div>
        </div>
      </div>
      <div class=" mt-10">
        <a class="horizontal-align" href="">
          <span class="text-tertiary body-small body-medium">Creative +</span>
          <span class="icon-7-13  flex-content-right">
            <img src="@/assets/images/icons/right-btn.svg" alt="Icon">
          </span>
        </a>
      </div>

    </div>
    <div class="blogger-card container  mt-10">
      <div class="flex">
        <div class="blogger-avatar">
          <img src="@/assets/images/utils/blogger-avatar.jpg" alt="User Avatar" class="user-avatar">
        </div>
        <div class="blogger-body">
          <div class="grid">
            <p class="text-secondary  body-small medium">Александра</p>
            <span class="caption regular text-secondary-inverse mt-5">+7 (999) 999-99-99</span>
          </div>

        </div>
      </div>
      <div class="height-100">
        <button class="blogger-follow mt-10" type="button" title="Follow">
          <img src="@/assets/images/icons/toggle-side-menu.svg" class="exit" alt="exit">
        </button>
      </div>
    </div>
    <div class="container horizontal-align mt-10">
      <span class="icon  icon-16">
        <img src="@/assets/images/icons/RU.svg" alt="Icon">
      </span>
      <span class="text-tertiary  caption ">RU</span>
      <span class="icon  icon-16 ">
        <img src="@/assets/images/icons/arrow-down.svg" alt="Icon" class="">
      </span>
    </div>
  </div>
</template>


<script setup lang="ts">
import NavMenuItem from '@/components/ui/NavMenuItem.vue'
import Icon from '@/components/ui/Icon.vue'
import BloggerCard from '@/components/ui/BloggerCard.vue'

const {
  image = '/src/assets/images/utils/video-preview.png',
  desc = '500 000 лайков на ютубе делаем, <br>бля буду скидываю 😘',
  username = '@blogerich',
  followers = '384.5K',
  likes = '105K',
  comments = '485',
  date = '12.12.2025'
} = defineProps<{
  image?: string
  desc?: string
  username?: string
  followers?: string
  likes?: string
  comments?: string
  date?: string
}>();
</script>
<style scoped>
img.exit[src$="toggle-side-menu.svg"] {
  transform: rotate(180deg);
}

img.in[src$="toggle-side-menu.svg"] {
  transform: none;
}

img.out[src$="toggle-side-menu.svg"] {
  transform: rotate(180deg);
}

.blogger-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.blogger-avatar {
  width: 40px;
  height: 40px;
}

.blogger-body {
  padding-left: 6px;
}

.user-avatar {
  width: 100%;
  height: 100%;
  border-radius: 128px;
  border: 1px solid var(--white);
}

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
  padding: 8px 10px;
}

.sidebar nav ul li a {

  padding: 0px;
  text-decoration: none;
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



.tokens {

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

  object-fit: contain;
}

.text-primary {
  color: black;
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
