export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'nuxtFrontEnd',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'stylesheet', href: "https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" }, 
      { rel: 'stylesheet', href: "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" },
      { rel: 'preload', as: 'script', href: "https://code.jquery.com/jquery-3.5.1.slim.min.js" },
      { rel: 'preload', as: 'script', href: "https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" },
      { rel: 'preload', as: 'script', href: "https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" },
      { rel: 'preload', as: 'script', href: "https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" },
      { rel: 'preload', as: 'script', href: "https://kit.fontawesome.com/b17c92d058.js" }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css:[
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/i18n'
  ],
    i18n: {
      locales: ['en', 'ru'],
      defaultLocale: 'ru',
      vueI18n: {
        fallbackLocale: 'en',
        locales: {
          en: '~/assets/locales/en.json',
          ru: '~/assets/locales/ru.json'
        }
      }
  },
  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {},

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}
