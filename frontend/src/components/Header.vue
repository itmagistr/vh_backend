<template>
  <header>
    <nav v-if="resize === false" class="navbar navbar-expand-xl navbar-light">
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav hract">
          <li class="nav-item" :id="[$route.name === 'service' ? 'active' : '']">
            <hr>
            <router-link to="/service" custom v-slot="{ navigate }">
              <a href="#" @click="navigate" class="nav-link" @keypress.enter="navigate">{{ $t('menu.services') }}</a>
            </router-link>
            <hr>
          </li>
          <li class="nav-item" :id="[$route.name === 'booking' ? 'active' : '']">
            <hr>
            <router-link to="#" custom v-slot="{ navigate }">
              <a href="#" @click="navigate" class="nav-link" @keypress.enter="navigate" data-toggle="modal" data-target="#mdl-future-ok">{{ $t('menu.booking') }}</a>
            </router-link>
            <hr>
          </li>
          <li class="nav-item" :id="[$route.name === 'doctors' ? 'active' : '']">
            <hr>
            <router-link to="/doctors" custom v-slot="{ navigate }">
              <a href="#" @click="navigate" class="nav-link" @keypress.enter="navigate">{{ $t('menu.doctors') }}</a>
            </router-link>
            <hr>
          </li>
          <li class="nav-item" :id="[$route.name === 'virtualtour' ? 'active' : '']">
            <hr>
            <router-link to="/virtual_tour" custom v-slot="{ navigate }">
              <a href="#" @click="navigate" class="nav-link" @keypress.enter="navigate">{{ $t('menu.virtual_tour') }}</a>
            </router-link>
            <hr>
          </li>
          <li class="nav-item" :id="[$route.name === 'documents' ? 'active' : '']">
            <hr>
            <router-link to="/documents" custom v-slot="{ navigate }">
              <a href="#" @click="navigate" class="nav-link" @keypress.enter="navigate">{{ $t('menu.documentation') }}</a>
            </router-link>
            <hr>
          </li>
          <li class="nav-item">
            <hr>
            <a href="#" class="nav-link" data-toggle="modal" data-target="#mdl-contacts">{{ $t('menu.contacts') }}</a>
            <hr>
          </li>
        </ul>
        <ul class="navbar-nav">
          <router-link to="/" custom v-slot="{ navigate }">
            <img @click="navigate" @keypress.enter="navigate" class="logo" src="/img/logo-sm.svg"/>
          </router-link>
        </ul>
        <ul class="navbar-nav rightM">
          <li class="nav-item">
            <div class="search-field" :class="{active: isActive}">
              <input v-model='q' type="text" class="form-control"
                     :placeholder="$t('menu.search_ph')" @keyup.enter="search">
              <button @click="clear" v-show="q.length !== 0 && isActive" class="btn close-search-btn">
                <i class="bi bi-x"></i>
              </button>
              <button class="btn search-btn" type="button" @click="search">
                <i class="fas fa-search"></i>
              </button>
              <div class="search-result" v-show="isActive">
                <div class="result" v-for="(n, idx) in res" :key="n.uid" @click="underground(idx)">{{n.title}}</div>
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
            <router-link to="#" custom v-slot="{ navigate }">
              <a @click="navigate" class="nav-link" @keypress.enter="navigate">{{ $t('menu.profile') }} <i class="fas fa-user"></i></a>
            </router-link>
          </li>
          <li class="nav-item">
            <span class="number">{{ $t('menu.phone_num')}}</span>
            <a class="nav-link" href="#" id="order-call" data-toggle="modal" data-target="#mdl-call-back">{{ $t('menu.callback_lnk')}}</a>
          </li>
        </ul>
      </div>
    </nav>
    <nav v-if="resize === true" class="navbar navbar-light">
      <button class="navbar-toggler" type="button" data-toggle="modal" data-target="#mdlm-menu">
        <i class="fas fa-bars"></i>
      </button>
      <router-link to="/" custom v-slot="{ navigate }">
        <img @click="navigate" @keypress.enter="navigate" class="mobile logo" src="/img/logo-sm.svg"/>
      </router-link>
      <label class="seaF" for="searchfField" :class="{active: isActiveSearch, act: isActive}">
        <button class="btn search-btn" type="button" @click="search">
          <i class="fas fa-search"></i>
        </button>
        <input @blur="handleBlur" @focus="handleFocus" id="searchfField" type="text" v-model="q" @keyup.enter="search"/>
        <div class="search-result-mobile" v-show="isActive">
          <div class="result" v-for="(n, idx) in res" :key="n.uid" @click="underground(idx)">{{n.title}}</div>
        </div>
        <button @click="clear" v-show="q.length !== 0 && isActiveSearch" class="btn close-search-btn">
          <i class="bi bi-x"></i>
        </button>
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
      isActiveSearch: false,
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
    clear(){
      this.res = [];
      this.q = '';
      this.isActive = this.res.length !== 0;
      this.isActiveSearch = this.q.length !== 0;
    },
    underground(e) {
      console.log(this.res[e]);
    },
    handleFocus() {
      this.isActiveSearch = true;
    },
    handleBlur() {
      if(this.q.length === 0)
        this.isActiveSearch = false;
    },
    chLang(locale) {
      this.locale = locale;
      this.$i18n.locale = locale;
      this.$cookies.set("lang", locale);
    },
    search() {
      return new Promise(() => {
        if (this.q.length < 3) {
          return [];
        }

        const options = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({"q": this.q})
        };
        fetch(`${this.$store.state.apihost}${this.$i18n.locale}/vhapi/mpsearch/`, options).
        then(response => response.json()).
        then(data => {
          this.res = data;
        }).
        catch((error) => { console.log(error); this.results = null;}).
        finally(() => {
          console.log(this.res)
          this.loading = false;
          this.isActive = this.res.length !== 0;
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
    max-width: 1640px
    margin: auto
    height: $heightHeader
    > div
      justify-content: space-between
      > ul
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
          .search-field
            position: relative
            display: flex
            align-items: center
            input
              width: 210px
              padding-right: 3.25rem
            .close-search-btn
              position: absolute
              border: none
              right: 36px
              padding: .25rem 0
              font-size: 1.25rem
              z-index: 10
              color: $header_text
              &:hover
                box-shadow: none
            .search-btn
              position: absolute
              border: none
              right: 0
              font-size: 1.25rem
              z-index: 10
              padding: .375rem .5rem
              > i
                transform: scaleX(-1)
                color: $header_text
              &:hover
                box-shadow: none
            &.active
              > input
                border-radius: .5rem .5rem 0 0
              button
                border-radius: 0 .5rem 0 0
            > .search-result
              width: 210px
              height: 100px
              position: absolute
              background: #FEFDFB
              top: 38px
              border-radius: 0 0 .5rem .5rem
              overflow: auto
              > .result
                overflow: hidden
                white-space: nowrap
                text-overflow: ellipsis
                padding: .375rem .75rem
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
    display: flex
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
        height: 0
    &.act
      border-radius: .5rem .5rem 0 0
    .close-search-btn
      padding: .25rem 0
      font-size: 1.25rem
      z-index: 10
      color: $header_text
      &:hover
        box-shadow: none
    .search-btn
      font-size: 1.25rem
      z-index: 10
      padding: .375rem .5rem
      > i
        transform: scaleX(-1)
        color: $header_text
      &:hover
        box-shadow: none
    input
      height: 2rem
      width: 100%
      background: transparent
      border: none
      box-sizing: border-box
      font-family: Helvetica
      font-size: 1rem
      color: inherit
      outline-width: 0
    > .search-result-mobile
      width: 200px
      height: 100px
      position: absolute
      background: #FEFDFB
      top: 3rem
      border-radius: 0 0 .5rem .5rem
      overflow: auto
      > .result
        overflow: hidden
        white-space: nowrap
        text-overflow: ellipsis
        padding: .375rem .75rem
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

@media (max-width: 1399px)
  .navbar-light
      color: $white
  header
    > nav.navbar
      height: 64px
      > i.fas.fa-search
        transform: scaleX(-1)
</style>
