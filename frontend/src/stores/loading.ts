import { defineStore } from 'pinia';
import { computed } from 'vue';
import { useApi } from '@/composables/useApi';

export const useLoadingStore = defineStore('loading', () => {
  const api = useApi();

  // Proxy to shared global loading from useApi (singleton)
  const isGlobalLoading = computed(() => api.loading.value);

  return { 
    isGlobalLoading 
  };
});

