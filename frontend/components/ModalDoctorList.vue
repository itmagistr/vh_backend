<template>
  <div class="modal fade" id="mdl-doc-list" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog modal-ctm modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="card_name">Врачи<hr></h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <DoctorCardChoice v-for="c in data" :key="c.uid" :data="c"/>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-ok" @click="send" data-dismiss="modal" >{{$t('doctorpage.close')}}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import DoctorCardChoice from "@/components/DoctorCardChoice";

export default {
  props: {
    data: Array,
  },
  data() {
    return {
    }
  },
  watch: {
    data: {
      handler(newValue, oldValue) {
        if (newValue === oldValue)
          return;
        console.log(newValue);
      },
    },
  },
  components: { DoctorCardChoice, },
  methods:{
    send() { console.log(this.data); },
  }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

#mdl-doc-list
  .modal-ctm
    max-width: 658px
    .modal-header, .modal-footer
      border: none
    .modal-header
      padding: 1.5rem 1.5rem 1rem
      display: initial
      > h5.card_name
        font-family: Montserrat
        font-style: normal
        font-weight: normal
        font-size: 19px
        line-height: 24px
        > hr
          border-top: 1px solid $button-color
          margin-bottom: 0
      > .close
        position: absolute
        right: 16px
        top: 16px
        color: $button-color
        > span
          font-size: 2rem
        &:hover
          color: #9CC6BE
    .modal-footer
      padding: 0
      display: flex
      justify-content: center
      > .btn-ok
        position: absolute
        width: 240px
        height: 48px
        border-radius: 0.5rem
        background: $active-link-line
        color: white
        font-family: FuturaBookC
        font-size: 1rem
        line-height: 1.25rem
        letter-spacing: 0.08em
        text-transform: uppercase
        color: $white
@media (max-width: 1399px)
  #mdl-doc-list
    > .modal-ctm
      display: block
      height: 100%
      width: 100%
      max-width: initial
      margin: 0
      > .modal-content
        border-radius: 0
        > .modal-header
          padding: 1.25rem 1rem 1rem
          > h5.card_name
            display: initial
          > img
            margin-left: 1rem
          > .close
            padding: 1.25rem 1rem
        > .modal-body
          padding: 0
        > .modal-footer
          > .btn
            position: static
            margin: 32px auto 58px
            left: auto
            bottom: auto
@media (max-width: 450px)
  #mdl-doc-list
    > .modal-ctm
      > .modal-content
        > .modal-footer
          margin: 2rem 0
          > .btn
            margin: auto
            position: initial
</style>