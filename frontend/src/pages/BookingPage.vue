<template>
    <div class="d-flex">
        <div class="registration">
            <div class="row">
                <Procedure/>
                <Doctor/>
            </div>
            <div class="row">
                <Calendary/>
                <Shedule/>
            </div>
            <div style="text-align: center; margin-top: 16px;">
                <span class="title-price">Стоимость: </span>
                <span class="price">{{ 5000 | numberFormat}} ₽</span>
            </div>
            <router-link tag="button" class="btn" :to="{name: 'booking'}">Записаться</router-link>
        </div>
        <div v-if="$store.state.usefulTips" class="col useful-tips"></div>
    </div>
</template>

<script>
import Doctor from "@/components/Doctor";
import Procedure from "@/components/Procedure";
import Calendary from "@/components/Calendary";
import Shedule from "@/components/Shedule";
import numberFormat from '@/helpers/numberFormat';

export default {
    filters: {
        numberFormat,
    },
    components: {
        Doctor, Procedure, Calendary, Shedule
    }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.registration, .useful-tips
    background: rgba(254, 253, 251, 0.64)
    backdrop-filter: blur(16px)
    border-radius: 16px
    /*height: 586px*/
    height: 627px

.registration
    width: 752px
    margin: 0px 4px 0px 0px
    padding: 32px
    position: relative

.useful-tips
    width: 265px
    margin: 0px 0px 0px 4px

.registration > .row > .col:first-child
    margin-right: 8px
.registration > .row > .col:last-child
    margin-left: 8px
.col
    padding: 0px
.registration > .row > .col
    width: 336px
.registration > .row
    margin: 0px
.registration > .row:first-child
    margin-bottom: 24px

.calendary, .schedule, .doctor, .procedure
  background: white
  border-radius: 8px

.calendary
  padding: 32px
  height: 413px

.schedule
  padding: 24px
  height: 413px

.weekday, .days, #shedule-time >
  div
    font-family: FuturaBookC
    font-size: 16px
    line-height: 21px
    text-align: center
    vertical-align: middle
    display: inline-block

.registration > .btn
    font-family: FuturaBookC
    letter-spacing: 0.08em
    text-transform: uppercase
    width: 171px
    height: 48px
    background: #42E1C5
    border: none
    border-radius: 8px
    color: $white
    position: absolute
    bottom: -9%
    right: 27%
    transform: translate(-50%, -50%)

.title-price
    font-family: FuturaBookC;
    font-size: 22px
    line-height: 21px

.price
    font-family: Montserrat
    font-style: normal
    font-weight: 600
    font-size: 27px
    line-height: 33px
    color: #E1BE7A

</style>