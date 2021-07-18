<template>
  <body :class="[$route.name === 'doctors' ? 'chg-doc' : '',
  $route.name === 'service' ? 'chg-proc' : '',
  $route.name === 'documents' ? 'documGal' : '',
  $route.name === 'virtualtour' ? 'tour' : '',
  $route.name === 'main' ? 'mainP' : '',
  $route.name === 'booking' ? 'booking' : '']">
    <noscript>
      <strong>We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled.
        Please enable it to continue.</strong>
    </noscript>
    <Header :resize="mobile" v-if="$route.name !== 'ComingSoon'"/>
    <main v-if="$route.name !== 'ComingSoon'">
      <div class="container">
        <modalMessenger/>
        <modalContact/>
        <modalLeaveRequest/>
        <modalFutureOk/>
        <modalCallBack/>
        <modalImage/>
        <modalMobileMenu v-if="mobile === true" :resize="mobile"/>
        <div class="d-flex align-items-center justify-content-between">
          <div class="d-flex flex-column ctm-col-rt col">
            <a href="https://www.instagram.com/tohwddent" target="_blank"><button class="social-btn"><i class="fab fa-instagram"></i></button></a>
            <a href="https://www.youtube.com/channel/UCeyxKBqdLFA79kCTH29RDsQ" target="_blank"><button class="social-btn"><i class="fab fa-youtube"></i></button></a>
            <a href="https://www.facebook.com/ToHwdDent" target="_blank"><button class="social-btn"><i class="fab fa-facebook-f"></i></button></a>
            <a href="https://vk.com/tohwddent" target="_blank"><button class="social-btn"><i class="fab fa-vk"></i></button></a>
          </div>
          <router-view :resize="mobile" :class="[$route.name !== 'booking' ? 'col' : '']"/>
          <div class="d-flex flex-column ctm-col-lt col">
            <button class="social-btn" data-toggle="modal" data-target="#mdl-leave-request"><i class="far fa-comment-alt"></i></button>
            <button class="social-btn" data-toggle="modal" data-target="#mdl-contacts"><i class="fas fa-map-marker-alt"></i></button>
            <!--<button class="social-btn"><i class="fas fa-route"></i></button>-->
            <button class="social-btn" data-toggle="modal" data-target="#mdl-call-back"><i class="fas fa-phone-alt"></i></button>
            <a href="https://api.whatsapp.com/send?phone=79096952043" target="_blank"><button class="social-btn"><i class="fab fa-whatsapp"></i></button></a>
          </div>
        </div>
      </div>
    </main>
    <footer v-if="$route.name !== 'ComingSoon'">
      <div class="ftr-btn">
        <a href="https://www.instagram.com/tohwddent" target="_blank"><button class="social-btn"><i class="fab fa-instagram"></i></button></a>
        <a href="https://www.youtube.com/channel/UCeyxKBqdLFA79kCTH29RDsQ" target="_blank"><button class="social-btn"><i class="fab fa-youtube"></i></button></a>
        <a href="https://www.facebook.com/ToHwdDent" target="_blank"><button class="social-btn"><i class="fab fa-facebook-f"></i></button></a>
        <a href="https://vk.com/tohwddent" target="_blank"><button class="social-btn"><i class="fab fa-vk"></i></button></a>
      </div>
      <div class="ftr-btn">
        <a href="#"><button class="social-btn" data-toggle="modal" data-target="#mdl-leave-request"><i class="far fa-comment-alt"></i></button></a>
        <a href="#"><button class="social-btn" data-toggle="modal" data-target="#mdl-contacts"><i class="fas fa-map-marker-alt"></i></button></a>
        <!--<button class="social-btn"><i class="fas fa-route"></i></button>-->
        <a href="#"><button class="social-btn" data-toggle="modal" data-target="#mdl-call-back"><i class="fas fa-phone-alt"></i></button></a>
        <a href="https://api.whatsapp.com/send?phone=79096952043" target="_blank"><button class="social-btn"><i class="fab fa-whatsapp"></i></button></a>
      </div>
    </footer>
    <router-view v-if="$route.name === 'ComingSoon'"/>
  </body>
</template>

