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
        autoWidth : true,
        autoheight: true,
        gap: '2rem',
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
.wrapper
  width: calc(100% - 300px)
@media (max-width: 1399px)
  .wrapper
    width: 100%
</style>
