<template>
    <div class="col">
        <div class="schedule">
          <div class="month">{{day}} {{months[month]}} {{year}}</div>
          <div id="shedule-time">
              <div v-for="count in results" :class="{ 'two': count.s === 2, 'three':  count.s === 3 }"
                 :key="count.t" @click="selected(count.t)"> {{ count.t }} </div>
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
            select: this.$store.state.Booking.Hour,
            date: this.$store.state.Booking.Date,
            day: null,
            month: null,
            year: null,
            months: ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря'],
            results: null
        }
    },
    async created() {
        this.day = new Date(this.date).getDate();
        this.month = new Date(this.date).getMonth();
        this.year = new Date(this.date).getFullYear();
        await this.daystatus(this.date);
    },
    methods: {
        daystatus(day) {
            fetch(`http://localhost:8000/ru/vhapi/timestatus/${day}/`).
            then(stream => stream.json()).
            then(response => {
                this.results = response.results;
            }).
            catch((error) => {
                console.log(error);
                this.errored = true;
                this.results = null;
            })
            .finally(() => {
                this.loading = false;
            });
        },
        selected(val){
            this.select = val;
            this.$store.commit("updHour", this.select);
        }
    }
}
//TODO Доделать отобажение расписания после выбора дня в Календаре. Сейчас расписание обновляеться после возврата с люьой страницы.
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