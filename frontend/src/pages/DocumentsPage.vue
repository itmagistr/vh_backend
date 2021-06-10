<template>
  <div class="slideshow-container">
    <div v-for="(data, index) in photo" class="mySlides" :key="index">
      <img :src="data.img" v-if="index === slideIndex">
    </div>
    <a class="prev" @click="plusSlides(-1)">&#10094;</a>
    <a class="next" @click="plusSlides(1)">&#10095;</a>
  </div>
</template>

<script>
export default {
  props: ['resize'],
  data() {
    return {
      slideIndex: 0,
      timer: null,
      photo: [
        {img: "http://localhost:8000/media/uploads/documents/doc1.png"},
        {img: "http://localhost:8000/media/uploads/documents/doc2.png"},
        {img: "http://localhost:8000/media/uploads/documents/doc3.png"}
      ],
    }
  },
  mounted() {
    this.timer = setInterval(() => {
      this.plusSlides(1);
    }, 5000)
  },
  methods: {
    plusSlides(n) {
      this.slideIndex += n;
      if(this.slideIndex < 0)
        this.slideIndex = this.photo.length;
      else if(this.slideIndex >= this.photo.length)
        this.slideIndex = 0;
    },
  },
  beforeDestroy() {
    clearInterval(this.timer)
  }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.fade-enter-active, .fade-leave-active
  transition: opacity .5s

.fade-enter, .fade-leave-to
  opacity: 0

.slideshow-container
  max-width: 1000px
  position: relative
  margin: auto

.prev, .next
  cursor: pointer
  position: absolute
  top: 50%
  width: auto
  margin-top: -22px
  padding: 16px
  color: white
  font-weight: bold
  font-size: 18px
  transition: 0.6s ease
  border-radius: 0 3px 3px 0
  user-select: none

.next
  right: 0
  border-radius: 3px 0 0 3px

.prev:hover, .next:hover
  background-color: rgba(0,0,0,0.8)
</style>
