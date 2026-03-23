import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { Post } from '@/types/post';
import { useApi } from '@/composables/useApi';

export const usePostsStore = defineStore('posts', () => {
  const posts = ref<Post[]>([
    {
      id: 1,

      stats: ['105k', '85k', '15k', '485'],
      desc: '500 000 лайков на ютубе делаем, буду скидывать 😊',
      username: '@blogerich',
      followers: '384.5K',
      likes: '105K'
    },
    {
      id: 2,
image: '/src/assets/images/utils/video-preview.png',
      stats: ['98k', '72k', '12k', '320'],
      desc: 'Новый тренд в тиктоке! 🔥',
      username: '@trender',
      followers: '250.2K',
      likes: '98K'
    },
    {
      id: 3,
image: '/src/assets/images/utils/video-preview.png',
      stats: ['120k', '95k', '20k', '650'],
      desc: 'Как набрать миллион подписчиков за неделю',
      username: '@growfast',
      followers: '1.2M',
      likes: '120K'
    },
    {
      id: 4,
image: '/src/assets/images/utils/video-preview.png',
      stats: ['89k', '65k', '10k', '280'],
      desc: 'Секреты вирусного контента 💎',
      username: '@viralpro',
      followers: '456.7K',
      likes: '89K'
    },
    {
      id: 5,
image: '/src/assets/images/utils/video-preview.png',
      stats: ['75k', '55k', '8k', '210'],
      desc: 'Топ 5 идей для рилсов',
      username: '@reelsmaster',
      followers: '189.3K',
      likes: '75K'
    }
  ]);

  const { loading, error, fetchPosts } = useApi();

  const loadMore = async () => {
    const newPosts = await fetchPosts();
    if (newPosts) {
      posts.value.push(...newPosts);
    }
  };

  return { posts, loading, error, loadMore };
});

