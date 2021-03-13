import Vue from 'vue';
import App from './App.vue';
import router from "./router";
import store from "./store";
//import en from './locales/en';
//import ru from './locales/ru';
import VueMeta from 'vue-meta';
import VueI18n from 'vue-i18n';
Vue.use(VueMeta)
Vue.use(VueI18n)



Vue.config.productionTip = false


const messages = {
  en: { message: {
			'hello1': 'hello 1 world',
			
			'menu_services': 'Services',
			'menu_booking': 'Booking',
			'menu_doctors': 'Doctors',
			'menu_contacts': 'Contacts',
			'search_ph': 'Search',
			'callback_lnk': 'Callbak',
		}
	},
  ru: { message: { 
			'hello1': 'привет 1 мир',
			'menu_services': 'Услуги',
			'menu_booking': 'Запись',
			'menu_doctors': 'Врачи',
			'menu_contacts': 'Контакты',
			'search_ph': 'Найти',
			'callback_lnk': 'Заказать звонок',
		}
	},
}

// Create VueI18n instance with options
const i18n = new VueI18n({
  locale: 'ru', // set locale
  messages // set locale messages
})


new Vue({
  i18n,
  router,
  store,
   render: h => h(App),
}).$mount('#app')

