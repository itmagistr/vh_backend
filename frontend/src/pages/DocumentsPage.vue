<template>
  <div class="wrapper">
    <splide :options="options" has-slider-wrapper>
      <splide-slide v-for="slide in slides" :key="slide.src">
        <img :src="slide.src">
      </splide-slide>
    </splide>
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
        {src: "http://localhost:8000/media/uploads/documents/doc1.png"},
        {src: "http://localhost:8000/media/uploads/documents/doc2.png"},
        {src: "http://localhost:8000/media/uploads/documents/doc3.png"}
      ],
    }
  },
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"
body.documGal
  background: #F6F3ED
  > header
    background: #F6F3ED
  > main
    padding-bottom: 2rem
    > div.container
      padding: 0
  .wrapper
    width: calc(100% - 300px)
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
