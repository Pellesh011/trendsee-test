<template>
  <Transition name="modal">
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
            <img src="@/assets/images/icons/video-play.svg" alt="open" class="video-play">
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
                background="caption semibold-500 gray-8" />
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
        <div class="flex flex-full-width">
          <div>
            <p class="text-secondary body-small">Тема видео</p>
            <h3 v-html="modalStore.activePost?.desc || ''" class="text-primary heading-3 semibold"></h3>
          </div>

          <button class="modal-close-btn background-secondary " @click="modalStore.close">
            <img src="@/assets/images/icons/close.svg">
          </button>
        </div>

        <div class="modal-content">


          <div class="flex">
            <div class="background-secondary  music-item">
              <div class="horizontal-align ">
                <div class="icon  icon-16">
                  <img src="@/assets/images/icons/music.svg" alt="views" class="">
                </div>
                <span class="action-small text-lh-caption semibold ml-5 gray-8">Tyga – Pop it off</span>
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
              <span class="body-small brand-medium semibold-500">Туториал</span>
            </div>
            <div class="tag backgroud-warning-subtle">
              <span class="body-small warning-bold semibold-500">Энергичное видео</span>
            </div>
            <div class="tag backgroud-danger-subtle">
              <span class="body-small danger-bold semibold-500">Изи монтаж</span>
            </div>
            <div class="tag backgroud-success-subtle">
              <span class="body-small success-bold semibold-500">Трендовый звук</span>
            </div>
            <div class="tag background-brand-subtle">
              <span class="body-small brand-medium semibold-500">Лид магнит</span>
            </div>
            <div class="tag backgroud-success-subtle">
              <span class="body-small success-bold semibold-500">Красота и здоровье</span>
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
                  <span class="action-small text-lh-caption semibold brand-medium">Переведено</span>
                </div>
              </div>
              <button class="btn-mid background-secondary ml-10">
                <img src="@/assets/images/icons/copy.svg">
              </button>
            </div>
          </div>
          <div class="mt-10">
            <Expand v-model="transcridtionText" :maxCollapsedHeight="160" :transitionMs="250"
              expandBtnAlign="flex-content-right" expandIcon="arrow-down"
              background="background-secondary pad-20 body-small text-secondary text-lh-big" />
          </div>
          <button class="btn-big  background-default mt-30">
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
            <div class="background-secondary pad-20 mt-10">
              <p class="body-small text-secondary ">
                Разбор состава/логики: он в человеческих словах переводит состав/механику (“что реально делает X”),
                называет 2–3 работающих активных компонента и 2–3 маркетинговых “пустых” обещания.
              </p>

            </div>
          </div>
          <div class="stepper pt-20">
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
                  <p class="step-desc body-small text-secondary">[Герой] показывает проблему -> Резкар смена кадра ->
                    Решение</p>
                </div>

              </li>
              <li>
                <div class="left-stepper">
                  <p class="caption text-secondary"> <img src="@/assets/images/icons/timer.svg">15–120 сек</p>
                </div>
                <div class="right-stepper">
                  <img src="@/assets/images/icons/step-3.svg">
                  <p class="step-heading heading-5">Сюжет</p>
                  <p class="step-desc body-small text-secondary last-step-desc">Призыв: "Пиши слово "ССЫЛКА" в комменты"
                  </p>
                </div>
              </li>
            </ul>
          </div>
          <div class="pad-20 background-secondary">
            <div class="flex-full-width panel">
              <div>
                <h5 class="heading-5">Хук фраза</h5>
                <p class="body-small text-secondary mt-10">Одна из них — пустышка. Угадаешь какая?</p>
              </div>
              <div class="flex">
                <button class="btn-mid background-secondary ml-10">
                  <img src="@/assets/images/icons/copy.svg">
                </button>
              </div>
            </div>
            <div class="flex-full-width panel  mt-10">
              <div>
                <h5 class="heading-5">Визуальный хук</h5>
                <p class="body-small text-secondary mt-10">Одна из них — пустышка. Угадаешь какая?</p>
              </div>
              <div class="flex">
                <button class="btn-mid background-secondary ml-10">
                  <img src="@/assets/images/icons/copy.svg">
                </button>
              </div>
            </div>
            <div class="flex-full-width panel mt-10">
              <div>
                <h5 class="heading-5">Текстовый хук</h5>
                <p class="body-small text-secondary mt-10">Одна из них — пустышка. Угадаешь какая?</p>
              </div>
              <div class="flex">
                <button class="btn-mid background-secondary ml-10">
                  <img src="@/assets/images/icons/copy.svg">
                </button>
              </div>
            </div>
          </div>
          <div class="panel flex-full-width pt-20">
            <div>
              <h5 class="heading-5">Рабочие приёмы</h5>
            </div>
            <div class="flex">
              <button class="btn-mid background-secondary ml-10">
                <img src="@/assets/images/icons/copy.svg">
              </button>
            </div>
          </div>
          <div class="pad-20 background-secondary mt-10">
              <div>
                <h5 class="heading-5">2. Суть видео</h5>
                <p class="body-small text-secondary mt-10">Приём: “кому подходит / кому нет” двумя блоками. <br><br>
