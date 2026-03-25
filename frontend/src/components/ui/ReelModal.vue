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
                  <img src="@/assets/images/icons/open.svg" alt="open" class="mt-5">
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
          </div>
        </div>
      </div>
      <div class="reel-modal-right">
        <button class="modal-close-btn" @click="modalStore.close">
          ×
        </button>
        <div class="modal-content">
          <div v-html="modalStore.activePost?.desc || ''" class="modal-desc"></div>
          <div class="modal-stats">
            <div class="stat-item">
              <img src="@/assets/images/icons/views.svg" alt="Views">
              <span>{{ modalStore.activePost?.stats?.[0] || '0' }}</span>
            </div>
            <div class="stat-item">
              <img src="@/assets/images/icons/likes.svg" alt="Likes">
              <span>{{ modalStore.activePost?.stats?.[1] || '0' }}</span>
            </div>
            <div class="stat-item">
              <img src="@/assets/images/icons/comments.svg" alt="Comments">
              <span>{{ modalStore.activePost?.stats?.[2] || '0' }}</span>
            </div>
            <div class="stat-item">
              <img src="@/assets/images/icons/shares.svg" alt="Shares">
              <span>{{ modalStore.activePost?.stats?.[3] || '0' }}</span>
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
  min-width: 0;
}

.modal-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.reel-modal-right {
  flex: 1;

  position: relative;
  display: flex;
  flex-direction: column;
}

.modal-close-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: rgba(0, 0, 0, 0.5);
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 10;
  backdrop-filter: blur(10px);
  color: white;
  font-size: 24px;
  font-weight: bold;
}

.modal-close-btn:hover {
  background: rgba(0, 0, 0, 0.7);
}

.modal-content {
  flex: 1;
  padding: 2rem;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 2rem;
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

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  font-weight: 500;
}

.stat-item img {
  width: 24px;
  height: 24px;
}

.modal-blogger {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #eee;
}

.blogger-avatar-large {
  width: 60px;
  height: 60px;
}

.user-avatar-large {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  border: 2px solid white;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.blogger-info a {
  color: #1a73e8;
  text-decoration: none;
}

.follow-btn-large {
  margin-left: auto;
  padding: 0.75rem 1.5rem;
  background: #f8f9fa;
  border: 1px solid #ddd;
  border-radius: 25px;
  cursor: pointer;
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

.bottom-btn {
  position: absolute;
  bottom: 10px;
  width: calc(100% - 10px);
}

.video-cart {


  max-width: 100%;
  display: flex;
  flex-direction: column;
  gap: 4px;
  border-radius: 12px;
  padding: 4px 4px 8px 4px;
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

.video-card-desc-short {

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

.icon-button-lg {
  display: flex;
  align-items: center;
  padding: 8px;
  gap: 8px;
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

.video-statistics {
  display: flex;
  justify-content: space-between;
  max-width: 254px;
  margin: 0 auto;
  position: absolute;
  bottom: 0px;
  width: 100%;
}

.video-statistics-container {
  margin: 10px;
  border: 1px solid transparent;
  border-radius: 8px;
  width: 100%;
  backdrop-filter: blur(8px);
  background-color: var(--Black-40, #00000066);
}

.video-statistics .stats {

  color: white;
  padding-bottom: 5px;
}

.column {
  flex: 1;
  padding: 0px;
  text-align: center;
}

.image-container {
  width: 100%;
  padding: 5px;
}

.image-container img {
  width: 20px;
  height: 20px;
}
</style>
