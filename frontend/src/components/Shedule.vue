<template>
    <div class="col">
        <div class="schedule">
          <div class="month">{{day}} {{months[month]}} {{year}}</div>
          <div id="shedule-time">
            <div v-for="count in results" :class="[count.s === 2 ? 'two' : '',
            count.s === 3 ? 'three' : '']" :key="count.t">
              {{ count.t }}
            </div>
          </div>
          <div class="row place">
            <div class="col-auto"><i class="profi"></i> Выгодно</div>
            <div class="col-auto"><i class="few-places"></i> Мало мест</div>
            <div class="col-auto"><i class="no-places"></i> Нет мест</div>
          </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
      return {
        day: new Date().getDate(),
        month: new Date().getMonth(),
        year: new Date().getFullYear(),
        months: ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря'],
        schedule: ["6:00", "6:30", "7:00", "7:30", "8:00", "8:30", "9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"],
        results: null
      }
  },
  async created() {
      await fetch(`http://localhost:8000/ru/vhapi/timetatus/${new Date().toLocaleString('en-CA', { dateStyle: 'short' })}/`)
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
      .finally(() => (this.loading = false));
    },
  methods: {
    daystatus: function (day) {
        fetch(`http://localhost:8000/ru/vhapi/timetatus/${day}/`).
        then(stream => stream.json()).
        then(response => {
            this.results = response.results;
            console.log(response.results);
        }).
        catch((error) => { console.log(error); this.results = null;}).
        finally(() => {
          this.loading = false;
        });
    },
  }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"
#shedule-time >
  div
    border-radius: 2px
    margin: 4px
    padding: 2px
    width: 64px
    height: 24px

.two
    background: $active-link-line
    border: 1px solid $active-link-line
    color: $white

.three
    background: $ocupado-main
    border: 1px solid $ocupado-sec
    color: $ocupado-text


</style>