<template>
  <div class="gCarousel">
    <button class="btn leftBtn" @click="chgPos(-1)">
      <i class="fas fa-caret-left" aria-hidden="true"></i>
    </button>
    <div class="imgField">
      <div v-for="(c, index) in data" :key="index" class="imgCarousel">
        <img :src="c.img"
             :alt="c.title"
             @click="imgShow(c.img)"
             data-toggle="modal"
             data-target="#mdl-image">
      </div>
    </div>
    <button class="btn rightBtn" @click="chgPos(1)">
      <i class="fas fa-caret-right" aria-hidden="true"></i>
    </button>
  </div>
</template>

<script>
export default {
  props: ['selfInfo'],
  data(){
    return {
      data: [],
    }
  },
  created() {
    if(this.selfInfo !== undefined)
      this.getInfo();
  },
  watch: {
    selfInfo: {
      handler(newValue, oldValue) {
        if (newValue === oldValue)
          return;
        this.getInfo();
      },
    },
  },
  methods: {
    imgShow(val){
      this.$root.$emit("imgShowGL", val);
    },
    chgPos(val){
      console.log(val);
    },
    show(pos){
      this.states[pos] = !this.states[pos];
    },
    getInfo() {
      fetch(`${this.$store.state.apihost}${this.$i18n.locale}/vhapi/doctor/${this.selfInfo}/workres/`)
      .then(response => response.json())
      .then(data => {
        this.data = data.results;
      }).catch((error) => {
        console.log(error);
        this.data = null;
      }).finally(() => {
        this.states = { proc: false, photo: false, youtube: false, cert: false, edu: false };
        // this.loading = false;
      });
    },
  },
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.gCarousel
  background: #F3E9D4
  display: flex
  margin: 0 1.5rem 1rem
  height: 80px
  border-radius: .25rem
  color: $white
  > .leftBtn, .rightBtn
    height: 100%
    width: 1rem
    background-color: $active-link-line
    border: none
    border-radius: .25rem
    &.btn
      padding: 0
    > i
      right: 1px
      position: relative
      color: $white
  > .imgField
    overflow: auto
    display: flex
    width: 100%
    > .imgCarousel
      border-radius: .25rem
      background: $backgroundImage
      width: 88px
      height: 64px
      margin: .5rem .25rem
      &:first-child
          margin-left: .5rem
      &:last-child
          margin-right: .5rem
      > img
        border-radius: .25rem
        display: flex
        width: 88px
        height: 64px
        justify-content: center
        align-items: center
</style>