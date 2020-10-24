<template>
    <div class="col">
      <div class="calendary">
        <div class="month">
          <button class="btn" @click="decr()"><i class="fas fa-caret-left"></i></button>
          <div>{{months[month]}} {{year}}</div>
          <button class="btn" @click="incr()"><i class="fas fa-caret-right"></i></button>
        </div>
        <div class="weekday">
          <div v-for="count in dates" :key="count">
            {{ count }}
          </div>
        </div>
        <div class="days">
          <div v-for="count in daysInMonth()" :class="[count.status !=1 ? 'days-none' : '']" :key="count.key">
            {{ count.day }}
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
    data() {
      return {
            month: new Date().getMonth(),
            year: new Date().getFullYear(),
            dates: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
            months: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
            loading: true,
            errored: false,
            results: null
        }
    },
    async created() {
      await fetch(`http://localhost:8000/ru/vhapi/daystatus/${new Date().toLocaleString('en-CA', { dateStyle: 'short' })}/${this.year}-${this.month + 1}-${new Date(this.year, this.month + 1, 0).getDate()}/`)
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
        daystatus: function (start, finish) {
            fetch(`http://localhost:8000/ru/vhapi/daystatus/${start}/${finish}/`).
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
        incr: function () {
            this.month++;
            if (this.month > 11) {
                this.month = 0
                this.year++;
            }
            const d = new Date().toLocaleString('en-CA', { dateStyle: 'short' });
            let start = `${this.year}-${this.month + 1}-`;
            if (d !== `${this.year}-${this.month+1}-${new Date().getDate()}`) {
              start += `1`
            } else
              start = d

            this.daystatus(start, `${this.year}-${this.month+1}-${new Date(this.year, this.month + 1, 0).getDate()}`);
        },
        decr: function () {
          this.month--;
          if (this.month < 0) {
            this.month = 11;
            this.year--;
          }
          var d = new Date().toLocaleString('en-CA', { dateStyle: 'short' });
            var start = `${this.year}-${this.month+1}-`;
            if (d !== `${this.year}-${this.month+1}-${new Date().getDate()}`) {
              start += `1`
            } else
              start = d
          this.daystatus(start, `${this.year}-${this.month+1}-${new Date(this.year, this.month + 1, 0).getDate()}`);
        },
        daysInMonth: function () {
            var lastMonth = new Date(this.year, this.month, 1).getDay();
            lastMonth = (lastMonth == 0) ? 6 : lastMonth - 1; //Получаю кол-во дней предыдущего месяца, если есть
            var countDay = new Date(this.year, this.month + 1, 0).getDate(); //Получаю кол-во дней в этом месяце
            var nextMonth = 7 - new Date(this.year, this.month + 1, 0).getDay(); //Получаю кол-во дней следующего месяца, если есть
            var buf = new Date(this.year, this.month, 0).getDate() + 1;
            var send = [];

            for(var i = buf - lastMonth; i < buf; i++)
                send.push({'key': `${this.year}-${this.month-1}-${i}`, 'day': i, 'status': 0});
            for(i = 1; i < countDay + 1;i++)
                send.push({'key': `${this.year}-${this.month}-${i}`, 'day': i, 'status': 1});
            for(i = 1; i < nextMonth + 1; i++)
                send.push({'key': `${this.year}-${this.month+1}-${i}`, 'day': i, 'status': 2});
            return send;
        },
    }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.month
  font-family: Montserrat
  font-size: 19px
  line-height: 24px
  text-align: center
  margin-bottom: 16px

.month >
  div
    display: inline-block
    width: 70%
    padding: 5px 0px

.weekday, .days
  margin: 0px -4px

.weekday, .days >
  div
    border-radius: 4px
    margin: 4px
    padding: 7px
    width: 32px
    height: 32px

.days-selected
  border: $profi-main solid 2px
  background: $profi-sec

.days-none
  color: $no-places-sec
</style>