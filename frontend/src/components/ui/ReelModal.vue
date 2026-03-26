<template>
  <div v-if="modalStore.activePost" class="reel-modal-overlay" @click.self="modalStore.close">
    <div class="reel-modal">
      <div class="reel-modal-left">
        <div class="video-cart">
          <div class="video-content">
            <div class="video-actions panel">
              <div class="flex left-panel">
                <div class="">
                  <button class="icon-button-sm">
                    <span class="icon icon-16">
                      <img src="@/assets/images/icons/media.svg" alt="Icon">
                    </span>
                    <span class="text">Reels</span>
                  </button>
                  <button class="icon-button-sm">
                    <span class="icon  icon-16">
                      <img src="@/assets/images/icons/hot.svg" alt="Icon">
                    </span>
                    <span class="text">X10</span>
                  </button>
                </div>
              </div>
            </div>
            <img :src="modalStore.activePost?.image || ''" alt="Post Image" class="post-image">
            <div class="container  flex flex-full-width mt-5">
              <p class="text-secondary-inverse caption text-lh-caption regular">{{ modalStore.activePost?.date || new
                Date().toLocaleDateString() }}</p>
              <a href="">
                <img src="@/assets/images/icons/open.svg" alt="open" class="mt-5">
              </a>
            </div>
            <div class="blogger-card container">
              <div class="flex">
                <div class="blogger-avatar">
                  <img src="@/assets/images/utils/blogger-avatar.jpg" alt="User Avatar" class="user-avatar">
                </div>
                <div class="blogger-body">
                  <div class="grid">
                    <a href="#" class="text-brand  heading-6 semibold">{{ modalStore.activePost?.username || '' }}</a>
                    <span class="action-small regular text-secondary">{{ modalStore.activePost?.followers || ''
                    }}</span>
                  </div>
                </div>
              </div>
              <div class="height-100 mt-10">
                <button class="blogger-follow" type="button" title="Follow">
                  <img src="@/assets/images/icons/blogger-follow.png" alt="Follow">
                </button>
              </div>
            </div>
            <div class="container video-card-desc-short mt-10">
              <Expand v-model="modalStore.activePost.desc" :maxCollapsedHeight="16" :transitionMs="250" />
            </div>
            <div class="mt-10">
              <div class="horizontal-align flex-full-width background-secondary modal-stat-item ">
                <div class="horizontal-align ">
                  <div class="icon  icon-16">
                    <img src="@/assets/images/icons/views.svg" alt="views" class="color-filter-blue">
                  </div>
                  <span class="caption text-lh-caption regular gray-8  ml-10">Просмотры</span>
                </div>
                <span class="text-secondary body-small gray-7 ">1,2 млн</span>
              </div>
            </div>
            <div class="mt-5">
              <div class="horizontal-align flex-full-width background-secondary modal-stat-item ">
                <div class="horizontal-align ">
                  <div class="icon  icon-16">
                    <img src="@/assets/images/icons/likes.svg" alt="views" class="color-filter-electic-crimson">
                  </div>
                  <span class="caption text-lh-caption regular gray-8  ml-10">Лайки</span>
                </div>
                <span class="text-secondary body-small gray-7 ">1,2 млн</span>
              </div>
            </div>
            <div class="mt-5">
              <div class="horizontal-align flex-full-width background-secondary modal-stat-item ">
                <div class="horizontal-align ">
                  <div class="icon  icon-16">
                    <img src="@/assets/images/icons/comments.svg" alt="views" class="color-filter-green-bell-pepper">
                  </div>
                  <span class="caption text-lh-caption regular gray-8  ml-10">Комментарии</span>
                </div>
                <span class="text-secondary body-small gray-7 ">1,2 млн</span>
              </div>
            </div>
            <div class="mt-5">
              <div class="horizontal-align flex-full-width background-secondary modal-stat-item ">
                <div class="horizontal-align ">
                  <div class="icon  icon-16">
                    <img src="@/assets/images/icons/shares.svg" alt="views" class="color-filter-lucky-orange">
                  </div>
                  <span class="caption text-lh-caption regular gray-8  ml-10">Репосты</span>
                </div>
                <span class="text-secondary body-small gray-7 ">1,2 млн</span>
              </div>
            </div>
            <div class="mt-5">
              <div class="horizontal-align flex-full-width background-secondary modal-stat-item ">
                <div class="horizontal-align ">
                  <div class="icon  icon-16">
                    <img src="@/assets/images/icons/er.svg" alt="views" class="">
                  </div>
                  <span class="caption text-lh-caption regular gray-8  ml-10">ER</span>
                </div>
                <span class="text-secondary body-small gray-7 ">1,2 млн</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="reel-modal-right">
        <button class="modal-close-btn background-secondary" @click="modalStore.close">
          <img src="@/assets/images/icons/close.svg">
        </button>
        <div class="modal-content">
          <p class="text-secondary body-small">Тема видео</p>
          <h3 v-html="modalStore.activePost?.desc || ''" class="text-primary heading-3 semibold"></h3>
          <div class="flex">
            <div class="background-secondary  music-item">
              <div class="horizontal-align ">
                <div class="icon  icon-16">
                  <img src="@/assets/images/icons/music.svg" alt="views" class="">
                </div>
                <span class="action-small text-lh-caption regular ">Tyga – Pop it off</span>
              </div>
            </div>

            <div class=" video-language-item ml-10">
              <div class="horizontal-align ">
                <span class="action-small text-secondary regular ">Язык: </span>
                <div class="icon  icon-16 ml-10">
                  <img src="@/assets/images/icons/RU.svg" alt="views" class="" height="14">
                </div>
                <span class="action-small text-secondary regular ml-5">Russian</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script setup lang="ts">
