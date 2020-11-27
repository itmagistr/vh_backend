<template>
  <body>
    <noscript>
      <strong>We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled.
        Please enable it to continue.</strong>
    </noscript>
    <Header></Header>
    <main class="container">
      <modalContact/>
      <modalLeaveRequest/>
      <modalCallBack/>
      <div class="d-flex align-items-center justify-content-between">
        <div class="d-flex flex-column">
          <a href="https://www.instagram.com/inessa_braginskaia/" target="_blank"><button class="social-btn"><i class="fab fa-instagram"></i></button></a>
          <a href="https://www.youtube.com/channel/UCQ5YCpgwVDsr1mTU0bsKNaQ" target="_blank"><button class="social-btn"><i class="fab fa-youtube"></i></button></a>
          <a href="https://www.facebook.com/inessa.karahanyan/" target="_blank"><button class="social-btn"><i class="fab fa-facebook-f"></i></button></a>
          <button class="social-btn"><i class="fab fa-vk"></i></button>
        </div>
        <router-view/>
        <div class="d-flex flex-column">
          <button class="social-btn" data-toggle="modal" data-target="#mdl-leave-request"><i class="far fa-comment-alt"></i></button>
          <button class="social-btn"><i class="fas fa-map-marker-alt"></i></button>
          <button class="social-btn"><i class="fas fa-route"></i></button>
          <button class="social-btn" data-toggle="modal" data-target="#mdl-call-back"><i class="fas fa-phone-alt"></i></button>
          <button class="social-btn"><i class="fab fa-telegram-plane"></i></button>
        </div>
      </div>
    </main>
  </body>
</template>

<script>
import Header from "@/components/Header.vue";
import modalContact from "@/components/ModalContact.vue";
import modalCallBack from "@/components/ModalCallBack.vue";
import modalLeaveRequest from "@/components/ModalLeaveRequest.vue";

export default {
  components: { Header, modalContact, modalLeaveRequest, modalCallBack },
};
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

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

@media screen and (max-width: 1400px)
  header
    display: none

@media screen and (max-width: 991px)
  .registration
    display: none

@media screen and (min-width: 1200px)
  .container
    max-width: 1560px

@media screen and (max-width: 1200px)
  .container
    max-width: none
</style>