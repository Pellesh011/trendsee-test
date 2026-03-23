<template>
    <div class="video-cart">
        <div class="video-content">
            <img :src="image" alt="Post Image" class="post-image">
        </div>
        <div class="blogger-card container">
            <div class="flex">
                <div class="blogger-avatar">
                    <img src="@/assets/images/utils/blogger-avatar.jpg" alt="User Avatar" class="user-avatar">
                </div>
                <div class="blogger-body">
                    <div class="grid">
                        <a href="#" class="text-brand  heading-6 semibold">{{ username }}</a>
                        <span class="action-small regular">{{ followers }}</span>
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
            <p v-html="desc" class="text-secondary caption regular"></p>
        </div>
        <div class="container grid">
            <p class="text-secondary-inverse caption regular">{{ date }}</p>
            <button class="primary background-default">Анализ</button>
        </div>
    </div>
</template>

<script setup lang="ts">
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

.flex {
    display: flex;
    align-items: center;
    gap: 10px;
}

.blogger-avatar {
    width: 40px;
    height: 40px;
}

.user-avatar {
    width: 100%;
    height: 100%;
    border-radius: 128px;
    border: 1px solid var(--White-100, #FFFFFF);
}

.blogger-follow {
    width: 32px;
    height: 32px;
    padding: 0;
    cursor: pointer;
    background-color: transparent;
}

.blogger-follow:hover {
    opacity: 1;
}

.blogger-follow img {
    width: 100%;
    height: 100%;
    object-fit: contain;
}
</style>