import { useModalStore } from '@/stores/modal';
import type { Post } from '@/types/post';

const modalStore = useModalStore();


import Expand from '@/components/ui/ExpandContent.vue' // путь к файлу



</script>

<style scoped>
.video-language-item{
    width: fit-content;
  padding: 3.2px 8px;

}
.music-item {
  width: fit-content;
  padding: 3.2px 8px;
  border: 1px solid transparent;
  border-radius: 16px;
}

.modal-content h3 {
  margin: 10px 70px 10px 0px;
}

.reel-modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 1000;
  background: rgba(0, 0, 0, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
}

.reel-modal {
  display: flex;
  width: 920px;
  height: 800px;
  max-width: 1400px;
  background: white;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}

.reel-modal-left {
  flex: 1;
  max-width: 216px;
  margin: 10px;
  min-width: 0;
}



.reel-modal-right {
  flex: 1;
  margin: 10px;
  position: relative;
  display: flex;
  flex-direction: column;
}

.modal-close-btn img {
  width: 10px;
  height: 10px;
}

.modal-close-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  border: none;
  border-radius: 16px;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 10;

}

.modal-close-btn:hover {
  background: rgba(179, 179, 179, 0.7);
}

.modal-content {
  overflow-y: auto;
}

.modal-desc {
  font-size: 1.1rem;
  line-height: 1.6;
  color: #333;
}

.modal-stats {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
}

.modal-stat-item {
  padding: 10px;
  white-space: nowrap;
  border: 1px solid transparent;
  border-radius: 8px;
}










@media (max-width: 768px) {
  .reel-modal {
    flex-direction: column;
    width: 95vw;
    height: 95vh;
  }

  .reel-modal-right {
    max-width: none;
  }
}




.video-actions {
  position: absolute;

}



.video-cart {


  max-width: 100%;
  display: flex;
  flex-direction: column;
  gap: 4px;
  border-radius: 12px;

  overflow: hidden;
  background-color: white;
  position: relative;
}

.video-content {
  margin: 2px;
  position: relative;
  flex-grow: 0;
}

.post-image {
  width: 100%;

  height: 340px;
  border-radius: 12px;
  object-fit: cover;
  object-position: center;
  display: block;
}

.video-card-desc-short {}

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
  border: 1px solid var(--White-100, #FFFFFF);
}

.video-actions .btn {
  color: white;
  height: 28px;
  min-width: 28px;
}

.video-actions .btn>img {
  width: 16px;
  height: 16px;
  ;
}



.icon-button-sm {
  display: flex;
  align-items: center;
  padding: 6px;
  gap: 6px;
  background-color: var(--Black-40, #00000066);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 12px;
  margin-bottom: 4px;
}



.icon-button span.text {
  margin-left: 4px;
}
</style>
