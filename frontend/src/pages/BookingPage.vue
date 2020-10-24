<template>
    <div class="d-flex">
        <div class="registration">
            <div class="row">
                <Procedure></Procedure>
                <Doctor></Doctor>
            </div>
            <div class="row">
                <Calendary></Calendary>
                <Shedule></Shedule>
            </div>
        </div>
        <div class="col useful-tips"></div>
    </div>
</template>

<script>
import Doctor from "@/components/Doctor";
import Procedure from "@/components/Procedure";
import Calendary from "@/components/Calendary";
import Shedule from "@/components/Shedule";
export default {
    components: {
        Doctor, Procedure, Calendary, Shedule
    }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.registration
    background: rgba(254, 253, 251, 0.64)
    backdrop-filter: blur(16px)
    border-radius: 16px
    width: 752px
    height: 586px
    margin: 0px 4px 0px 0px
    padding: 32px
.useful-tips
    background: rgba(254, 253, 251, 0.64)
    backdrop-filter: blur(16px)
    border-radius: 16px
    width: 265px
    height: 586px
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

.schedule
  padding: 24px

.weekday, .days, #shedule-time >
  div
    font-family: FuturaBookC
    font-size: 16px
    line-height: 21px
    text-align: center
    vertical-align: middle
    display: inline-block

//
.profi
  background-color: $profi-main

.few-places
  background-color: $few-places-main

.no-places
  background-color: $no-places-main
</style>