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
                  <table class="table table-borderless">
                        <tbody v-for="n in cat" :key="n.tittle">
                              <tr class="category">
                                    <td><div class="icon-teeth"><img :src="n.img" alt=""/></div></td>
                                    <td class="cat-name" colspan="4">{{n.tittle}}</td>
                              </tr>
                              <tr v-for="c in n.results" class="product" :class="[{spec: c.code.length > 5}, { active: c.uuid === select}]" :key="c.uuid" @click="selected(c.uuid)">
                                    <td class="pr-code">{{ c.code }}</td>
                                    <td class="pr-tittle">{{ c.tittle }}</td>
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
                {uuid: '18abdf34-516f-4e95-9b61-2d2052d4f60d', img: '/img/Teeth/Orthodontics.svg', tittle: '01. Ортодонтия', results: [
                    {uuid: '41b6e7a0-e395-45d3-bccb-ad097c427643', code: '01.01', tittle: 'Установка брекетов', price: 150000, duration: 90},
                    {uuid: '951a9eb9-e0a4-444c-a060-a1d6a1e65181', code: '01.02', tittle: 'Замена брекет-системы', price: 3000, duration: 30},
                    {uuid: '86862dce-dcee-4fed-9f84-5568cd2ce088', code: '01.03', tittle: 'Очень длинное название процедуры, очень длинное', price: 10000, duration: 120},
                    {uuid: '222acbed-7f8b-45c4-b113-2b0df57f2b74', code: '01.03.01', tittle: 'Очень длинное название процедуры, очень длинное врач Василенко Л.И.', price: 10000, duration: 90},
                    {uuid: '9e165e33-0205-4f10-b57a-94cc7009037a', code: '01.03.02', tittle: 'Очень длинное название процедуры, очень длинное врач Василенко Л.И.', price: 15000, duration: 90},
                    {uuid: '181c9634-de66-44fa-a4fe-d7a59f8842ce', code: '01.04', tittle: 'Изготовление Капп', price: 500, duration: 15},]
                },
                {uuid: '72c10fc6-350a-42ef-888a-4835f88de9ca', img: '/img/Teeth/Implantation.svg', tittle: '02. Хирургия', results: [
                    {uuid: 'c210c3c5-f406-43ea-ae0a-85c99fc8b30e', code: '01.01', tittle: 'Установка брекетов', price: 150000, duration: 90},
                    {uuid: '3a7e973e-1df8-4ec3-8954-2df798f6bac6', code: '01.02', tittle: 'Замена брекет-системы', price: 3000, duration: 30},
                    {uuid: '341c9610-addd-45f2-8bc1-f4529956cc7a', code: '01.03', tittle: 'Очень длинное название процедуры, очень длинное', price: 10000, duration: 120},
                    {uuid: '697940ed-05d2-4f77-b5b1-d50b0c8dcc4c', code: '01.03.01', tittle: 'Очень длинное название процедуры, очень длинное врач Василенко Л.И.', price: 10000, duration: 90},
                    {uuid: '7e182f76-b16e-4885-b913-6bcd07ba3c68', code: '01.03.02', tittle: 'Очень длинное название процедуры, очень длинное врач Василенко Л.И.', price: 15000, duration: 90},
                    {uuid: 'd8853c50-282f-4a14-9866-c72cc2b32dd7', code: '01.04', tittle: 'Изготовление Капп', price: 500, duration: 15},]
                },
            ],
        }
    },
    filters: {
        currencyFormat, timeFormat
    },
    methods: {
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

.procedure-choice hr
    margin-top: .5em
    width: 632px
    border: 1px solid #F3E9D4

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

.product > td
    display: inline-table
    margin: 0px 8px
.product > td:first-child
      margin: 0px 0px 8px
.product > td:last-child
    margin-right: 0px
.product > td
    margin-bottom: 8px
.product.active, .product:hover
    background: rgba(238, 209, 153, 0.16)
.product.active > .pr-info > i, .product:hover > .pr-info > i
    display: inline-table
.product.active > .pr-price, .product:hover > .pr-price
    color: #B8882F
.product.active > .pr-duration, .product:hover > .pr-duration
    color: #071013

.pr-code
    width: 48px
    font-family: Montserrat
    font-size: 19px
    line-height: 24px
    color: #071013
.product.spec > .pr-code
    width: 64px
    font-size: 16px
    line-height: 21px

.pr-tittle
    width: 376px
    font-family: FuturaBookC
    line-height: 16px
    color: #071013
.product.spec > .pr-tittle
    width: 360px

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

.procedure-choice > .btn
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
</style>