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
              <Expand v-model="modalStore.activePost.desc" :maxCollapsedHeight="16" :transitionMs="250"
                background="caption gray-8" />
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
          <div class=" mt-10">
            <div class="tag background-brand-subtle">
              <span class="body-small brand-medium">Туториал</span>
            </div>
            <div class="tag backgroud-warning-subtle">
              <span class="body-small warning-bold">Энергичное видео</span>
            </div>
            <div class="tag backgroud-danger-subtle">
              <span class="body-small danger-bold">Изи монтаж</span>
            </div>
            <div class="tag backgroud-success-subtle">
              <span class="body-small success-bold">Трендовый звук</span>
            </div>
            <div class="tag background-brand-subtle">
              <span class="body-small brand-medium">Лид магнит</span>
            </div>
            <div class="tag backgroud-success-subtle">
              <span class="body-small success-bold">Красота и здоровье</span>
            </div>
          </div>
          <div class="panel flex-full-width pt-20">
            <div>
              <h5 class="heading-5">Транскрибация</h5>
            </div>
            <div class="flex">
              <div class="background-secondary  translated-item">
                <div class="horizontal-align ">
                  <div class="icon  icon-16">
                    <img src="@/assets/images/icons/translate.svg" alt="views" class="">
                  </div>
                  <span class="action-small text-lh-caption regular brand-medium">Tyga – Pop it off</span>
                </div>
              </div>
              <button class="btn-mid background-secondary ml-10">
                <img src="@/assets/images/icons/copy.svg">
              </button>
            </div>
          </div>
          <div class="mt-10">
            <Expand v-model="transcridtionText" :maxCollapsedHeight="140" :transitionMs="250"
              expandBtnAlign="flex-content-right" expandIcon="arrow-down"
              background="background-secondary pad-20 body-small text-secondary " />
          </div>
          <button class="btn-big  background-default mt-20">
            <div class="horizontal-align">
              <div class="icon icon-16 ml-10">
                <img src="@/assets/images/icons/magic.svg" alt="" class="">
              </div>
              <span class="white ml-10">
                Адаптировать
              </span>
            </div>
          </button>

          <div class=" pt-20">
            <div>
              <h5 class="heading-5">Суть</h5>
            </div>
            <div class="background-secondary pad-20">
              <p class="body-small text-secondary">
                Разбор состава/логики: он в человеческих словах переводит состав/механику (“что реально делает X”),
                называет 2–3 работающих активных компонента и 2–3 маркетинговых “пустых” обещания.
              </p>

            </div>
          </div>
          <div class="stepper">
            <ul class=" ">
              <li>
                <div class="left-stepper">
                  <p class="caption text-secondary"> <img src="@/assets/images/icons/timer.svg">0–3 сек</p>
                </div>
                <div class="right-stepper ">
                  <img src="@/assets/images/icons/step-1.svg">
                  <p class="step-heading heading-5">Шок-сравнение</p>
                  <p class="step-desc body-small text-secondary">Визуальный (Девушка с предметом) + Текст на экране:
                    "Это спасет вашу зиму"</p>
                </div>

              </li>
              <li>
                <div class="left-stepper">
                  <p class="caption text-secondary"> <img src="@/assets/images/icons/timer.svg">3–15 сек</p>
                </div>
                <div class="right-stepper">
                  <img src="@/assets/images/icons/step-2.svg">
                  <p class="step-heading heading-5">Сюжет</p>
                  <p class="step-desc body-small text-secondary">[Герой] показывает проблему -> Резкар смена кадра -> Решение</p>
                </div>

              </li>
              <li>
                <div class="left-stepper">
                  <p class="caption text-secondary"> <img src="@/assets/images/icons/timer.svg">15–120 сек</p>
                </div>
                <div class="right-stepper">
                  <img src="@/assets/images/icons/step-3.svg">
                  <p class="step-heading heading-5">Сюжет</p>
                  <p class="step-desc body-small text-secondary last-step-desc">Призыв: "Пиши слово "ССЫЛКА" в комменты" </p>
                </div>

              </li>

            </ul>


          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script setup lang="ts">
