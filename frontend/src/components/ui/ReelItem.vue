<template>
    <div class="video-cart" @click="handleClick" role="button" tabindex="0">
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
                <div class="right-panel">
                    <button class="icon-button-lg">
                        <span class="icon  icon-20">
                            <img src="@/assets/images/icons/like.svg" alt="Icon">
                        </span>
                    </button>
                    <button class="icon-button-lg">
                        <span class="icon  icon-20">
                            <img src="@/assets/images/icons/share.svg" alt="Icon">
                        </span>
                    </button>
                </div>
            </div>
            <div class="video-statistics">
                <div class="video-statistics-container">
                    <div class="flex">
                        <div class="column">
                            <div class="image-container">
                                <img src="@/assets/images/icons/views.svg" alt="Картинка 1">
                            </div>
                            <div class="stats caption text-lh-caption regular">42</div>
                        </div>

                        <div class="column">
                            <div class="image-container">
                                <img src="@/assets/images/icons/likes.svg" alt="Картинка 2">
                            </div>
                            <div class="stats caption text-lh-caption regular">128</div>
                        </div>

                        <div class="column">
                            <div class="image-container">
                                <img src="@/assets/images/icons/comments.svg" alt="Картинка 3">
                            </div>
                            <div class="stats caption text-lh-caption regular">7</div>
                        </div>

                        <div class="column">
                            <div class="image-container">
                                <img src="@/assets/images/icons/shares.svg" alt="Картинка 4">
                            </div>
                            <div class="stats caption text-lh-caption regular">256</div>
                        </div>
                    </div>
                </div>
            </div>
            <img src="@/assets/images/utils/video-preview.png" alt="Post Image" class="post-image">
        </div>
        <div class="blogger-card container">
            <div class="flex">
                <div class="blogger-avatar">
                    <img src="@/assets/images/utils/blogger-avatar.jpg" alt="User Avatar" class="user-avatar">
                </div>
                <div class="blogger-body">
                    <div class="grid">
                        <a href="#" class="text-brand  heading-6 semibold">{{ post.username }}</a>
                        <span class="action-small semibold-500 text-secondary">{{ post.followers }}</span>
                    </div>

                </div>
            </div>
            <div class="height-100">
                <button class="blogger-follow" type="button" title="Follow">
                    <img src="@/assets/images/icons/blogger-follow.png" alt="Follow">
                </button>
            </div>
        </div>
        <div class="container video-card-desc-short">
            <p v-html="post.desc" class="text-secondary caption text-lh-caption semibold-500"></p>
        </div>
        <div class="container bottom-btn  grid">
            <p class="text-secondary-inverse caption text-lh-caption regular">{{ post.date || new Date().toLocaleDateString() }}</p>
            <button class="primary background-default">Анализ</button>
        </div>
    </div>
</template>

<script setup lang="ts">
import type { Post } from '@/types/post';

interface Props {
  post: Post;
}

const props = withDefaults(defineProps<Props>(), {});

const emit = defineEmits<{
  (e: 'open-reel', post: Post): void;
}>();

const handleClick = () => {
  emit('open-reel', props.post);
};
</script>

<style scoped>


.video-actions {
    position: absolute;
   
}

.bottom-btn{
    position: absolute;
    bottom: 10px;
    width: calc(100% - 10px);
}

.video-cart {
    width: 262px;
    height: 576px;
    min-width: 220px;
    max-width: 262px;
    display: flex;
    flex-direction: column;
    gap: 4px;
    border-radius: 12px;
    padding: 4px 4px 8px 4px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
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
    max-width: 254px;
    height: 400px;
    border-radius: 12px;
    object-fit: cover;
    object-position: center;
    display: block;
}

.video-card-desc-short {
    max-height: 44px;
    overflow: hidden;
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
.blogger-body{
    padding-left: 6px;
}

.user-avatar {
    width: 100%;
    height: 100%;
    border-radius: 128px;
    border: 1px solid var(--white);
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
