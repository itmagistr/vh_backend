<template>
    <div class="col">
      <div class="calendary">
        <div class="d-flex justify-content-between month">
          <div class="d-flex"><button class="btn" @click="decr()"><i class="fas fa-caret-left"></i></button></div>
          <div class="d-flex">{{months[month]}} {{year}}</div>
          <div class="d-flex"><button class="btn" @click="incr()"><i class="fas fa-caret-right"></i></button></div>
        </div>
        <div class="weekday">
          <div v-for="count in dates" :key="count">
            {{ count }}
          </div>
        </div>
        <div class="days">
          <div v-for="count in num" :class="[count.status ===-1 ? 'days-none' : '',
          count.status ===1 ? 'profi' : '', count.status ===2 ? 'few-places' : '',
          count.status ===3 ? 'no-places' : '', count.key === hoy ? 'hoy' : '']" :key="count.key">
            {{ count.day }}
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
            hoy: new Date().toLocaleString('en-CA', { dateStyle: 'short' }),
            month: new Date().getMonth(),
            year: new Date().getFullYear(),
            dates: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
            months: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
            num: null,
            loading: true,
            errored: false,
            results: null
        }
    },
    async created() {
      await this.daystatus(this.hoy, `${this.dat(this.year, this.month + 1, new Date(this.year, this.month + 1, 0).getDate())}`);
    },
    methods: {
        dat: function (year, month, day){
            return new Date(year, month, day).toLocaleString('en-CA', { dateStyle: 'short' });
        },
        daystatus: function (start, finish) {
            fetch(`http://localhost:8000/ru/vhapi/daystatus/${start}/${finish}/`).
            then(stream => stream.json()).
            then(response => {
            this.results = response.results;
            console.log(response.results);
            this.daysInMonth();
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
            let start = `${this.dat(this.year, this.month, 1)}`;
            if (this.hoy === `${this.dat(this.year, this.month, new Date().getDate())}`) {
              start = this.hoy
            }
            this.daystatus(start, `${this.dat(this.year, this.month+1, 0)}`);
        },
        decr: function () {
          this.month--;
          if (this.month < 0) {
            this.month = 11;
            this.year--;
          }
          let start = `${this.dat(this.year, this.month, 1)}`;
          if (this.hoy === `${this.dat(this.year, this.month, new Date().getDate())}`) {
            start = this.hoy;
          }
          this.daystatus(start, `${this.dat(this.year, this.month+1, 0)}`);
        },
        daysInMonth: function () {
            let i;
            let opt = {
                pM: new Date(this.year, this.month, 1).getDay(),
                tM: new Date(this.year, this.month + 1, 0).getDate(),
                nM: 7 - new Date(this.year, this.month + 1, 0).getDay()
            };
            opt.pM = opt.pM = (opt.pM === 0) ? 6 : opt.pM - 1;
            const buf = new Date(this.year, this.month, 0).getDate() + 1;
            this.num = [];

            for(i = buf - opt.pM; i < buf; i++)
                this.num.push({'key': `${this.dat(this.year, this.month-1, i)}`, 'day': i, 'status': -1}); // Дни предыдущего месяца

            let n = 0;
            for (i = 1; i < opt.tM + 1; i++) { // Этот месяц
              const key = `${this.dat(this.year, this.month, i)}`;
              if (this.results !== null && this.hoy < this.dat(this.year, this.month, opt.tM)) { // Есть ответ с сервера и месяц и год не предыдущие
                if (key === this.results[n].d) {
                  this.num.push({'key': key, 'day': i, 'status': this.results[n].s});
                  n += (n + 1 !== this.results.length) ? 1 : 0;
                } else
                this.num.push({'key': key, 'day': i, 'status': 0});
              } else
                this.num.push({'key': key, 'day': i, 'status': 0});
            }
            if (this.num.length < 35) {
                opt.nM += 7;
            }
            for(i = 1; i < opt.nM + 1; i++)
              this.num.push({'key': `${this.dat(this.year, this.month+1, i)}`, 'day': i, 'status': -1}); // Дни следующего месяйа
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
  margin-bottom: 12px

.month > div > .btn
    padding: 0px
    width: 32px
    height: 24px

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

.place
    margin: 0px
    margin-top: 12px

.place i
    display: inline-block
    width: 8px
    height: 8px
    border-radius: 2px

.place > div
    font-family: FuturaBookC
    font-size: 16px
    line-height: 21px
    padding: 0px 8px 0px 8px

.profi
    background-color: $profi-main

.few-places
  background-color: $few-places-main

.no-places
  background-color: $no-places-main

.hoy
  border: 2px solid #1DE0BE
  border-radius: 4px
  padding: 5px!important

.free
  width: 8px
  height: 8px
  background: #1DE0BE
  opacity: 0.5
  border-radius: 2px

</style>