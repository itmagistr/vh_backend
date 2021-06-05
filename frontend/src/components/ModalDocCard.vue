<template>
    <div class="modal fade" id="mdl-doc-card" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog modal-ctm modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="card_name">{{$t('doctorpage.titledoccard')}}<hr></h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
            <div class="modalTop">
              <div class="image">
                <img :src="data.img">
              </div>
              <div class="info">
                <div class="top">
                  <div class="icon"><img :src="data.special_img"></div>
                  <div class="bk1">
                    <div class="tittle">{{ data.special }}</div>
                    <div class="education">{{ data.degree }}</div>
                  </div>
                  <div class="name">{{ data.firstName }} {{ data.lastName }} {{ data.midName }}</div>
                </div>
                <div class="bottom">
                  <div class="card_footer">
                    <StarRating class="card_rating" :rating="parseFloat(data.rating)" :read-only="true" :increment="0.1"
                                      active-color="#DFB971" inactive-color="#F1EEE6"
                                      :show-rating="false" :star-size="22"/>
                    <div class="card_review">{{ data.reviewCount }} {{$t('doctorpage.review')}}</div>
                    <div class="d-flex">
                        <div class="d-flex card_social">
                          <i class="fab fa-instagram" aria-hidden="true"></i>
                          <i class="fab fa-youtube" aria-hidden="true"></i>
                        </div>
                        <div class="d-flex ml-auto card_icons">
                          <i class="fas fa-phone" style="transform: scaleX(-1)"/>
                          <img src="/img/chat.svg"/>
                          <i class="fas fa-heart"/>
                        </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-body">
            <div class="clip-accordion" @click="show('proc')" :class="[states.proc ? 'active' : '']">
              {{ $t('modaldoccard.procedure') }} <i class="fas fa-caret-down"></i>
            </div>
            <div class="clip-accordion" @click="show('photo')" :class="[states.photo ? 'active' : '']">
              {{ $t('modaldoccard.photo') }} <i class="fas fa-caret-down"></i>
            </div>
            <div class="clip-accordion" @click="show('youtube')" :class="[states.youtube ? 'active' : '']">
              Youtube <i class="fas fa-caret-down"></i>
            </div>
            <div class="clip-accordion" @click="show('cert')" :class="[states.cert ? 'active' : '']">
              {{ $t('modaldoccard.certificate') }} <i class="fas fa-caret-down"></i>
            </div>
            <div class="clip-accordion" @click="show('edu')" :class="[states.edu ? 'active' : '']">
              {{ $t('modaldoccard.education') }} <i class="fas fa-caret-down"></i>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-ok" @click="send()">{{ $t('modaldoccard.signup') }}</button>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import StarRating from "vue-star-rating";

