<template>
  <main>
    <TheHeader :resize="false"/>
    <Nuxt :resize="false"/>
  </main>
</template>

<script>
export default {

}
</script>


<style lang="sass">
@import "~/styles/_variables.sass"
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap')

@font-face
  font-family: "FuturaBookC"
  font-style: normal
  src: local("FuturaBookC"), url('~/assets/fonts/FuturaBookC/e05b78cd627ded97c38881306e3601fe.eot')
  src: url('~/assets/fonts/FuturaBookC/e05b78cd627ded97c38881306e3601feiefix.eot') format('embedded-opentype'), url('~/assets/fonts/FuturaBookC/e05b78cd627ded97c38881306e3601fe.woff2') format("woff2"), url('~/assets/fonts/FuturaBookC/e05b78cd627ded97c38881306e3601fe.woff') format("woff"), url('~/assets/fonts/FuturaBookC/e05b78cd627ded97c38881306e3601fe.ttf') format("truetype"), url('~/assets/fonts/FuturaBookC/e05b78cd627ded97c38881306e3601fe.svg') format("svg")

html, body
  height: 100%
  width: 100%

body
  font-family: FuturaBookC, serif
  background: url('~/assets/img/img1.png') no-repeat center center fixed
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
  margin: 12px 0
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
      margin: 0
      > .modal-content
        border-radius: 0

@media screen and (min-width: 1200px)
  .container
    max-width: 1640px

@media screen and (max-width: 1200px)
  .container
    max-width: none

@media screen and (max-width: 768px)
  body.mainP
    .container
      >.d-flex
        >.d-flex
          &:first-child, &:last-child
            display: none!important
    footer
      display: flex
</style>