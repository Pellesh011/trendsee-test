<template>
  <div class="blogger-card container">
    <div class="flex">
      <div class="blogger-avatar">
        <img :src="avatarSrc" alt="User Avatar" class="user-avatar" />
      </div>
      <div class="blogger-body">
        <div class="grid">
          <a href="#" class="text-brand heading-6 semibold">{{ username }}</a>
          <span class="action-small semibold-500 text-secondary">{{ followers }}</span>
        </div>
      </div>
    </div>
    <div v-if="showFollow" class="height-100">
      <button class="blogger-follow" type="button" title="Follow">
        <img src="@/assets/images/icons/blogger-follow.png" alt="Follow" />
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  avatarSrc?: string
  username: string
  followers: string
  showFollow?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  avatarSrc: '@/assets/images/utils/blogger-avatar.jpg',
  showFollow: true
}) as Props // eslint-disable-next-line @typescript-eslint/no-unused-vars
</script>

<style scoped>
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
</style>

