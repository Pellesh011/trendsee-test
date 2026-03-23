import { createApp } from 'vue';
import App from '@/App.vue';
import type { SetupContext } from 'vue';
import { createPinia } from 'pinia';
import { router } from './router';
import './assets/main.css';

const app = createApp(App);
app.use(createPinia());
app.use(router);
app.mount('#app');

