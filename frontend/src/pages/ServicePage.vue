<template>
    <div class="d-flex flex-column mar">
        <modalDocCard :selfInfo="selfInfo"/>
<!--        <div class="bgz-main"></div>-->
        <div class="tittle-of-service">{{ $t('servicepage.service') }}</div>
        <div class="service">
            <div v-for="c in category" class="card-tooth"
                 :class="[{active: catSel === c.code}]"
                 :key="c.code"
                  @click="chgCat(c)">
              <div>
                <img :src="c.img"/>
                <div>{{c.title}}</div>
              </div>
            </div>
        </div>
        <div class="block-2">
            <div class="block-top">
                <div class="tittle">
                    {{ catObj.title }}
                </div>
                <div class="text">
                    {{ catObj.description }}
                </div>
            </div>
            <!--<div class="accordion">
                TODO
            </div>-->
        </div>
        <div class="block-3">
            <div class="block-left col-6">
                <div>{{ $t('servicepage.price') }}</div>
                <template v-for="c in results">
                    <div class="product"
                         :class="[{spec: c.code.length > 5}, { active: c.uid === prselect}]"
                         :key="c.uid"
                         @click="selected(c.uid, c.price)">
                        <div class="sr-start">
                          <!--<div class="pr-code">{{ c.code }}</div>-->
                          <div class="pr-tittle">{{ c.title_check }}</div>
                        </div>
                        <div class="sr-end">
                          <div class="pr-price">{{ c.price | currencyFormat("RUB")}}</div>
                          <!--<div class="pr-duration">{{ c.duration | timeFormat("ru-RU")}}</div>-->
                          <div class="pr-duration">{{ c.duration}} {{$t("servicepage.min")}}</div>
                        </div>
                    </div>
                    <info v-if="prselect === c.uid && resize"
                          :key="'block-'+c.uid"
                          class="hm-block"
                          :info="prselect"/>
                </template>
                <!--<button class="btn vis" @click="send()">{{ $t('proсchoice.select') }}</button>-->
            </div>
            <info class="block-right col-6" :info="prselect" :resize="resize" v-on:showDocM="updCardModal"/>
        </div>
    </div>
</template>

<script>
import currencyFormat from '@/helpers/currencyFormat';
import timeFormat from "@/helpers/timeFormat";
import info from "@/components/ServicePageInfoProc";
import modalDocCard from "@/components/ModalDocCard";

export default {
    props: ['resize'],
    data() {
      return {
        select: this.$store.state.Booking.Procedure,
        prselect: this.$store.state.Booking.Procedure,
        selfInfo: '',
        catSel: null,
        catObj: {},
        category: [],
        doc: null,
        price: null,
        loading: true,
        errored: false,
        results: null,
        locale: this.$i18n.locale
      }
    },
    components:{
      info, modalDocCard,
    },
    async mounted() {
      //await this.getMedProc("Орто", "2021-03-21", "bf0f0856-f57d-48c6-b99c-b3c8a2e3ea82");
      this.categoryList();
    },
    watch: {
      "$i18n.locale": {
        handler(newLocale, oldLocale) {
          if (newLocale === oldLocale)
            return;
          this.locale = newLocale;
          this.categoryList();
        },
        immediate: true,
      },
    },
    methods: {
      updCardModal(uid) {
        this.selfInfo = uid;
      },
      chgCat(cat){
        this.catSel = cat.code;
        //this.catSel = 'PRE_BOOKING';
        this.catObj = cat;
        //this.getMedProc(this.$store.state.Booking.Date, [{code: this.catSel}]);
      },
      categoryList() {
        fetch(`${this.$store.state.apihost}${this.$i18n.locale}/vhapi/category/`).
        then(response => response.json()).
        then(data => {
        this.category = data.results;
        console.log(data.results);
        }).
        catch((error) => { console.log(error); this.results = null;}).
        finally(() => {
          if(this.catSel === null) {
            this.chgCat(this.category[0]);
          } else
            for(let i = 0; i < this.category.length; i++)
              if(this.category[i].code === this.catSel)
                this.chgCat(this.category[i]);
          this.getMedProc(this.$store.state.Booking.Date, [{code: 'PRE_BOOKING'}]);
          this.loading = false;
        });
      },
      getMedProc(date, catSel) {
        const options = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({"dt": date, "category": catSel})
        };
        fetch(`${this.$store.state.apihost}${this.locale}/vhapi/medproc/list/`, options).
        then(response => response.json()).
        then(data => {
          this.results = data;
          if(!this.resize && this.results.length > 0)
            this.prselect = this.results[0].uid;
          console.log(data);
        }).
        catch((error) => { console.log(error); this.results = null;}).
        finally(() => {
          this.loading = false;
        });
      },
      selected(sel, price){
        if(this.prselect === sel) {
          this.prselect = null;
          this.price = null;
        } else {
          this.prselect = sel;
          this.price = price;
        }
      },
      send() {
        this.$store.commit("updProc", this.prselect);
        this.$store.commit("updPrice", this.price);
        //this.$emit('pageProcedure', this.select, 2);
      }
    },
    filters: {
        currencyFormat, timeFormat
    },
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"
body.chg-proc
  // backdrop-filter: blur(16px)
  background: #F6F3ED
  > main
    // background-color: rgba(254, 253, 251, 0.64)
    > .container
      padding-top: 27px
    > div
      > .modal
        height: 100vh
  > header
    background: #F6F3ED
    // backdrop-filter: none
