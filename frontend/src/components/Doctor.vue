<template>
  <div class="col doctor">
    <div id="icon-doctor"> </div>
    <div id="name-doctor">
      <div>{{ results[0].human.title }}</div>
      <div>{{ results[0].human.lastName }} {{ results[0].human.firstName }}</div>
    </div>
    <div id="star-doctor">
      <i class="fas fa-star star-full"></i>
      <i class="fas fa-star star-full"></i>
      <i class="fas fa-star star-full"></i>
      <i class="fas fa-star star-half"></i>
      <i class="fas fa-star star-none"></i>
    </div>
    <button class="btn" id="btn-doctor" @click="doctors"><i class="fas fa-caret-right"></i></button>
  </div>
</template>

<script>
export default {
  data() {
      return {
          loading: true,
          errored: false,
          results: null
      };
  },
  async created() {
    await fetch('http://localhost:8000/ru/vhapi/doctor/')
    .then(stream => stream.json())
    .then(response => {
      this.results = response.results;
      console.log(response.results);
    })
    .catch(error => {
      console.error(error);
      this.errored = true;
      this.results = null;
    })
    .finally(() => {
      this.loading = false;
    });
  },
  // определяйте методы в объекте `methods`
  methods: {
     doctors: function () {
      fetch('http://localhost:8000/ru/vhapi/doctor/').
      then(stream => stream.json()).
      then(response => {
        this.results = response.results;
        console.log(response.results);
      }).
      catch((error) => { console.log(error); }).
      finally(() => {
        this.loading = false;
      });
    }
  }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.doctor
  height: 72px

.doctor > div, .doctor > button
  display: inline-block

#icon-doctor
  position: absolute
  top: 8px
  left: 8px
  width: 56px
  height: 56px
  background: $active-link-line
  border-radius: 4px

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

#star-doctor
  position: absolute
  top: 15px
  right: 34px
  width: 96px
  height: 16px

#star-doctor > i
  margin: 0px 2px
  width: 16px
  height: 16px

#star-doctor > i:first-child
  margin-left: 0px

#star-doctor > i:last-child
  margin-right: 0px

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