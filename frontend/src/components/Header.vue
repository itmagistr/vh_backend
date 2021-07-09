<template>
  <header>
    <nav v-if="resize === false" class="navbar navbar-expand-xl navbar-light">
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav hract">
          <li class="nav-item" :id="[$route.name === 'service' ? 'active' : '']">
            <hr>
            <router-link class="nav-link" :to="{name: 'service'}">{{ $t('menu.services') }}</router-link>
            <hr>
          </li>
          <li class="nav-item" :id="[$route.name === 'booking' ? 'active' : '']">
            <hr>
            <a class="nav-link active" data-toggle="modal" data-target="#mdl-future-ok" >{{ $t('menu.booking') }}</a>
            <hr>
          </li>
          <li class="nav-item" :id="[$route.name === 'doctors' ? 'active' : '']">
            <hr>
            <router-link class="nav-link" :to="{name: 'doctors'}">{{ $t('menu.doctors') }}</router-link>
            <hr>
          </li>
          <li class="nav-item">
            <hr>
            <a href="#" class="nav-link" data-toggle="modal" data-target="#mdl-future-ok" data-name="тур">{{ $t('menu.virtual_tour') }}</a>
            <hr>
          </li>
          <li class="nav-item" :id="[$route.name === 'documents' ? 'active' : '']">
            <hr>
             <router-link class="nav-link" :to="{name: 'documents'}" data-name="докум">{{ $t('menu.documentation') }}</router-link>
            <hr>
          </li>
          <li class="nav-item">
            <hr>
            <a href="#" class="nav-link" data-toggle="modal" data-target="#mdl-contacts">{{ $t('menu.contacts') }}</a>
            <hr>
          </li>
        </ul>
        <ul class="navbar-nav"><router-link :to="{name: 'main'}"><img class="logo" src="/img/logo-sm.svg"/></router-link></ul>
        <ul class="navbar-nav rightM">
          <li class="nav-item">
            <div class="input-group">
              <input v-model='q' type="text" class="form-control" :placeholder="$t('menu.search_ph')" aria-describedby="ba2">
              <div class="input-group-append">
                <button class="btn" type="button" id="ba2" data-toggle="modal" data-target="#mdl-future-ok"><i class="fas fa-search"></i></button>
              </div>
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
          <li class="nav-item">
            <router-link class="nav-link" to="#"><h6 id="profile_field">{{ $t('menu.profile')}} </h6> <i class="fas fa-user"></i></router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link number" href="https://api.whatsapp.com/send?phone=79096952043" target="_blank">{{ $t('menu.phone_num')}}</a>
            <a class="nav-link" href="#" id="order-call" data-toggle="modal" data-target="#mdl-call-back">{{ $t('menu.callback_lnk')}}</a>
          </li>
        </ul>
      </div>
    </nav>
    <nav v-if="resize === true" class="navbar navbar-light">
      <button class="navbar-toggler" type="button" data-toggle="modal" data-target="#mdlm-menu">
        <i class="fas fa-bars"></i>
      </button>
      <router-link :to="{name: 'main'}"><img class="mobile logo" src="/img/logo-sm.svg"/></router-link>
      <label class="seaF" for="searchfField" :class="{active: isActive}">
<!--    <input @blur="handleBlur" @focus="handleFocus" id="searchfField" type="text" v-model="q"
        data-toggle="modal" data-target="#mdl-future-ok"/>-->
        <input @blur="handleBlur" @focus="handleFocus" id="searchfField" type="text" v-model="q" @keyup="search"/>
      </label>
    </nav>
  </header>
</template>

<script>
export default {
  props: ['resize'],
  data() {
    return {
      locale: this.$i18n.locale,
      q: '',
      isActive: false,
      res: [],
    }
  },
  created() {
    if(this.$cookies.get('lang')) {
      this.locale = this.$cookies.get('lang');
      this.$i18n.locale = this.$cookies.get('lang');
    } else {
      this.$cookies.set("lang", this.$i18n.locale);
    }
  },
  methods: {
    handleFocus() {
      this.isActive = true;
    },
    handleBlur() {
      if(this.q.length === 0)
        this.isActive = false;
    },
    chLang(locale) {
      this.locale = locale;
      this.$i18n.locale = locale;
      this.$cookies.set("lang", locale);
    },
    search() {
      return new Promise(() => {
        // if (this.q.length < 3) {
        //   return resolve([]);
        // }

        const options = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({"q": this.q})
        };
        fetch(`http://localhost:8000/${this.$i18n.locale}/vhapi/mpsearch/`, options).
        then(response => response.json()).
        then(data => {
          this.res = data;
        }).
        catch((error) => { console.log(error); this.results = null;}).
        finally(() => {
          console.log(this.res)
          this.loading = false;
        });
        return false;
      });
    },
  }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

$heightHeader: 136px

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

.navbar-light a, .navbar-light, .bg-light, .bg-light a
  font-family: FuturaBookC
  font-style: normal
  font-weight: normal
  font-size: 14px
  line-height: 21px
  letter-spacing: 0.05em
  color: $header_text!important

header
  background: rgba(254, 253, 251, 0.64)
  backdrop-filter: blur(32px)
  font-family: FuturaBookC
  > nav.navbar
    max-width: 1560px
    margin: auto
    height: $heightHeader
    > div
      justify-content: space-between
      > ul
        > a
          > img.logo
            width: 250px
        > li
          > a
            &#nDML
              font-size: 1rem
              text-transform: uppercase
              color: $button-color!important
            &#order-call
              text-align: right
              padding-top: .25rem
              color: $active-text-link!important
            &.number
              font-size: 21px!important
              line-height: 16px!important
              text-align: right
              padding-bottom: .25rem
            > h6#profile_field
              line-height: 21px
              margin-right: 8px
              display: inline-flex
        &.rightM
          align-items: center
        &.hract
          text-transform: uppercase
          height: $heightHeader
          > li
            display: flex
            flex-direction: column
            justify-content: space-between
            align-items: center
            > hr
              border: none
              background: transparent
              width: 40px
              height: 4px
              margin: 0
            &#active
              > hr
                background: #42e1c5
              > a
                color: $active-text-link!important
    .toggler
      display: none
      width: 100%
  .btn-outline
    color: $header_text
    background: $white

  .seaF
    height: 2rem
    width: 2rem
    transition: all 200ms ease
    cursor: text
    margin: 0
    &.active, &:hover
      width: 200px
      height: 2rem
      border-radius: 0.5rem
      border-width: 0
      background: $white
      box-shadow: 0 0 0 0.2rem rgba(184,136,47,.25)
      &:after
        height: 0px
    input
      background-color: transparent
      background: url('/img/search.svg') no-repeat scroll 5px 5px
      padding-left: 2rem
      height: 2rem
      width: 100%
      border: none
      box-sizing: border-box
      font-family: Helvetica
      font-size: 1rem
      color: inherit
      outline-width: 0px
      &.active, &:hover
        border: none
        box-shadow: none

.btn-outline
  &:hover
    color: $header_text

// Change standart color of input
.form-control
  border: none
  color: $header_text
  &::placeholder
    color: $header_text

.form-control, .social-btn
  &:focus, &:hover
    outline: 0
    box-shadow: 0 0 0 0.2rem rgba(184,136,47,.25)
    color: $header_text

#ba2
  background: #FFF
  > i
    transform: scaleX(-1)
    color: $header_text

@media (max-width: 1399px)
  .navbar-light
      color: $white
  header
    > nav.navbar
      height: 64px
      > i.fas.fa-search
        transform: scaleX(-1)
</style>
