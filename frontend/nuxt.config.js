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
      { rel: 'stylesheet', href: "https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" }
    ],
    script: [
      { src: "https://code.jquery.com/jquery-3.5.1.slim.min.js" },
      { src: "https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" },
      { src: "https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" },
      { src: "https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" },
      { src: "https://kit.fontawesome.com/b17c92d058.js" }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css:[
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: '~/plugins/ymapPlugin.js',  mode: 'client' }
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
    '@nuxtjs/i18n',
    'cookie-universal-nuxt'
  ],
    i18n: {
      locales: [
        {
          code: 'en',
          file: 'en-US.js'
        },
        {
          code: 'ru',
          file: 'ru-RU.js'
        },
      ],
      langDir: 'assets/locales/',
      defaultLocale: 'ru',
      vueI18n: {
        fallbackLocale: 'en',
      }
  },
  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {},

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}
