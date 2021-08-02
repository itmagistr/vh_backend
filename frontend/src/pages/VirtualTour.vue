<template>
  <div class="wrapper">
    <div class="proto2">
      <div v-for="image in images" :key="image.src">
        <img :src="image.src" @click="imgShow(image.src)" data-toggle="modal" data-target="#mdl-image">
      </div>
    </div>
     <div class="proto2">
      <div v-for="video in videos" :key="video.src">
        <video @click="videoShow(video.src)" data-toggle="modal" data-target="#mdl-image">
          <source :src="video.src" type="video/mp4"/>
        </video>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['resize'],
  data() {
    return {
      images: [
        {src: `${this.$store.state.apihostImg}/media/virttur/hollywood_dentistry_gal2.jpg`},
        {src: `${this.$store.state.apihostImg}/media/virttur/hollywood_dentistry_gal4.jpg`},
        {src: `${this.$store.state.apihostImg}/media/virttur/image1.jpeg`},
        {src: `${this.$store.state.apihostImg}/media/virttur/image0.jpeg`},
        {src: `${this.$store.state.apihostImg}/media/virttur/image2.jpeg`}],
      videos: [
        {src: `${this.$store.state.apihostImg}/media/virttur/181336916.mp4`},
        {src: `${this.$store.state.apihostImg}/media/virttur/93671.mp4`},
        {src: `${this.$store.state.apihostImg}/media/virttur/93672.mp4`}
      ],
    }
  },
  methods: {
    imgShow(val){
      this.$root.$emit("imgShowGL", val, false);
    },
    videoShow(val){
      this.$root.$emit("imgShowGL", val, true);
    }
  }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

body.tour
  background: #F6F3ED
  > header
    background: #F6F3ED
  > main
    padding: 27px 0 2rem
  .wrapper
    width: calc(100% - 300px)
    .proto2
      padding: 1rem
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
        > img, video
          height: 100%
          width: auto
          border-radius: .5rem
    .splide
      padding: 0 0 3rem
@media (max-width: 1399px)
  body.tour
    background: #F6F3ED
    > header
      background: #F6F3ED
    > main
      padding: 0
    .wrapper
      margin: auto
      width: calc(100% - 2rem)
</style>
