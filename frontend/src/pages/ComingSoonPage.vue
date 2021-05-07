<template>
  <main>
    <div class="wrapper">
      <div>
        <img  class="img-responsive" src="@/assets/LogoBG.png"  :alt="$t('comingsoon.dentistry')"/>
        <h1 class="h2 my-5">{{ $t('comingsoon.wwwhere') }}<br/>{{ $t('comingsoon.salon') }}<br/>
          &ldquo;<span class="mgold">{{ $t('comingsoon.dentistry') }}</span>&rdquo;</h1>
        <h2 class="h3 my-5">{{ $t('comingsoon.opens') }} <br/> {{ $t('comingsoon.dateopen') }}</h2>
      </div>
      <a href="https://www.facebook.com/ToHwdDent" class="share fa fa-facebook facebook"
         target="_blank" rel="noreferrer"></a>
      <a href="https://www.instagram.com/tohwddent/" class="share fa fa-instagram instagram"
         target="_blank" rel="noreferrer"></a>
      <a href="https://www.youtube.com/channel/UCeyxKBqdLFA79kCTH29RDsQ" class="share fa fa-youtube youtube"
         target="_blank" rel="noreferrer"></a>
    </div>
  </main>
</template>

<script>
export default {

};
</script>

<style scoped lang="sass">
@import "@/styles/_variables.sass"

@font-face
  font-family: "VDS"
  src: local("VDS"),
  url("../fonts/VDS/6f15514498b89a9ba710dc3eb4f96be0.eot")
  src: url("../fonts/VDS/6f15514498b89a9ba710dc3eb4f96be0iefix.eot") format("embedded-opentype"),
  url("../fonts/VDS/6f15514498b89a9ba710dc3eb4f96be0.woff2") format("woff2"),
  url("../fonts/VDS/6f15514498b89a9ba710dc3eb4f96be0.woff") format("woff"),
  url("../fonts/VDS/6f15514498b89a9ba710dc3eb4f96be0.ttf") format("truetype"),
  url("../fonts/VDS/6f15514498b89a9ba710dc3eb4f96be0.svg") format("svg")

h1, h2, h3, h4, h5, h6
  text-align: center

main
  font-family: VDS, Verdana, Arial, serif
  margin: auto
  align-items: center
  display: flex
  justify-content: center
  width: 100%
  height: 100%
  > .wrapper
    border-radius: 1rem
    background: rgba(254, 253, 251, 0.64)
    backdrop-filter: blur(16px)
    width: 100%
    display: flex
    flex-wrap: wrap
    align-items: center
    justify-content: center
    padding: 1rem
    img
      width: 100%
      height: auto
      &.img-responsive
        display: inline-block
        margin-top: 3em
    .mgold
      border-bottom: 2px solid #eed199
  a
    &.fa
      padding: 20px
      font-size: 30px
      width: 70px
      text-align: center
      text-decoration: none
      border-radius: 50%
    &.share
      width: 5rem
      height: 5rem
      float: left
      margin: .5rem .5rem .5rem .5rem
      color: #353c4a
      border: .125rem solid #f3f3f3
      box-shadow: 0 0 8px 0 rgba(50, 50, 50, 0.15)
      border-radius: 50%
      transition: 250ms
      &:hover
       text-decoration: none
    &.vk
      &:hover, &:focus
        color: #00ACED
        box-shadow: 0 0 24px 0 #00ACED
    &.instagram
      &:hover, &:focus
        color: #4183c4
        box-shadow: 0 0 24px 0 #4183c4
    &.pinterest
      &:hover, &:focus
        color: #bd081c
        box-shadow: 0 0 24px 0 #bd081c
    &.youtube
      &:hover, &:focus
        color: #cd201f
        box-shadow: 0 0 24px 0 #cd201f
    &.facebook
      &:hover, &:focus
        color: #3b5998
        box-shadow: 0 0 24px 0 #3b5998
    &.linkedin
      &:hover, &:focus
        color: #dd4b39
        box-shadow: 0 0 24px 0 #dd4b39

@media screen and (min-width: 576px)
  main
    max-width: 540px
@media screen and (min-width: 768px)
  main
    max-width: 720px
@media screen and (min-width: 992px)
  main
    max-width: 960px
@media screen and (min-width: 1200px)
  main
    max-width: 1140px

</style>
