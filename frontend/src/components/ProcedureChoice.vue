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
        <div v-for="n in category" :key="n.code">
          <div class="category">
            <div><div class="icon-teeth"><img :src="n.img" alt=""/></div></div>
            <div class="cat-name">{{n.title}}</div>
          </div>
          <listView
            :categoryCode="n.code"
            v-model="select"/>
          <hr>
        </div>
      </div>
      <button class="btn" @click="send()">{{ $t('proсchoice.select') }}</button>
    </div>
  </div>
</template>

<script>
import listView from "@/components/ProcedureListView";

export default {
    props: ['date'],
    data() {
        return {
            select: this.$store.state.Booking.Procedure,
            price: this.$store.state.Booking.Price,
            loading: true,
            errored: false,
            category: [],
            q: '',
        }
    },
    components: {
        listView
    },
    async created() {
      //await this.categoryList();
      //await this.medProcList('', this.$store.state.Booking.Date, 'bf0f0856-f57d-48c6-b99c-b3c8a2e3ea82', 0);
      /*await this.medProcList('Прот', this.$store.state.Booking.Date, 'bf0f0856-f57d-48c6-b99c-b3c8a2e3ea82', 1);*/
    },
    watch: {
      "$i18n.locale": {
        handler(newLocale, oldLocale) {
          if (newLocale === oldLocale)
            return;
          this.categoryList();
        },
        immediate: true,
      },
    },
    methods: {
        categoryList() {
            fetch(`${this.$store.state.apihost}${this.$i18n.locale}/vhapi/category/`).
            then(response => response.json()).
            then(data => {
            this.category = data.results;
            console.log(data.results);
            }).
            catch((error) => { console.log(error); this.results = null;}).
            finally(() => {
              this.loading = false;
            });
        },
        search() {
            const options = {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({"q": this.q})
            };
            fetch(`${this.$store.state.apihost}${this.$i18n.locale}/vhapi/mpsearch/`, options).
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