export default {
  props: ['selfInfo'],
  data(){
    return {
      data: {
        degree: "...",
        experience: 3,
        firstName: "",
        img: "",
        special_img: "",
        lastName: "",
        level: "",
        midName: "",
        rating: "",
        reviewCount: 0,
        special: "",
        uid: "",
      },
      states: {
        proc: false,
        photo: false,
        youtube: false,
        cert: false,
        edu: false
      },
    }
  },
  methods: {
    show(pos){
      this.states[pos] = !this.states[pos];
    },
    getInfo() {
      //http://localhost:8000/ru/vhapi/doctor/bf0f0856-f57d-48c6-b99c-b3c8a2e3ea82/workres/
      fetch(`http://localhost:8000/${this.$i18n.locale}/vhapi/doctor/${this.selfInfo}`).then(response => response.json()).then(data => {
        this.data = data;
        console.log(data);
      }).catch((error) => {
        console.log(error);
        //this.results = null;
      }).finally(() => {
        this.states = { proc: false, photo: false, youtube: false, cert: false, edu: false };
        //this.loading = false;
      });
    },
    send(){
      this.$store.commit("updDoc", this.data.uid);
    }
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
  components: {
    StarRating,
  },
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

#mdl-doc-card
  > .modal-ctm
    max-width: 688px
    > .modal-content
      background: #FEFDFB
      border: none
      border-radius: 0.5rem
  .modal-header, .modal-footer
    border: none
  .modal-header
    padding: 1.5rem 1.5rem 1rem
    display: initial
    > h5.card_name
      display: none
      font-family: Montserrat
      font-style: normal
      font-weight: normal
      font-size: 19px
      line-height: 24px
      > hr
        border-top: 1px solid $button-color
        margin-bottom: 2rem
    > .close
      position: absolute
      right: 16px
      top: 16px
      color: #DFB971
      > span
        font-size: 2rem
      &:hover
        color: #9CC6BE
    > .modalTop
      display: flex
      > div.image
        display: flex
        justify-content: center
        width: 240px
        height: 180px
        border-radius: .5rem
        background-color: $backgroundImage
        > img
          height: 180px
      > .info
        padding: .5rem 1rem
        display: inline-block
        vertical-align: top
        width: calc(100% - 256px)
        > .top
          > .icon
            background-color: $active-link-line
            width: 40px
            height: 40px
            margin-right: 8px
            border-radius: 4px
            padding: 8px
            text-align: center
            vertical-align: middle
            display: inline-block
            > img
              width: 24px
              height: 24px
          > .bk1
            display: inline-block
            vertical-align: middle
            > .tittle
              font-family: FuturaBookC
              font-size: 16px
              line-height: 21px
              color: $button-color
              padding-bottom: 4px
            > .education
              font-family: Montserrat
              font-size: 14px
              line-height: 16px
          > .name
            margin: 1rem auto
            font-family: Montserrat
            font-weight: 500
            font-size: 21px
            line-height: 26px
        > .bottom
          > .card_footer
            vertical-align: middle
            > .card_rating
              display: inline-block
              font-size: 22px
              line-height: 22px
              display: inline-flex
              > div
                > span
                  margin-right: 4px!important
            > .card_review
              display: inline-flex
              vertical-align: bottom
              font-family: FuturaBookC
              font-size: 16px
              line-height: 21px
              color: $blue_three
            > div:last-child
              margin: 16px auto 0
              > .card_social
                font-size: 22px
                line-height: 22px
                color: $blue_three
                > i
                  width: 22px
                  margin-left: 16px
                  &:first-child
                    margin-left: 0px
                  &:hover
                    color: $none
              > .card_icons
                font-size: 22px
                line-height: 22px
                color: $blue_three
                > i, img
                  vertical-align: text-bottom
                  width: 22px
                  margin-left: 16px
  .modal-body
    padding: inherit
    > .clip-accordion
      font-family: FuturaBookC
      font-size: 16px
      letter-spacing: 0.08em
      text-transform: uppercase
      color: #071013
      height: 1.5rem
      margin-bottom: 1rem
      padding: 0px 1.5rem
      &:hover, &.active
        color: $white
        background-color: $active-link-line
        > i
          transform: scaleY(-1)
          color: $white
      > i
        margin-left: 8px
        color: $blue_three

  .modal-footer
    padding: 0px
    > .btn-ok
      position: absolute
      bottom: -25px
      left: 35%
      width: 240px
      height: 48px
      border-radius: 0.5rem
      background: #42E1C5
      color: white
      font-family: FuturaBookC
      font-size: 1rem
      line-height: 1.25rem
      letter-spacing: 0.08em
      text-transform: uppercase
      color: #FEFDFB
.modal-backdrop
  background: #cef2e9
  backdrop-filter: blur(16px)

@media (max-width: 1399px)
  #mdl-doc-card
    > .modal-ctm
      display: block
      height: 100%
      width: 100%
      max-width: initial
      margin: initial
      > .modal-content
        border-radius: 0px
        height: 100%
        > .modal-header
          padding: 1.25rem 1rem 1rem
          > h5.card_name
            display: initial
          > img
            margin-left: 1rem
          > .close
            padding: 1.25rem 1rem
        > .modal-footer
          > .btn
            position: static
            margin: 32px auto 58px
            left: auto
            bottom: auto
@media (max-width: 450px)
  #mdl-doc-card
    > .modal-ctm
      > .modal-content
        height: initial
        > .modal-header
          > img
            width: 100%
            margin-left: initial
          > .info
            width: 100%
            padding: 1rem 0 0
        > .modal-footer
          padding-top: 32px
          padding-bottom: 70px
          > .btn
            margin: auto
            position: initial
</style>