import { useModalStore } from '@/stores/modal';
import type { Post } from '@/types/post';
import { ref } from 'vue';
const modalStore = useModalStore();


import Expand from '@/components/ui/ExpandContent.vue' // путь к файлу
import { VueElement } from 'vue';


const transcridtionText = ref(`SPF скатывается? Смотри — вот эти катышки. И нет, это не всегда “плохой SPF”.
<br>
<br>
Скатывается по трём причинам.
<br>
<br>
Первая — ты намазал под SPF слишком много всего: сыворотка, крем, база… сверху SPF — и оно начинает конфликтовать. Чем больше слоёв, тем выше шанс, что всё свернётся в катышки.
<br>
<br>
Вторая — ты наносишь толстым слоем и начинаешь тереть. SPF не надо втирать как крем для рук. Его задача — лечь ровной плёнкой. Распределил тонко и не трогаешь.
<br>
<br>
Третья — ты сразу сверху лепишь макияж или начинаешь трогать лицо. Дай SPF пару минут просто схватиться на коже — и только потом тон, консилер, пудра.
<br>
<br>
Теперь быстро: как сделать, чтобы не скатывалось.<br>
Убери один слой под SPF — оставь либо сыворотку, либо крем, не всё вместе.<br>
Наноси тонким слоем, без “массажа”.<br>
И не трогай лицо сразу после нанесения.<br>
<br>
<br>
Кому этот SPF чаще всего не заходит: очень жирная кожа, активные воспаления и если у тебя кожа реагирует на отдушки — будет либо блеск, либо высыпания.
<br>
<br>
Вердикт: если ты носишь SPF без плотного тона и у тебя не супер-жирная кожа — можно брать. Если у тебя всё скатывается вообще от всего и лицо жирнится за час — ищи матирующий флюид и проще схему ухода.
<br>
<br>
Напиши в комменты: тип кожи и что ты наносишь под SPF — скажу, почему именно у тебя скатывается и что убрать.
`)


</script>

<style scoped>
.btn-mid {
  width: 32px;
  height: 32px;
  border: 1px solid transparent;
  border-radius: 12px;
}

.tag {
  border: 1px solid transparent;
  border-radius: 20px;
  padding: 4px 12px;
  margin-right: 10px;
  white-space: nowrap;
  float: left;
  margin-top: 10px;
}

.video-language-item {
  width: fit-content;
  padding: 3.2px 8px;

}

.translated-item {
  width: fit-content;
  padding: 7px 8px;
  border: 1px solid transparent;
  border-radius: 12px;
}

.music-item {
  width: fit-content;
  padding: 3.2px 8px;
  border: 1px solid transparent;
  border-radius: 8px;
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
  min-width: 216px;
  max-width: 216px;
  margin: 10px;
}



.reel-modal-right {
  flex: 1;
  margin: 10px 20px;
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
  top: 0.5rem;
  right: 0.5rem;
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
  background-color: var(--white);
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

.stepper li {
  display: flex;
}

.stepper ul {
  list-style: none;
}

.stepper ul li div.right-stepper {
  display: grid;
  grid-auto-flow: row;
  position: relative;
}

   .stepper ul {
    padding: 0px;
   }

.stepper ul li div.right-stepper img {
  position: absolute;
  left: -7.5px;
}

.stepper ul li div.left-stepper {
  text-align: right;
}
.stepper ul li div.left-stepper p{
  width: 120px;
  padding-right: 20px;
}

.stepper ul li div.left-stepper img{
 
  padding-right: 5px;
}

.stepper .right-stepper p.step-desc {
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 30px;
  border-left: 1px solid var(--stroke-focus);
}

.stepper .right-stepper p.step-heading {
  padding-left: 30px;
  border-left: none !important;
  margin-bottom: -4px;
  margin-top: -4px;
}


p.last-step-desc {
  border: none !important;

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