.bgz-main
  background: #F6F3ED
  position: absolute
  z-index: -1
  width: 100%
  height: 105%
  left: 0
  top: 378px

.mar
    width: calc(100% - 152px)
    > div.service
        text-align: center
        overflow: auto
        max-width: 100%
        display: flex
        margin: auto
    .tittle-of-service
        text-align: center
        font-family: FuturaBookC
        font-size: 64px
        line-height: 61px
        color: $button-color
        margin-bottom: 56px

.card-tooth
  background: #F3E9D4
  border-radius: 8px
  margin: 0px 16px
  &:first-child
      margin-left: 1px
  &:last-child
    margin-right: 1px
  &.active
    background: $active-link-line
  &.active > div > div
    color: $white
  > div
    width: 200px
    height: 200px
    padding: 40px 0
    > img
      margin-bottom: 36px
    > div
      font-family: FuturaBookC
      font-style: normal
      font-weight: normal
      font-size: 16px
      line-height: 21px
      text-align: center
      letter-spacing: 0.08em
      text-transform: uppercase
      color: $button-color

.block-2
  margin-top: 64px
  text-align: center
  display: block!important
  .tittle
    font-family: FuturaBookC
    font-size: 48px
    line-height: 56px
    color: $button-color
  .text
    font-family: FuturaBookC
    font-size: 16px
    line-height: 21px
  .accordion
    margin-top: 38px
    margin-left: auto
    margin-right: auto
    width: calc(100% - 64px)
    height: 236px
    background: #00C0BB55
    border-radius: 16px

.block-3
  max-width: 100%
  margin: 64px 0 128px
  display: flex
  .btn
    padding: 0px
  > .block-left, .block-right
    // height: 867px
    // width: 681px
    width: 100%

.block-left
  border-radius: 16px 0px 0px 16px
  background: $white
  padding: 32px 0px
  position: relative
  text-align: left
  > div:first-child
    margin-left: 32px
    font-family: Montserrat
    font-weight: 500
    font-size: 21px
    line-height: 26px
    margin-bottom: 32px
  > .product
    padding: .25rem 2rem
    display: flex
    justify-content: space-between
    > div
      > div
        margin: auto
    &.active, &:hover
      background: rgba(238, 209, 153, 0.16)
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
      > .pr-price
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
  > .vis
    display: block
    margin: 40px auto 64px
    font-family: FuturaBookC
    letter-spacing: 0.08em
    text-transform: uppercase
    width: 300px
    height: 48px
    background: $active-link-line
    border: none
    border-radius: 8px
    color: $white

@media (max-width: 1399px)
  .chg-proc
    .container
      padding: 0
      .mar
        width: 100%
        > .bgz-main
          top: 308px
        > .tittle-of-service, > .service, > .block-2
          padding: 0 1rem
        > .block-3
          margin: 64px 0
          .block-left
            max-width: inherit
            padding: 32px 0px
            width: 100%
            height: 100%
            border-radius: 16px
            &.col-6
              flex: inherit
            .vis
              display: none
          .block-right
            display: none
            width: 100%
            height: 100%
            border-radius: 0px
@media (max-width: 450px)
  .block-3
    margin: 64px -16px 0
    > .block-left
      > div:first-child
        margin-left: 16px
      > .product
        padding: .25rem 1rem
        > .sr-end
          margin-left: .5rem
          flex-direction: column
          > .pr-price
            margin-right: 0
</style>
