<template>
  <header>
    <nav v-if="resize === false" class="navbar navbar-expand-xl navbar-light">
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item" :id="[$route.name === 'service' ? 'active' : '']">
            <router-link class="nav-link" :to="{name: 'service'}">{{ $t('menu.services') }}</router-link>
          </li>
          <li class="nav-item" :id="[$route.name === 'booking' ? 'active' : '']">
            <router-link class="nav-link active" :to="{name: 'booking'}">{{ $t('menu.booking') }}</router-link>
          </li>
          <li class="nav-item" :id="[$route.name === 'doctors' ? 'active' : '']">
            <router-link class="nav-link" :to="{name: 'doctors'}">{{ $t('menu.doctors') }}</router-link>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link" data-toggle="modal" data-target="#mdl-future-ok" data-name="тур">{{ $t('menu.virtual_tour') }}</a>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link" data-toggle="modal" data-target="#mdl-future-ok" data-name="докум">{{ $t('menu.documentation') }}</a>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link" data-toggle="modal" data-target="#mdl-contacts">{{ $t('menu.contacts') }}</a>
          </li>
        </ul>
        <ul class="navbar-nav mr-auto"><router-link :to="{name: 'main'}"><img class="logo" src="/img/logo-sm.svg"/></router-link></ul>
        <ul class="navbar-nav">
          <li class="nav-item">
            <div class="inner-addon right-addon">
              <i class="fas fa-search" aria-hidden="true" data-toggle="modal" data-target="#mdl-future-ok"></i>
              <input class="form-control" type="search" :placeholder="$t('menu.search_ph')" aria-label="Search"/>
            </div>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="nDML" role="button" data-toggle="dropdown"
               aria-haspopup="true" aria-expanded="false"> {{ locale }} </a>
            <div class="dropdown-menu" aria-labelledby="nDML">
              <a class="dropdown-item" @click="chLang('ru')">Русский</a>
              <a class="dropdown-item" @click="chLang('en')">English</a>
            </div>
          </li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class="nav-link" to="#"><h6 id="profile_field">{{ $t('menu.profile')}} </h6> <i class="fas fa-user"></i></router-link>
          </li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link number" href="https://api.whatsapp.com/send?phone=74950238669" target="_blank">+7 495 023 86 69</a>
            <a class="nav-link" href="#" id="order-call" data-toggle="modal" data-target="#mdl-call-back">{{ $t('menu.callback_lnk')}}</a>
          </li>
        </ul>
      </div>
    </nav>
    <nav v-if="resize === true" class="navbar navbar-light">
      <button class="navbar-toggler" type="button" data-toggle="modal" data-target="#mdlm-menu">
        <i class="fas fa-bars"></i>
      </button>
      <ul class="navbar-nav"><router-link :to="{name: 'main'}"><img class="mobile logo" src="/img/logo-sm.svg"/></router-link></ul>
      <ul class="navbar-nav">
        <li class="nav-item">
            <i class="fas fa-search" data-toggle="modal" data-target="#mdl-future-ok"></i>
        </li>
      </ul>
    </nav>
  </header>
</template>

<script>

export default {
  props: ['resize'],
  data() {
    return {
      locale: this.$i18n.locale,
    }
  },
  methods: {
    chLang(locale){
      this.locale = locale;
      this.$i18n.locale = locale;
    },
  }
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
  #nDML
    font-size: 1rem
    text-transform: uppercase
    color: $button-color!important
  h6#profile_field
    line-height: 21px
    margin-right: 8px
    display: inline
.logo
  width: 250px

#order-call
  text-align: right
  padding-top: .25rem
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
  .fas
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
  padding-bottom: .25rem

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