<script>
import Header from "@/components/Header.vue";
import modalContact from "@/components/ModalContact.vue";
import modalCallBack from "@/components/ModalCallBack.vue";
import modalLeaveRequest from "@/components/ModalLeaveRequest.vue";
import modalFutureOk from "@/components/ModalFutureOk.vue";
import modalMobileMenu from "@/components/ModalMobileMenu.vue"
import modalMessenger from "@/components/ModalMessenger.vue"
import modalImage from "@/components/ModalImage";
export default {
  name: 'App',
    metaInfo() {
      return {
        title: this.$t('meta.title'),
        meta: [
          { name: 'description', content:  this.$t('meta.description')},
          { name: 'keywords', content: this.$t('meta.keywords')},
          { property: 'og:title', content: this.$t('og.title')},
          { property: 'og:site_name', content: this.$t('og.sitename')},
          { property: 'og:description', content: this.$t('og.description')},
          { property: 'og:type', content: 'website'},
          { property: 'og:locale', content: this.$t('og.locale')},
          { name: 'robots', content: 'index,follow'}
        ]
      }
    },
  data() {
    return {
      mobile: null,
    }
  },
  methods: {
    onResize() {
      this.mobile = document.documentElement.clientWidth <= 1399;
    },
  },
  created() {
    this.$i18n.locale = navigator.language.slice(0,2) || navigator.userLanguage.slice(0,2);
    window.addEventListener('resize', this.onResize);
    this.onResize();
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize);
  },
  components: { Header, modalContact, modalLeaveRequest, modalFutureOk, modalCallBack, modalMobileMenu, modalMessenger, modalImage },
};

</script>

<style lang="sass">
@import "@/styles/_variables.sass"
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

@font-face
  font-family: "FuturaBookC"
  font-style: normal
  src: local("FuturaBookC"),
  url("./fonts/FuturaBookC/e05b78cd627ded97c38881306e3601fe.eot")
  src: url("./fonts/FuturaBookC/e05b78cd627ded97c38881306e3601feiefix.eot") format("embedded-opentype"),
  url("./fonts/FuturaBookC/e05b78cd627ded97c38881306e3601fe.woff2") format("woff2"),
  url("./fonts/FuturaBookC/e05b78cd627ded97c38881306e3601fe.woff") format("woff"),
  url("./fonts/FuturaBookC/e05b78cd627ded97c38881306e3601fe.ttf") format("truetype"),
  url("./fonts/FuturaBookC/e05b78cd627ded97c38881306e3601fe.svg") format("svg")

//@font-face
//  font-family: 'Montserrat'
//  font-style: normal
//  font-weight: 400
//  src: local("Montserrat"),
//  url('./fonts/Montserrat/montserrat-v15-latin_cyrillic-regular.eot')
//  src: url('./fonts/Montserrat/montserrat-v15-latin_cyrillic-regular.eot?#iefix'), format('embedded-opentype'),
//  url('./fonts/Montserrat/montserrat-v15-latin_cyrillic-regular.woff2') format('woff2'),
//  url('./fonts/Montserrat/montserrat-v15-latin_cyrillic-regular.woff') format('woff'),
//  url('./fonts/Montserrat/montserrat-v15-latin_cyrillic-regular.ttf') format('truetype'),
//  url('./fonts/Montserrat/montserrat-v15-latin_cyrillic-regular.svg#Montserrat') format('svg')

html, body
  height: 100%
  width: 100%

body
  font-family: FuturaBookC, serif
  background: url('/img/img1.png') no-repeat center center fixed
  background-size: cover
::-webkit-scrollbar
  display: none

.container
  .ctm-col-lt
    align-items: flex-end
.social-btn
  display: block
  width: 64px
  height: 64px
  background: rgba(254, 253, 251, 0.64)!important
  backdrop-filter: blur(24px)!important
  border: none
  border-radius: 4px
  color: $header_text
  font-size: 22px
  margin: 12px 0px
.btn:hover
  box-shadow: 0 0 0 0.2rem #b8882f40
.logo
    font-family: Josefin Sans
    font-style: normal
    font-weight: 300
    font-size: 28.925px
    line-height: 29px
    color: #000
    position: relative
    text-align: center
footer
  padding-top: 3rem
  padding-bottom: 3.5rem
  display: none
  flex-direction: column
  align-items: center
  > .ftr-btn
    display: flex
    justify-content: center
    > a
      margin: .5rem
      > .social-btn
        margin: 0

@media screen and (max-width: 1399px)
  /*header
    display: none*/
  body:not(.mainP)
    .container
      >.d-flex
        >.d-flex
          &:first-child, &:last-child
            display: none!important
    footer
      display: flex
  #mdl-contacts
    > .modal-ctm
      max-width: 100%
      min-height: 100%
      margin: 0px
      > .modal-content
        border-radius: 0px

@media screen and (min-width: 1200px)
  .container
    max-width: 1640px

@media screen and (max-width: 1200px)
  .container
    max-width: none
</style>