Почему сработало: это формат “диагноз → лечение → решение”. Люди сохраняют не эмоции, а инструкцию. И это “обзор”, а не философия</p>
              </div>
              <div class=" mt-10">
                <h5 class="heading-5">3. Монтаж</h5>
                <p class="body-small text-secondary mt-10">Приём: смена планов каждые 1–2 секунды: лицо → продукт крупно → рука (демо) → снова лицо. <br><br>
Почему сработало: вертикалки смотрят на автопилоте. Частая смена планов держит внимание даже без звука <br><br>
Приём: все доказательства — через B-roll вставки на 0.3–0.8 сек (катышки, блеск, этикетка, нанесение. <br><br>
Почему сработало: речь в кадре быстро утомляет. B-roll делает ощущение “я реально тестировал”.</p>
              </div>
              <div class=" mt-10">
                <h5 class="heading-5">4. Реплики</h5>
                <p class="body-small text-secondary mt-10">Приём: “триггер доверия” одной фразой: “Я не продаю этот SPF, мне пох, скажу как есть.”<br><br>
Почему сработало: снимает защиту “мне впаривают”.<br><br>
Приём: “вилка выбора” в середине: “Если кожа жирная — делай так. Если сухая — так.”<br><br>
Почему сработало: персонализация без долгого объяснения = удержание.</p>
              </div>
          </div>
          <div class="panel flex-full-width pt-20">
            <div>
              <h5 class="heading-5">Воронка / Маркетинг</h5>
            </div>
            <div class="flex">
              <button class="btn-mid background-secondary ml-10">
                <img src="@/assets/images/icons/copy.svg">
              </button>
            </div>
          </div>
          <div class="pad-20 background-secondary mt-10">
              <div>
                <h5 class="heading-5">CTA голос/визуал</h5>
                <p class="body-small text-secondary mt-10">Почему сработало: зритель узнаёт свой баг мгновенно. Это не “мнение”, а физический факт в кадре, мозг цепляется.</p>
              </div>
              <div class=" mt-10">
                <h5 class="heading-5">Тригер</h5>
                <p class="body-small text-secondary mt-10">Почему сработало: зритель узнаёт свой баг мгновенно. Это не “мнение”, а физический факт в кадре, мозг цепляется.</p>
              </div>
              <div class=" mt-10">
                <h5 class="heading-5">Куда ведет</h5>
                <p class="body-small text-secondary mt-10">Почему сработало: зритель узнаёт свой баг мгновенно. Это не “мнение”, а физический факт в кадре, мозг цепляется.</p>
              </div>
              <div class=" mt-10">
                <h5 class="heading-5">Лид-магнит</h5>
                <p class="body-small text-secondary mt-10">Почему сработало: зритель узнаёт свой баг мгновенно. Это не “мнение”, а физический факт в кадре, мозг цепляется.</p>
              </div>
          </div>
        </div>
      </div>
    </div>
    </div>
  </Transition>

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
  padding: 2px 12px 6px;
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

h3 {
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
  margin: 20px 10px 20px 20px;
}

.video-play{
  position: absolute;
    top: 145px;
    left: calc(50% - 30px);
}

.reel-modal-right {
  flex: 1;
  margin: 20px 20px;
  position: relative;
  display: flex;
  flex-direction: column;
}

.modal-close-btn img {
  width: 10px;
  height: 10px;
}

.modal-close-btn {

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

.stepper ul li div.left-stepper p {
  width: 120px;
  padding-right: 20px;
}

.stepper ul li div.left-stepper img {

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
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.25s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-active .reel-modal,
.modal-leave-active .reel-modal {
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.modal-enter-from .reel-modal,
.modal-leave-to .reel-modal {
  transform: translateY(20px) scale(0.95);
  opacity: 0;
}

.modal-enter-to .reel-modal,
.modal-leave-from .reel-modal {
  transform: translateY(0) scale(1);
  opacity: 1;
}

</style>

