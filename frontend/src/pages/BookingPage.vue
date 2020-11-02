<template>
    <div class="d-flex">
        <div v-if="phase === 2" class="registration">
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
                <span class="price">{{ 5000 | currencyFormat("RUB")}}</span>
            </div>
            <button class="btn" :to="{name: 'booking'}" @click="phase++">Записаться</button>
        </div>
        <div v-else-if="phase === 3" class="registration">
            <ProcedureChoice/>
            <button class="btn" :to="{name: 'booking'}" @click="phase++">Процедуры</button><!--Кнопка имеет смещение к окну в центре-->
        </div>
        <div v-else-if="phase === 4" class="registration">
            <DoctorChoice/>
            <button class="btn" :to="{name: 'booking'}" @click="phase=2">Доктора</button>
        </div>
<!--        <transition name="fade" mode="in-out">-->
            <div v-if="!utstate" class="shadow">
                <button type="button" class="btn" @click="changeUT"><i class="fas fa-caret-right"/></button>
            </div>
<!--        </transition>-->
<!--        <transition name="fade" mode="in-out">-->
            <div v-if="utstate" class="col useful-tips" >
                <button type="button" class="btn close" @click="changeUT">
                  <span class="fas fa-caret-left"></span>
                </button>
            </div>
<!--        </transition>-->
    </div>
</template>

<script>
import Doctor from "@/components/Doctor";
import Procedure from "@/components/Procedure";
import Calendary from "@/components/Calendary";
import Shedule from "@/components/Shedule";
import currencyFormat from '@/helpers/currencyFormat';
import ProcedureChoice from "@/components/ProcedureChoice";
import DoctorChoice from "@/components/DoctorChoice";

export default {
    data() {
        return{
            phase: 2,
            utstate: true
        }
    },
    filters: {
        currencyFormat,
    },
    mounted() {
        this.utstate = this.$store.state.usefulTips;
    },
    components: {
        Doctor, Procedure, Calendary, Shedule, ProcedureChoice, DoctorChoice
    },
    methods: {
        changeUT: function(){
            this.utstate = !this.utstate;
            this.$store.commit("updateUT", this.utstate);
        }
    }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.slide-fade-enter-active
  transition: all .8s ease
.slide-fade-leave-active
  transition: all .3s cubic-bezier(1.0, 0.5, 0.8, 1.0)
.slide-fade-enter, .slide-fade-leave-to
  transform: translateX(10px)
  opacity: 0

.registration, .useful-tips
    background: rgba(254, 253, 251, 0.64)
    backdrop-filter: blur(16px)
    border-radius: 16px
    height: 627px

.registration
    width: 752px
    margin: 0px 4px 0px 0px
    padding: 32px 32px 56px
    position: relative
    z-index: 3

.useful-tips
    width: 265px
    margin: 0px 0px 0px 4px

.useful-tips > .close
    width: 32px
    height: 32px
    box-shadow: none

.shadow
    position: relative
.shadow > button
    background: $none
    color: $white
    border-radius: 0px 8px 8px 0px
    width: 10px
    height: 72px
    position: absolute
    top: 11%
    transform: translate(-50%, -50%)
    z-index: 1
.shadow > button:hover
    color: $white

.calendary, .procedure
    margin-right: 8px
.schedule, .doctor
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