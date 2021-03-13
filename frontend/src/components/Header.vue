<template>
    <header>
      <nav v-if="mobile === false" class="navbar navbar-expand-xl navbar-light">
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item" :id="[$route.name === 'service' ? 'active' : '']">
              <router-link class="nav-link" :to="{name: 'service'}">{{ $t('message.menu_services') }}</router-link>
            </li>
            <li class="nav-item" :id="[$route.name === 'booking' ? 'active' : '']">
              <router-link class="nav-link active" :to="{name: 'booking'}">{{ $t('message.menu_booking') }}</router-link>
            </li>
            <li class="nav-item" :id="[$route.name === 'doctors' ? 'active' : '']">
              <router-link class="nav-link" :to="{name: 'doctors'}">{{ $t('message.menu_doctors') }}</router-link>
            </li>
            <li class="nav-item">
              <a href="#" class="nav-link" data-toggle="modal" data-target="#mdl-future-ok" data-name="тур">{{ langList.MENU_TOUR.title }}</a>
            </li>
            <li class="nav-item">
              <a href="#" class="nav-link" data-toggle="modal" data-target="#mdl-future-ok" data-name="докум">{{ langList.MENU_DOCS.title }}</a>
            </li>
            <li class="nav-item">
              <a href="#" class="nav-link" data-toggle="modal" data-target="#mdl-contacts">{{ $t('message.menu_contacts') }}</a>
            </li>
          </ul>
          <ul class="navbar-nav mr-auto"><router-link :to="{name: 'main'}"><img class="logo" src="/img/logo-sm.svg"/></router-link></ul>
          <ul class="navbar-nav">
            <li class="nav-item">
              <div class="inner-addon right-addon">
                <i class="fas fa-search"></i>
                <input class="form-control" type="search" :placeholder="$t('message.search_ph')" aria-label="Search"/>
              </div>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="nDML" role="button" data-toggle="dropdown"
                 aria-haspopup="true" aria-expanded="false"> {{ lang | capitalize}} </a>
              <div class="dropdown-menu" aria-labelledby="nDML">
                <a class="dropdown-item" @click="chLang('ru')">Русский</a>
                <a class="dropdown-item" @click="chLang('en')">English</a>
              </div>
            </li>
          </ul>
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link class="nav-link" to="#">Профиль <i class="fas fa-user"></i></router-link>
            </li>
          </ul>
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link number" href="https://api.whatsapp.com/send?phone=79684208413" target="_blank">+7 900 881 88 88</a>
              <a class="nav-link" href="#" id="order-call" data-toggle="modal" data-target="#mdl-call-back">{{ $t('message.callback_lnk')}}</a>
            </li>
          </ul>
        </div>
      </nav>
        <nav v-if="mobile === true" class="navbar navbar-light">
          <button class="navbar-toggler" type="button" data-toggle="modal" data-target="#mdlm-menu">
            <i class="fas fa-bars"></i>
          </button>
          <ul class="navbar-nav"><router-link :to="{name: 'main'}"><img class="mobile logo" src="/img/logo-sm.svg"/></router-link></ul>
          <ul class="navbar-nav">
            <li class="nav-item">
                <i class="fas fa-search"></i>
            </li>
          </ul>
        </nav>
    </header>
</template>

<script>
export default {
  data() {
    this.$i18n.locale = 'ru';
    return {
      lang: this.$store.state.lang,
      langList: null,
      mobile: null,
      locale: 'ru'
    }
  },
  mounted(){

  },
  filters: {
    capitalize: function (value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    }
  },
  methods: {
    onResize() {
      this.mobile = document.documentElement.clientWidth > 1399 ? false : true;
    },
    chLang(lang){
      this.$store.commit("updLang", lang);
      this.lang = lang;
      this.$i18n.locale = lang
      //this.langMenu();
    },
    langMenu() {
      const options = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({code: 'HEADER_MENU'})
      };
      fetch(`http://localhost:8000/${this.lang}/vhapi/dictstr/list/`, options).
      then(response => response.json()).
      then(data => {
        this.results = data;
      }).
      catch((error) => { console.log(error); this.results = null;}).
      finally(() => {
        this.langList = this.results;
      });
    },
  },
  created() {
    window.addEventListener('resize', this.onResize);
    this.langMenu();
    this.onResize();
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize);
  },
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"


.dropdown-submenu
  position: relative
  a::after
    transform: rotate(-90deg)
    position: absolute
    right: 6px
    top: .8em
  .dropdown-menu
    top: 0
    left: 100%
    margin-left: .1rem
    margin-right: .1rem

header
  background: rgba(254, 253, 251, 0.64)
  backdrop-filter: blur(32px)

.logo
  width: 250px

#order-call
  text-align: right
  color: $active-text-link!important

#active > a
  color: $active-text-link!important

.navbar-light a, .navbar-light, .bg-light, .bg-light a
  font-family: FuturaBookC
  font-style: normal
  font-weight: normal
  font-size: 14px
  line-height: 21px
  letter-spacing: 0.05em
  color: $header_text!important


.mr-auto a
  text-transform: uppercase

nav
  max-width: 1560px
  margin: auto
  height: 136px
  .toggler
    display: none
    width: 100%
.btn-outline
  color: $header_text
  background: #FFF

.btn-outline
  &:hover
    color: $header_text



// Change standart color of input
.form-control
  border: none
  color: $header_text
  &::placeholder
    color: $header_text

.btn.focus, .btn, .social-btn
  &:focus
    outline: 0
    box-shadow: 0 0 0 0.2rem rgba(184,136,47,.25)

.form-control, .social-btn
  &:focus, &:hover
    outline: 0
    box-shadow: 0 0 0 0.2rem rgba(184,136,47,.25)
    color: $header_text

.inner-addon
  position: relative

.inner-addon .fas
  position: absolute
  padding: 12px
  pointer-events: none
  transform: scaleX(-1)

.right-addon .fas
  right: 0px

.right-addon input
  padding-right: 30px

.number
  font-size: 21px!important
  line-height: 16px!important
  text-align: right

.right-side
  position: absolute
  right: 7.3%
  top: 304px

@media (max-width: 1399px)
  .navbar-light
      color: $white
  nav
    font-family: FuturaBookC
    font-size: 27px
    line-height: 33px
    text-align: center
    height: 64px
</style>
