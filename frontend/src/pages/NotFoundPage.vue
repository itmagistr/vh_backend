<template>
  <div class="ctm-notfound">
    <div>
      <img  class="img-responsive" src="@/assets/LogoBG.png"  :alt="$t('comingsoon.dentistry')"/>
      <h1>{{ $t('notfoundpage.header') }}</h1>
    </div>
  </div>
</template>

<script>
export default {

};
</script>

<style lang="sass">
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

div.ctm-notfound
  h1, h2, h3, h4, h5, h6
    text-align: center
  display: flex
  justify-content: center
  align-items: center
  height: calc(100vh - 136px)
  font-family: VDS, Verdana, Arial, serif
  > div
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

@media (max-width: 1399px)
  .ctm-notfound
    height: calc(100vh - 328px)!important
</style>