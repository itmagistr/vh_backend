<template>
    <div class="modal fade" id="mdlm-menu" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog modal-ctm modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button class="navbar-toggler" type="button" data-toggle="modal" data-target="#mdlm-menu">
              <i class="fas fa-bars"></i>
            </button>
            <ul>
              <li class="dropdown">
                <a class="dropdown-toggle" href="#" id="nDML" role="button" data-toggle="dropdown"
                   aria-haspopup="true" aria-expanded="false"> {{ locale }} </a>
                <div class="dropdown-menu" aria-labelledby="nDML">
                  <a class="dropdown-item" @click="chLang('ru')">Русский</a>
                  <a class="dropdown-item" @click="chLang('en')">English</a>
                </div>
              </li>
              <li>
                <router-link to="#" custom v-slot="{ navigate }">
                  <a @click="navigate" class="nav-link" @keypress.enter="navigate">{{ $t('menu.profile') }} <i class="fas fa-user"></i></a>
                </router-link>
              </li>
            </ul>
          </div>
          <div class="modal-body">
            <ul class="navbar-nav mr-auto">
              <li class="nav-item" :id="[$route.name === 'service' ? 'active' : '']">
                <router-link to="/service" custom v-slot="{ navigate }">
                  <a @click="navigate" class="nav-link" data-dismiss="modal" @keypress.enter="navigate">{{ $t('menu.services') }}</a>
                </router-link>
              </li>
              <li class="nav-item" :id="[$route.name === 'booking' ? 'active' : '']">
                <router-link to="#" custom v-slot="{ navigate }">
                  <a @click="navigate" class="nav-link" data-toggle="modal" data-dismiss="modal" data-target="#mdl-future-ok" @keypress.enter="navigate">{{ $t('menu.booking') }}</a>
                </router-link>
              </li>
              <li class="nav-item" :id="[$route.name === 'doctors' ? 'active' : '']">
                <router-link to="/doctors" custom v-slot="{ navigate }">
                  <a @click="navigate" class="nav-link" data-dismiss="modal" @keypress.enter="navigate">{{ $t('menu.doctors') }}</a>
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/virtual_tour" custom v-slot="{ navigate }">
                  <a @click="navigate" class="nav-link" data-dismiss="modal" @keypress.enter="navigate">{{ $t('menu.virtual_tour') }}</a>
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/documents" custom v-slot="{ navigate }">
                  <a @click="navigate" class="nav-link" data-dismiss="modal" @keypress.enter="navigate">{{ $t('menu.documentation') }}</a>
                </router-link>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-toggle="modal" data-dismiss="modal" data-target="#mdl-contacts">{{ $t('menu.contacts') }}</a>
              </li>
            </ul>
          </div>
          <div class="modal-footer">
            <div class="number">
              <a class="nav-link" href="#">{{ $t('menu.phone_num') }}</a>
              <a class="nav-link" href="#" data-toggle="modal" data-dismiss="modal" data-target="#mdl-call-back">{{ $t('menu.callback_lnk')}}</a>
            </div>
            <router-link to="/" custom v-slot="{ navigate }">
              <img @click="navigate" @keypress.enter="navigate" class="logo" data-dismiss="modal" src="/img/logo_light.svg"/>
            </router-link>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import capitalize from '@/helpers/capitalizeFormat';

export default {
  props: ['resize'],
  data() {
    return {
      locale: this.$i18n.locale,
    }
  },
  filters: {
    capitalize,
  },
  created() {
    if(this.resize)
      if(this.$cookies.get('lang')) {
        this.locale = this.$cookies.get('lang');
        this.$i18n.locale = this.$cookies.get('lang');
      } else {
        this.$cookies.set("lang", this.$i18n.locale);
      }
  },
  methods: {
    chLang(locale) {
      this.locale = locale;
      this.$i18n.locale = locale;
      this.$cookies.set("lang", locale);
    },
  },
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.navbar-light
  > .navbar-toggler
    color: #EED199
    border: none
    padding: .5rem .75rem

#mdlm-menu
  .modal-ctm
    margin: 0px
    display: block
    max-width: 481px
    border-radius: 0px 0px 8px 0px
    > .modal-content
      > .modal-header
        > .navbar-toggler
          color: $white
    > div
      border: none
      .modal-header, .modal-footer
        border: none
      .modal-body, .modal-footer
        text-align: center
        display: block
        padding: 0
        line-height: 33px
        letter-spacing: 0.05em
        font-size: 27px
      .modal-footer
        border-radius: 0 0 8px 0
        .number
          margin-top: 48px
          margin-bottom: 52px
          text-align: center
          > a
            color: #FEFDFB!important
            &:first-child
              font-size: 2rem
            &:last-child
              font-size: 1rem
              line-height: 21px
        .logo
          width: auto
          margin-bottom: 82px
      .modal-header
        height: 66px
        > ul
          display: inline-flex
          list-style: none
          > li
            padding: .5rem .5rem
            > a
              color: #FEFDFB!important
            > #nDML
              font-size: 1rem
              text-transform: uppercase
      > div
        background: #42E1C5
        &.modal-body
          > ul
            > li
              height: 56px
              padding: 16px
              margin: 9px 0px
              > a
                padding: 0px
                color: #FEFDFB!important
              &#active, &:hover
                background: #EED199
@media (max-width: 1399px)
  .modal-backdrop
    background: rgba(254, 253, 251, 0.64)

@media (max-width: 450px)
  .mobile.logo
    width: 145px
  #mdlm-menu
    > .modal-ctm
      height: 100%
      border-radius: 0px
      > .modal-content
        height: 100%
        > .modal-header
          > .navbar-toggler
            color: $white
        > .modal-footer
          border-radius: 0px!important
      > div > div.modal-body > ul > li
        height: 45px
        padding: 10px
        margin: 6px 0px
</style>
