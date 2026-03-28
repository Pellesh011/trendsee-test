<template>
  <DefaultLayout />
  <ReelModal />
  <Spinner v-if="loadingStore.isGlobalLoading" />
</template>

<script setup lang="ts">
import DefaultLayout from '@/layouts/DefaultLayout.vue';
import ReelModal from '@/components/ui/ReelModal.vue';
import Spinner from '@/components/ui/Spinner.vue';
import { useLoadingStore } from '@/stores/loading';

const loadingStore = useLoadingStore();
</script>

