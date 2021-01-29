<template>
  <div class="col">
    <div class="procedure">
      <div id="icon-procedure"> </div>
      <div id="name-procedure">
        <div>Процедура</div>
        <div>{{ title }}</div>
      </div>
      <div id="time-procedure">{{ duration | timeFormat("ru-RU")}}</div>
      <button class="btn" id="btn-procedure" @click="medproc()"><i class="fas fa-caret-right"></i></button>
    </div>
  </div>
</template>

<script>
import timeFormat from "@/helpers/timeFormat";
export default {
  model: {
    prop: 'phase',
    event: 'goToProcedure'
  },
  props: ['phase'],
  data() {
      return {
        uid: null,
        title: null,
        duration: null,
        price: null,
        loading: true,
        errored: false,
        results: null
      };
  },
  filters: {
    timeFormat
  },
  async created() {
    if (this.$store.state.Booking.Procedure !== null)
      await this.medProcUID(this.$store.state.Booking.Procedure);
    else
      await this.medProcUID('');
  },
  methods: {
    medProcUID(uid){
      fetch(`http://localhost:8000/ru/vhapi/medproc/`+uid)
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
        this.loading = false;
        this.duration = this.results.duration;
        this.title = this.results.title_check;
        this.price = this.results.price;
        this.$store.commit("updPrice", this.price);
        this.$emit('modProc', this.price);
      });
    },
     medproc() {
        this.$store.commit("updPhase", 3);
        this.$emit('goToProcedure', 3);
    }
  }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.procedure
  height: 72px
  position: relative

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
  left: 310px
  width: 26px
  height: 72px
  border: none
  border-radius: 0px 8px 8px 0px
  background: $none
  color: $white
</style>
