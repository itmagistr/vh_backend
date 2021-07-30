import Vue from 'vue';
import App from '@/App.vue';
import router from "@/router";
import store from "@/store";
import VueMeta from 'vue-meta';
import VueI18n from 'vue-i18n';
import VueSplide from '@splidejs/vue-splide';
import '@splidejs/splide/dist/css/themes/splide-sea-green.min.css';
import { VueReCaptcha } from 'vue-recaptcha-v3'

Vue.use(VueReCaptcha, { siteKey: '6Ldwx8cbAAAAAKd8-Y96OBm9pISwHFmfx5hEfcfy' })
Vue.use(require('vue-cookies'));
Vue.use(VueSplide);
Vue.use(VueMeta)
Vue.use(VueI18n)

Vue.config.productionTip = false

import { config } from '@/locales'

const i18n = new VueI18n(config)

new Vue({
  i18n,
  router,
  store,
  render: h => h(App),
  async created() {
    await this.$recaptchaLoaded().then(() => {
      const recaptcha = this.$recaptchaInstance;
      recaptcha.hideBadge();
    });
  },
}).$mount('#app')

