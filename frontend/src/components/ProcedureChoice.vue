<template>
    <div class="row">
        <div class="col procedure-choice">
            <div class="table-wrapper-scroll-y my-custom-scrollbar">
                  <div class="menu">
                        <button class="btn" @click="backToBooking()"><i class="fas fa-long-arrow-alt-left"/> Назад</button>
                        <div class="input-group">
                            <input type="text" class="form-control" placeholder="Найти процедуру..." aria-describedby="ba2">
                            <div class="input-group-append">
                                <button class="btn" type="button" id="ba2"><i class="fas fa-search"></i></button>
                            </div>
                        </div>
                  </div>
                  <div v-if="loading">Загрузка...</div>
                  <table class="table table-borderless">
                        <tbody v-for="n in cat" :key="n.uid">
                              <tr class="category">
                                    <td><div class="icon-teeth"><img :src="n.img" alt=""/></div></td>
                                    <td class="cat-name" colspan="4">{{n.title}}</td>
                              </tr>
                              <tr v-for="c in n.results" class="product" :class="[{spec: c.code.length > 5}, { active: c.uid === select}]" :key="c.uid" @click="selected(c.uid)">
                                    <td class="pr-code">{{ c.code }}</td>
                                    <td class="pr-tittle">{{ c.title }}</td>
                                    <td class="pr-info"><i class="fas fa-info-circle"></i></td>
                                    <td class="pr-price">{{ c.price | currencyFormat("RUB")}}</td>
                                    <td class="pr-duration">{{ c.duration | timeFormat("ru-RU")}}</td>
                              </tr>
                              <hr>
                        </tbody>
                  </table>
            </div>
            <button class="btn" @click="send()">Выбрать процедуру</button>
        </div>
    </div>
</template>

<script>
import currencyFormat from '@/helpers/currencyFormat';
import timeFormat from "@/helpers/timeFormat";

export default {
    props: ['date'],
    data() {
        return {
            select: this.$store.state.Booking.Procedure,
            cat: [
                { uid: '18abdf34-516f-4e95-9b61-2d2052d4f60d', img: '/img/Teeth/Orthodontics.svg', title: '01. Ортодонтия', results: [] },
                { uid: '72c10fc6-350a-42ef-888a-4835f88de9ca', img: '/img/Teeth/Implantation.svg', title: '02. Хирургия', results: [] },
            ],
            loading: true,
            errored: false,
            results: null,
        }
    },
    async mounted() {
        await this.medProcList('Орт', this.$store.state.Booking.Date, 'bf0f0856-f57d-48c6-b99c-b3c8a2e3ea82', 0);
        await this.medProcList('Прот', this.$store.state.Booking.Date, 'bf0f0856-f57d-48c6-b99c-b3c8a2e3ea82', 1);
    },
    filters: {
        currencyFormat, timeFormat
    },
    methods: {
        medProcList(cat, date, docUID, section) {
            const options = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({"txt": cat, "dt": date, "doctor_uid": docUID})
            };
            fetch(`http://localhost:8000/ru/vhapi/medproc/list/`, options).
            then(response => response.json()).
            then(data => {
            this.results = data;
            console.log(data);
            }).
            catch((error) => { console.log(error); this.results = null;}).
            finally(() => {
              this.loading = false;
              this.cat[section].results = this.results;
            });
        },
        backToBooking(){
            this.select = this.$store.state.Booking.Procedure;
            this.$emit('pageProcedure', this.select, 2);
        },
        selected(val) {
            this.select = val;
        },
        send() {
            this.$store.commit("updProc", this.select);
            this.$emit('pageProcedure', this.select, 2);
        }
    }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.procedure-choice
    /*background: linear-gradient(180deg, #FEFDFB 0%, #FEFDFB 78.65%, rgba(254, 253, 251, 0.16) 92.71%, rgba(254, 253, 251, 0.08) 100%)*/
    background: $white
    border-radius: 8px
    height: 536px

.my-custom-scrollbar
      position: relative
      height: 100%
      padding: 32px
      overflow: auto

//.table-wrapper-scroll-y
//      box-shadow: inset 0 -200px 200px -200px white

::-webkit-scrollbar
      width: 0px
/*::-webkit-scrollbar-track
      background: #F1EEE6*/
/*::-webkit-scrollbar-thumb
      background: rgba(238, 209, 153, 0.32)*/
/*::-webkit-scrollbar-thumb:hover
      background: rgba(238, 209, 153, 0.32)*/


.table td, .table th
    display: inline-table
    padding: 0px
    vertical-align: middle

.menu
    height: 64px
.menu > .btn
    display: inline-block
    font-family: FuturaBookC
    font-size: 16px
    line-height: 21px
    color: #071013
    margin-right: 25px
    padding: 6px 0px
    box-shadow: none
.menu .form-control::placeholder
    color: rgba( 238,209,153,0.32)
    font-family: FuturaBookC
    font-size: 16px
    line-height: 21px
.menu .input-group
    width: 533px
    display: inline-flex
.menu input
    height: 48px
    border-radius: 8px
#ba2 .fas
    transform: scaleX(-1)
    color: #B8882F
#ba2
    background: white

.category > td
    margin-bottom: 16px
.category > td:first-child
    margin-right: 16px

.icon-teeth
    display: table-cell
    vertical-align: middle
    text-align: center
    width: 56px
    height: 56px
    background: $active-link-line
    border-radius: 4px
.icon-teeth > img
    width: 32px
    height: 32px
.cat-name
    font-family: Montserrat
    font-style: normal
    font-weight: 500
    font-size: 21px
    line-height: 26px
    color: #071013

.product
    > td
        display: inline-table
        margin: 0px 8px
    > td:first-child
        margin: 0px 0px 8px
    > td:last-child
        margin-right: 0px
    > td
        margin-bottom: 8px
    &.active, &:hover
        background: rgba(238, 209, 153, 0.16)
    &.active > .pr-info > i, &:hover > .pr-info > i
        display: inline-table
    &.active > .pr-price, &:hover > .pr-price
        color: #B8882F
    &.active > .pr-duration, &:hover > .pr-duration
        color: #071013

    .pr-code
        width: 48px
        font-family: Montserrat
        font-size: 19px
        line-height: 24px
        color: #071013
    .pr-tittle
        width: 376px
        font-family: FuturaBookC
        line-height: 16px
        color: #071013
    .pr-info
        width: 16px
    .pr-info > i
        display: none
        font-size: 16px
        color: #42E1C5
    .pr-price
        width: 72px
        font-family: FuturaBookC
        line-height: 21px
        text-align: right
        color: #DFB971
    .pr-duration
        width: 56px
        font-family: FuturaBookC
        line-height: 21px
        text-align: right
        color: #9CC6BE
    &.spec
        > .pr-code
            width: 120px
            font-size: 16px
            line-height: 21px
        > .pr-tittle
            width: 300px

.procedure-choice
    > .btn
        font-family: FuturaBookC
        letter-spacing: 0.08em
        text-transform: uppercase
        width: 233px
        height: 48px
        background: $active-link-line
        border: none
        border-radius: 8px
        color: $white
        position: absolute
        bottom: -9%
        right: 15%
        transform: translate(-50%, -50%)
    hr
        margin-top: .5em
        width: 632px
        border: 1px solid #F3E9D4
</style>