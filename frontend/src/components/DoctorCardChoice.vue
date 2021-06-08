<template>
  <div class="doctor-clip"  @click="selected(data.uid)">
        <div class="d-flex clip-header">
            <div class="d-flex">
                <div class="clip-photo">
                  <img :src="'http://localhost:8000' + data.img" height="64px"/>
                </div>
                <div class="clip-bk1">
                    <div class="clip-tittle">{{ data.special }}</div>
                    <div class="clip-name">{{ data.firstName }} {{ data.lastName }} <br> {{ data.midName }}</div>
                </div>
            </div>
            <div class="d-flex flex-column clip-info">
                <div>{{ data.experience }}</div>
                <div>{{ data.level }}</div>
                <div>{{ data.degree }}</div>
            </div>
        </div>
        <div class="clip-body">
            <div class="clip-accordion" @click="show('proc')" :class="[states.proc ? 'active' : '']">
              {{ $t('modaldoccard.procedure') }} <i class="fas fa-caret-down"></i>
            </div>
            <div class="clip-accordion" @click="show('photo')" :class="[states.photo ? 'active' : '']">
              {{ $t('modaldoccard.photo') }} <i class="fas fa-caret-down"></i>
            </div>
            <Carousel v-show="states.photo" :self-info="data.uid"/>
            <div class="clip-accordion" @click="show('social')" :class="[states.social ? 'active' : '']">
              Соцсети <i class="fas fa-caret-down"></i>
            </div>
            <div class="soc-btn-card" v-show="states.social">
              <a href="https://www.instagram.com/tohwddent" target="_blank"><button class="social-btn"><i class="fab fa-instagram"></i></button></a>
              <a href="https://www.youtube.com/channel/UCeyxKBqdLFA79kCTH29RDsQ" target="_blank"><button class="social-btn"><i class="fab fa-youtube"></i></button></a>
              <a href="https://www.facebook.com/ToHwdDent" target="_blank"><button class="social-btn"><i class="fab fa-facebook-f"></i></button></a>
              <a href="https://vk.com/tohwddent" target="_blank"><button class="social-btn"><i class="fab fa-vk"></i></button></a>
            </div>
            <div class="clip-accordion" @click="show('cert')" :class="[states.cert ? 'active' : '']">
              {{ $t('modaldoccard.certificate') }} <i class="fas fa-caret-down"></i>
            </div>
            <div class="clip-accordion" @click="show('edu')" :class="[states.edu ? 'active' : '']">
              {{ $t('modaldoccard.education') }} <i class="fas fa-caret-down"></i>
            </div>
        </div>
        <div class="d-flex clip-footer">
            <div>
                <StarRating class="clip-rating" :rating="parseFloat(data.rating)" :read-only="true" :increment="0.1"
                        active-color="#DFB971" inactive-color="#F1EEE6"
                        :show-rating="false" :star-size="22"/>
                <div class="d-flex clip-review">{{ data.reviewCount }} {{ $t('doctorchoice.review') }}</div>
            </div>
                <div class="d-flex clip-icons">
                    <i class="fas fa-phone" style="transform: scaleX(-1)"/>
                    <img src="/img/chat.svg"/>
                    <i class="fas fa-heart"/>
                </div>
        </div>
  </div>
</template>

<script>
import StarRating from "vue-star-rating";
import Carousel from "@/components/DoctorWorkresCarousel"
import currencyFormat from "@/helpers/currencyFormat";
import timeFormat from "@/helpers/timeFormat";

export default {
    props: ['data'],
    data() {
        return {
            // select: this.$store.state.Booking.Doctor || 'cc3c3aa6-590a-49c2-b9d1-faf4cf3505a0',
            loading: true,
            errored: false,
            results: null,
            states: {
              proc: false,
              photo: false,
              social: false,
              cert: false,
              edu: false
            },
        }
    },
    watch:{
      select: {
        handler(newValue, oldValue) {
          if (newValue === oldValue)
            return;
          console.log(newValue);
        },
      },
    },
    components: {
      StarRating, Carousel,
    },
    filters: {
      currencyFormat, timeFormat
    },
    methods: {
        show(pos){
            this.states[pos] = !this.states[pos];
        },
        selected(val) {
            this.$emit('select', val);
            this.select = val;
        },
    }
}

</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.doctor-clip
  display: flex
  flex-direction: column
  border: 1px solid rgba(238, 209, 153, 0.32)
  border-radius: 8px
  width: 624px
  margin-bottom: 16px
  padding: 0
  &:hover, &.active
      border: 2px solid #42E1C5
  > .clip-header
    margin: 1.625rem 1.5rem 1rem 1.5rem
    justify-content: space-between
    .clip-photo
      display: flex
      justify-content: center
      width: 64px
      height: 64px
      background: #e9ecef
      border-radius: 4px
      margin-right: 12px
    .clip-bk1
      vertical-align: top
      .clip-tittle
        font-family: FuturaBookC
        font-size: 14px
        line-height: 16px
        color: #B8882F
        padding-top: 4px
        padding-bottom: 4px
      .clip-name
        font-family: Montserrat
        font-size: 19px
        line-height: 19px
        color: #071013
    .clip-info
      text-align: right
      font-family: FuturaBookC
      font-size: 16px
      line-height: 21px
      color: #071013
  > .clip-body
    display: flex
    flex-direction: column
    margin-bottom: .25rem
    > .clip-accordion
      font-family: FuturaBookC
      font-size: 16px
      line-height: 21px
      letter-spacing: 0.08em
      text-transform: uppercase
      color: #071013
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
    > .soc-btn-card
      display: flex
      margin: 0 1.5rem 1rem
      > a
        margin: 0 .5rem
        > button
          border: 1px solid #B8882F
          border-radius: 4px
          margin: 0
  > .clip-footer
    justify-content: space-between
    vertical-align: middle
    margin: 0 1.5rem 1.5rem
    > div
      display: flex
      >.clip-rating
        font-size: 22px
        line-height: 22px
        margin-right: .5rem
        > div
          > span
            margin-right: 4px!important
    .clip-review, .clip-icons
      font-family: FuturaBookC
      font-size: 16px
      line-height: 21px
      color: $blue_three
    .clip-icons
      font-size: 22px
      line-height: 22px
      color: $blue_three
      > i, img
        margin-left: 16px
</style>














