<template>
  <div class="col">
    <div class="doctor">
      <div id="icon-doctor">
        <img :src="results.img">
      </div>
      <div id="name-doctor">
        <div>{{ results.special}}</div>
        <div>{{ results.lastName }} {{ results.firstName }}</div>
      </div>
      <StarRating class="star-doctor" :rating="parseFloat(results.rating)" :read-only="true" :increment="0.1"
                                    active-color="#DFB971" inactive-color="#F1EEE6"
                                    :show-rating="false" :star-size="16"/>
      <button class="btn" id="btn-doctor" @click="doctors"><i class="fas fa-caret-right"></i></button>
    </div>
  </div>
</template>

<script>
import StarRating from "vue-star-rating";

export default {
  model: {
    prop: 'phase',
    event: 'goToDoctor'
  },
  props: ['phase'],
  data() {
      return {
          uid: null,
          title: null,
          fName: null,
          lName: null,
          loading: true,
          errored: false,
          results: [],
      };
  },
  components: {
    StarRating,
  },
  async created() {
    if (this.$store.state.Booking.Doctor !== null)
      await this.docUID(this.$store.state.Booking.Doctor);
    else
      await this.docUID('');
  },
  // определяйте методы в объекте `methods`
  methods: {
    docUID(uid){
      fetch(`http://localhost:8000/${this.$i18n.locale}/vhapi/doctor/${uid}`)
      .then(stream => stream.json())
      .then(response => {
        this.results = response;
        console.log(response);
      })
      .catch(error => {
        console.error(error);
        this.errored = true;
        this.results = null;
      })
      .finally(() => {
        if(this.results.img === null)
          this.results.img = 'http://localhost:8000/media/uploads/human/defaultAvatar.png';
        this.loading = false;
      });
    },
     doctors() {
        this.$store.commit("updPhase", 4);
        this.$emit('goToDoctor', 4);
    }
  },
  watch: {
    "$i18n.locale": {
      handler(newLocale, oldLocale) {
        if (newLocale === oldLocale)
          return;
        if (this.$store.state.Booking.Doctor !== null)
          this.docUID(this.$store.state.Booking.Doctor);
        else
          this.docUID('');
      },
      immediate: true,
    },
  },
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.doctor
  height: 72px
  position: relative

.doctor > div, .doctor > button
  display: inline-block

#icon-doctor
  display: flex
  justify-content: center
  position: absolute
  top: 8px
  left: 8px
  width: 56px
  height: 56px
  background: $backgroundImage
  border-radius: 4px
  > img
    height: 100%

#name-doctor
  font-family: FuturaBookC
  position: absolute
  top: 18px
  left: 80px
  width: 177px
  line-height: 1

#name-doctor > div:first-child
  color: $button-color
  font-size: 14px

#name-doctor > div:last-child
  font-size: 21px

.star-doctor
  position: absolute
  top: 15px
  right: 34px
  > div
    > span
      margin: 0 4px
      width: 16px
      height: 16px
      &:first-child
        margin-left: 0
      &:last-child
        margin-right: 0

.star-none
  color: #f1eee6

.star-half
  background: linear-gradient(90deg, $button-color 55%, #f1eee6 55%)
  -webkit-background-clip: text
  -webkit-text-fill-color: transparent

.star-full
  color: $button-color

#btn-doctor
  position: absolute
  right: 0px
  width: 26px
  height: 72px
  border: none
  border-radius: 0px 8px 8px 0px
  background: $none
  color: $white
</style>
