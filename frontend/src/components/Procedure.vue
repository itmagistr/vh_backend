<template>
  <div class="col procedure">
    <div id="icon-procedure"> </div>
    <div id="name-procedure">
      <div>Процедура</div>
      <div>{{ title }}</div>
    </div>
    <div id="time-procedure">{{ duration }} мин</div>
    <button class="btn" id="btn-procedure" @click="medproc"><i class="fas fa-caret-right"></i></button>
  </div>
</template>

<script>
export default {
  data() {
      return {
        uuid: null,
        title: null,
        duration: null,
        loading: true,
        errored: false,
        results: null
      };
  },
  async created() {
    await fetch('http://localhost:8000/ru/vhapi/medproc/')
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
      this.duration = this.results[0].duration;
      this.title = this.results[0].title;
    });
  },
  // определяйте методы в объекте `methods`
  methods: {
     medproc: function () {
      fetch('http://localhost:8000/ru/vhapi/medproc/').
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

.procedure
  height: 72px

.procedure > div, .procedure > button
  display: inline-block

#icon-procedure
  position: absolute
  top: 8px
  left: 8px
  width: 56px
  height: 56px
  background: $active-link-line
  border-radius: 4px

#name-procedure
  font-family: FuturaBookC
  position: absolute
  top: 13px
  left: 80px
  width: 177px
  line-height: 1

#name-procedure > div:first-child
  color: $button-color
  font-size: 14px

#name-procedure > div:last-child
  font-size: 16px

#time-procedure
  position: absolute
  top: 16px
  right: 34px
  width: 32px
  height: 40px
  padding: 10px 0px
  background: $blue_three
  color: $white
  border-radius: 4px
  text-align: center
  vertical-align: middle
  font-family: FuturaBookC
  line-height: 12px
  font-size: 14px

#btn-procedure
  position: absolute
  right: 0px
  width: 26px
  height: 72px
  border: none
  border-radius: 0px 8px 8px 0px
  background: $none
  color: $white

</style>