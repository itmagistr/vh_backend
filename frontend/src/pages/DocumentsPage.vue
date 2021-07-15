<template>
  <div class="wrapper">
    <div class="proto2">
      <div v-for="slide in slides" :key="slide.src">
        <img :src="slide.src"  @click="imgShow(slide.src)" data-toggle="modal" data-target="#mdl-image">
      </div>
    </div>
    <!--<splide :options="options" has-slider-wrapper>
      <splide-slide v-for="slide in slides" :key="slide.src">
        <img :src="slide.src">
      </splide-slide>
    </splide>-->
  </div>
</template>

<script>
export default {
  props: ['resize'],
  data() {
    return {
      options: {
        type: 'loop',
        rewind: true,
        autoHeight: true,
        autoWidth : true,
        gap: '2rem',
        focus: 'center',
      },
      slides: [
        {src: `${this.$store.state.apihostImg}/media/uploads/documents/doc1.png`},
        {src: `${this.$store.state.apihostImg}/media/uploads/documents/doc2.png`},
        {src: `${this.$store.state.apihostImg}/media/uploads/documents/doc3.png`}
      ],
    }
  },
  methods: {
    imgShow(val){
      this.$root.$emit("imgShowGL", val);
    },
  }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

body.documGal
  background: #F6F3ED
  > header
    background: #F6F3ED
  > main
    padding: 27px 0 2rem
  .wrapper
    width: calc(100% - 300px)
    .proto2
      height: 320px
      width: 100%
      overflow: auto
      background: #F3E9D4
      border-radius: 1rem
      margin: 27px 0
      display: flex
      > div
        margin: 0 .5rem
        &:first-child
          margin-left: 0
        &:last-child
          margin-right: 0
        > img
          height: 100%
    .splide
      padding: 0 0 3rem
@media (max-width: 1399px)
  body.documGal
    background: #F6F3ED
    > header
      background: #F6F3ED
    > main
      padding: 0
    .wrapper
      margin: auto
      width: calc(100% - 2rem)
</style>
