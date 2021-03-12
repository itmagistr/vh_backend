import Vue from 'vue';
import App from './App.vue';
import router from "./router";
import store from "./store";
import en from './locales/en';
import ru from './locales/ru';
import VueMeta from 'vue-meta';
import VueI18n from 'vue-i18n';



Vue.config.productionTip = false
Vue.use(VueMeta)
Vue.use(VueI18n)

const locmsgs = {
  en,
  ru
}

// Create VueI18n instance with options
const i18n = new VueI18n({
  locale: 'ru', // set locale
  locmsgs, // set locale messages
})


new Vue({
  i18n,
  router,
  store,
   render: h => h(App),
}).$mount('#app')

