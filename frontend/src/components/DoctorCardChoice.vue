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
        <docAccordionMenu class="clip-body" :selfInfo="data"/>
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
import currencyFormat from "@/helpers/currencyFormat";
import timeFormat from "@/helpers/timeFormat";
import docAccordionMenu from "@/components/DocAccordionMenu";

export default {
    props: ['data'],
    data() {
        return {
            // select: this.$store.state.Booking.Doctor || 'cc3c3aa6-590a-49c2-b9d1-faf4cf3505a0',
            loading: true,
            errored: false,
            results: null,
            medprocs: [],
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
      StarRating, docAccordionMenu
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
        getProcDoc() {
          fetch(`${this.$store.state.apihost}${this.$i18n.locale}/vhapi/doctor/${this.data.uid}/medprocs/`)
          .then(response => response.json()).then(data => {
            this.medprocs = data;
            console.log(data);
          }).catch((error) => {
            console.log(error);
            //this.results = null;
          }).finally(() => {
            //this.loading = false;
          });
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
      border: 2px solid $profi-main
  > .clip-header
    margin: 1.625rem 1.5rem 1rem 1.5rem
    justify-content: space-between
    .clip-photo
      display: flex
      justify-content: center
      width: 64px
      height: 64px
      background: $backgroundImage
      border-radius: 4px
      margin-right: 12px
    .clip-bk1
      vertical-align: top
      .clip-tittle
        font-family: FuturaBookC
        font-size: 14px
        line-height: 16px
        color: $header_text
        padding-top: 4px
        padding-bottom: 4px
      .clip-name
        font-family: Montserrat
        font-size: 19px
        line-height: 19px
        color: $black
    .clip-info
      text-align: right
      font-family: FuturaBookC
      font-size: 16px
      line-height: 21px
      color: $black
  > .clip-body
    display: flex
    flex-direction: column
    margin-bottom: .25rem
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














