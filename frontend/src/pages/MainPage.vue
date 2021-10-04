<template>
    <div class="d-flex ctm-main">
        <div class="cl-full">
            <!--<div class="calen">
                <div class="cl-day" >
                    <img src="/img/calendary.svg"/>
                    <span>{{day}}</span>
                </div>
                <div class="cl-month">{{$t(`months.m${month}`)}}</div>
            </div>-->
            <!--<router-link tag="button" class="btn" data-toggle="modal"
                    data-dismiss="modal" data-target="#mdl-future-ok" to="#">{{ $t('bookingpage.calendar') }}</router-link>-->
        </div>
    </div>
</template>

<script>
export default {
    data() {
      return {
        day: new Date().getDate(),
        month: new Date().getMonth(),
        }
    }
};
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.ctm-main
  display: flex
  justify-content: center
  align-items: center
  height: calc(100vh - 136px)
.calen
  width: 120px
  height: 148px
  background: rgba(254, 253, 251, 0.64)
  backdrop-filter: blur(24px)
  border-radius: 8px
  text-align: center
  color: $button-color

.cl-day
  padding-top: 28px
  position: relative
  text-align: center
  > span
    font-size: 24px
    line-height: 26px
    font-weight: 300
    font-style: normal
    position: absolute
    top: 80%
    left: 50%
    transform: translate(-50%, -50%)

.cl-month
  margin-top: 4px
  font-family: FuturaBookC
  font-size: 16px
  line-height: 21px

.cl-full
  margin-top: 50vh
  position: relative
  text-align: center
  .btn
    font-family: FuturaBookC
    letter-spacing: 0.08em
    text-transform: uppercase
    width: 289px
    height: 48px
    background: #42E1C5
    border: none
    border-radius: 8px
    color: $white
    position: absolute
    bottom: -30%
    transform: translate(-50%, -50%)

@media (max-width: 1399px)
  .ctm-main
    height: calc(100vh - 64px)!important
</style>
