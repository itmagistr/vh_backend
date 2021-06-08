<template>
  <div class="row">
    <div class="col procedure-choice">
      <div class="table-wrapper-scroll-y ctm-scroll">
        <div class="menu">
          <button class="btn" @click="backToBooking()"><i class="fas fa-long-arrow-alt-left"/> {{ $t('proсchoice.back') }}</button>
          <div class="input-group">
            <input v-model='q' type="text" class="form-control" placeholder="Найти процедуру..." aria-describedby="ba2">
            <div class="input-group-append">
              <button class="btn" type="button" id="ba2" @click="search()"><i class="fas fa-search"></i></button>
            </div>
          </div>
        </div>
        <div v-if="loading">{{ $t('proсchoice.load') }}</div>
          <div v-for="n in cat" :key="n.uid">
            <div class="category">
              <div><div class="icon-teeth"><img :src="n.img" alt=""/></div></div>
              <div class="cat-name" colspan="4">{{n.title}}</div>
            </div>
            <div v-for="c in n.results" class="product" :class="[{spec: c.code.length > 5}, { active: c.uid === select}]" :key="c.uid" @click="selected(c.uid, c.price)">
              <div class="sr-start">
                <div class="pr-code">{{ c.code }}</div>
                <div class="pr-tittle">{{ c.title_check }}</div>
              </div>
              <div class="sr-end">
                <div class="pr-info"><i class="fas fa-info-circle"></i></div>
                <div class="pr-price">{{ c.price | currencyFormat("RUB")}}</div>
                <div class="pr-duration">{{ c.duration | timeFormat("ru-RU")}}</div>
              </div>
            </div>
            <hr>
          </div>
      </div>
      <button class="btn" @click="send()">{{ $t('proсchoice.select') }}</button>
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
            price: this.$store.state.Booking.Price,
            cat: [
                { uid: '18abdf34-516f-4e95-9b61-2d2052d4f60d', img: '/img/Teeth/Orthodontics.svg', title: '01. Ортодонтия', results: [] },
                { uid: '72c10fc6-350a-42ef-888a-4835f88de9ca', img: '/img/Teeth/Implantation.svg', title: '02. Хирургия', results: [] },
            ],
            loading: true,
            errored: false,
            results: [],
            q: '',
        }
    },
    async created() {
        await this.medProcList('', this.$store.state.Booking.Date, 'bf0f0856-f57d-48c6-b99c-b3c8a2e3ea82', 0);
        /*await this.medProcList('Прот', this.$store.state.Booking.Date, 'bf0f0856-f57d-48c6-b99c-b3c8a2e3ea82', 1);*/
    },
    mounted(){
        this.$watch( "$i18n.locale",
            (newLocale, oldLocale) => {
                if (newLocale === oldLocale)
                  return;
               this.medProcList('', this.$store.state.Booking.Date, 'bf0f0856-f57d-48c6-b99c-b3c8a2e3ea82', 0);
            },
            { immediate: true }
        );
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
            fetch(`http://localhost:8000/${this.$i18n.locale}/vhapi/medproc/list/`, options).
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
        search() {
            const options = {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({"q": this.q})
            };
            fetch(`http://localhost:8000/${this.$i18n.locale}/vhapi/mpsearch/`, options).
            then(response => response.json()).
            then(data => {
              this.results = data;
              console.log(data);
            }).
            catch((error) => { console.log(error); this.results = null;}).
            finally(() => {
              this.loading = false;
              this.cat[0].results = this.results;
            });
        },
        backToBooking(){
            this.select = this.$store.state.Booking.Procedure;
            this.$emit('pageProcedure', this.select, 2);
        },
        selected(val, price) {
            this.select = val;
            this.price = price;
        },
        send() {
            this.$store.commit("updProc", this.select);
            this.$store.commit("updPrice", this.price);
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
  .ctm-scroll
    position: relative
    height: 100%
    padding: 0
    overflow: auto
  &::-webkit-scrollbar
        display: none

//.table-wrapper-scroll-y
//      box-shadow: inset 0 -200px 200px -200px white
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

.procedure-choice
  .menu
    height: 48px
    margin: 32px 32px
    > .btn
      display: inline-block
      font-family: FuturaBookC
      font-size: 16px
      line-height: 21px
      color: #071013
      margin-right: 25px
      padding: 6px 0px
      box-shadow: none
    .form-control
      &::placeholder
        color: rgba( 238,209,153,0.32)
        font-family: FuturaBookC
        font-size: 16px
        line-height: 21px
    .input-group
      width: calc(100% - 87px)
      display: inline-flex
    input
      height: 48px
      border-radius: 8px
    #ba2 .fas
      transform: scaleX(-1)
      color: #B8882F
    #ba2
      background: white
  .category
    padding: 0 2rem 1rem
    display: flex
    justify-content: flex-start
    > div
      margin: auto 0
      &:first-child
        margin-right: 16px
      > .icon-teeth
        display: table-cell
        vertical-align: middle
        text-align: center
        width: 56px
        height: 56px
        background: $active-link-line
        border-radius: 4px
        > img
          width: 32px
          height: 32px
    > .cat-name
      font-family: Montserrat
      font-style: normal
      font-weight: 500
      font-size: 21px
      line-height: 26px
      color: #071013
  .product
    padding: .25rem 2rem
    display: flex
    justify-content: space-between
    > div
      > div
        margin: auto
    &.active, &:hover
      background: rgba(238, 209, 153, 0.16)
    &.active > .sr-end > .pr-info > i, &:hover > .sr-end > .pr-info > i
      display: flex
    &.active > .sr-end > .pr-price, &:hover > .sr-end > .pr-price
      color: #B8882F
    &.active > .sr-end > .pr-duration, &:hover > .sr-end > .pr-duration
      color: #071013
    > .sr-start
      display: flex
      justify-content: flex-start
      > .pr-code
        width: 62px
        margin-right: 8px
        font-family: Montserrat
        font-size: 19px
        line-height: 24px
        color: #071013
      > .pr-tittle
        font-family: FuturaBookC
        color: #071013
    > .sr-end
      display: flex
      justify-content: flex-end
      > .pr-info
        width: 16px
        > i
          display: none
          font-size: 16px
          color: #42E1C5
      > .pr-price
        width: 72px
        font-family: FuturaBookC
        line-height: 21px
        text-align: right
        color: #DFB971
        margin-right: 1rem
      > .pr-duration
        width: 56px
        font-family: FuturaBookC
        line-height: 21px
        text-align: right
        color: #9CC6BE
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
    @media (min-width: 1399px)
      position: relative
      left: 50%
      transform: translate(-50%, -50%)
  hr
    margin-top: .5em
    width: 100%
    border: 1px solid #F3E9D4

@media (max-width: 1399px)
  .procedure-choice
    @media (min-width: 451px)
      .menu
        margin: 8px 16px 32px
    height: 100%
    .category
      padding: 0 1rem .5rem
    .product
      padding: .25rem 1rem
    > .btn
      display: block
      margin: 42px auto 64px
@media (max-width: 450px)
  .procedure-choice
    .product
      > .sr-end
        margin-left: .5rem
        flex-direction: column
        > .pr-info
          display: none
        > .pr-price
          margin-right: 0
</style>
