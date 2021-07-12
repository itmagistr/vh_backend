<template>
  <div class="modal fade" id="mdl-image" tabindex="-1" role="dialog" aria-hidden="true">
    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
      <span aria-hidden="true">&times;</span>
     </button>
    <div class="modal-dialog modal-ctm modal-dialog-centered" role="document">
      <img class="modal-content" data-dismiss="modal" :src="img">
    </div>
  </div>
</template>

<script>
export default {
  data() {
      return {
        img: null,
      }
  },
  mounted() {
    this.$root.$on("imgShowGL", (val) => {
      this.img = val;
    });
  },
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

#mdl-image
  z-index: 1051
  > button.close
    position: absolute
    top: 1rem
    right: 1rem
    font-size: 3rem
  > .modal-dialog
    > .modal-content
      width: -webkit-fill-available
      border-radius: 1rem
@media (max-width: 450px)
  #mdl-image
    > .modal-dialog
      margin: 0
      max-width: 100%
</style>