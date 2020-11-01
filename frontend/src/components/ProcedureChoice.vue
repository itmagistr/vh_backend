<template>
    <div class="row">
        <div class="col procedure-choice">

            <div class="table-wrapper-scroll-y my-custom-scrollbar">
                  <div class="menu">
                        <button class="btn" ><i class="fas fa-long-arrow-alt-left"/> Назад</button>
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
                              <tr v-for="c in n.results" class="product" :class="[c.date.length > 5 ? 'spec' : '']" :key="c.date">
                                    <td class="pr-date">{{ c.date }}</td>
                                    <td class="pr-tittle">{{ c.tittle }}</td>
                                    <td class="pr-info"><i class="fas fa-info-circle"></i></td>
                                    <td class="pr-price">{{ c.price | currencyFormat("RUB")}}</td>
                                    <td class="pr-duration">{{ c.duration | timeFormat("ru-RU")}}</td>
                              </tr>
                              <hr>
                        </tbody>
                  </table>
            </div>
        </div>
    </div>
</template>

<script>
import currencyFormat from '@/helpers/currencyFormat';
import timeFormat from "@/helpers/timeFormat";

export default {
      data() {
            return {
                  cat: [{img: '/img/Teeth/Orthodontics.svg', tittle: '01. Ортодонтия', results: [{date: '01.01', tittle: 'Установка брекетов', price: 150000, duration: 90},
                  {date: '01.02', tittle: 'Замена брекет-системы', price: 3000, duration: 30},
                  {date: '01.03', tittle: 'Очень длинное название процедуры, очень длинное', price: 10000, duration: 120},
                  {date: '01.03.01', tittle: 'Очень длинное название процедуры, очень длинное врач Василенко Л.И.', price: 10000, duration: 90},
                  {date: '01.03.02', tittle: 'Очень длинное название процедуры, очень длинное врач Василенко Л.И.', price: 15000, duration: 90},
                  {date: '01.04', tittle: 'Изготовление Капп', price: 500, duration: 15},]
                  },
                  {img: '/img/Teeth/Implantation.svg', tittle: '02. Хирургия', results: [{date: '01.01', tittle: 'Установка брекетов', price: 150000, duration: 90},
                  {date: '01.02', tittle: 'Замена брекет-системы', price: 3000, duration: 30},
                  {date: '01.03', tittle: 'Очень длинное название процедуры, очень длинное', price: 10000, duration: 120},
                  {date: '01.03.01', tittle: 'Очень длинное название процедуры, очень длинное врач Василенко Л.И.', price: 10000, duration: 90},
                  {date: '01.03.02', tittle: 'Очень длинное название процедуры, очень длинное врач Василенко Л.И.', price: 15000, duration: 90},
                  {date: '01.04', tittle: 'Изготовление Капп', price: 500, duration: 15},]
                  },],
            }
      },
      filters: {
            currencyFormat, timeFormat
      },
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.procedure-choice
    background: linear-gradient(180deg, #FEFDFB 0%, #FEFDFB 78.65%, rgba(254, 253, 251, 0.16) 92.71%, rgba(254, 253, 251, 0.08) 100%)
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
.product:hover
    background: rgba(238, 209, 153, 0.16)
.product:hover > .pr-info > i
    display: inline-table
.product:hover > .pr-price
    color: #B8882F
.product:hover > .pr-duration
    color: #071013

.pr-date
    width: 48px
    font-family: Montserrat
    font-size: 19px
    line-height: 24px
    color: #071013
.product.spec > .pr-date
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
</style>