<template>
    <div class="d-flex">
        <div class="row registration">
            <div class="col">
                <div id="calendary"></div>
            </div>
            <div class="col">
                <div id="schedule"></div>
            </div>
        </div>
        <div class="col useful-tips"></div>
    </div>
</template>

<script>
export default {

}
</script>

<style lang="sass">
// colors
// Выгодно
$profi-main: #42e1c5
$profi-sec: #e3faf4

// Мало мест
$few-places-main: #efdbb6

// Нет мест
$no-places-main: #f1ede2
$no-places-sec: #7f817f

// Занято
$taken: #а9а9а7

$ocupado-main: rgba(7, 16, 19, 0.04)
$ocupado-sec: rgba(7, 16, 19, 0.32)

.registration
    background: rgba(254, 253, 251, 0.64)
    backdrop-filter: blur(16px)
    border-radius: 16px
    width: 752px
    height: 586px
    margin: 0px 4px 0px 0px

.useful-tips
    background: rgba(254, 253, 251, 0.64)
    backdrop-filter: blur(16px)
    border-radius: 16px
    width: 265px
    height: 586px
    margin: 0px 0px 0px 4px

#calendary, #schedule
  background: white
  border-radius: 8px
  width: 336px
  margin: 24px 32px

#calendary
  padding: 32px
  margin-right: 8px

#schedule
  padding: 24px
  margin-left: 8px

.col
  padding: 0px!important

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

#weekday, #days, #shedule-time >
  div
    font-family: FuturaBookC
    font-size: 16px
    line-height: 21px
    text-align: center
    vertical-align: middle
    display: inline-block

#weekday, #days
  margin: 0px -4px

#shedule-time >
  div
    border-radius: 2px
    margin: 4px
    padding: 2px
    width: 64px
    height: 24px

    background: $ocupado-main
    border: 1px solid $ocupado-sec

#weekday, #days >
  div
    border-radius: 4px
    margin: 4px
    padding: 7px
    width: 32px
    height: 32px

.nlm
  margin-left: 0px!important
.nrm
  margin-right: 0px!important

.days-selected
  border: $profi-main solid 2px
  background: $profi-sec

.days-none
  color: $no-places-sec

//
.profi
  background-color: $profi-main

.few-places
  background-color: $few-places-main

.no-places
  background-color: $no-places-main
</style>