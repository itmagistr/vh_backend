<template>
    <div class="d-flex flex-column mar">
        <modalDoctorList :data="list"/>
        <modalDocCard :selfInfo="selfInfo"/>
<!--        <div class="bgz-main"></div>-->
        <div class="tittle-of-service">{{ $t('servicepage.service') }}</div>
        <div class="service">
            <div v-for="c in category" class="card-tooth"
                 :class="[{active: catSel === c.code}]"
                 :key="c.code" @click="chgCat(c)">
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
                <listView v-model="prselect" :categoryCode="catSel" :resize="resize" :infoBlock="true" :showDoc="true"
                                 v-on:showDocM="updCardModal" v-on:showListDocM="updCardListModal"/>
                <!--<button class="btn vis" @click="send()">{{ $t('proсchoice.select') }}</button>-->
            </div>
            <info class="block-right col-6" :info="prselect" :resize="resize" :showDoc="true"
                  v-on:showDocM="updCardModal" v-on:showListDocM="updCardListModal"/>
        </div>
    </div>
</template>

<script>
import currencyFormat from '@/helpers/currencyFormat';
import timeFormat from "@/helpers/timeFormat";
import info from "@/components/ServicePageInfoProc";
import listView from "@/components/ProcedureListView";
import modalDocCard from "@/components/ModalDocCard";
import modalDoctorList from "@/components/ModalDoctorList";

export default {
    props: { resize: Boolean },
    data() {
      return {
        select: this.$store.state.Booking.Procedure,
        prselect: this.$store.state.Booking.Procedure,
        selfInfo: '',
        catSel: null,
        catObj: {},
        list: [],
        category: [],
        categoryPre: {},
        price: null,
        loading: true,
        errored: false,
        locale: this.$i18n.locale
      }
    },
    filters: { currencyFormat, timeFormat },
    components: { info, modalDocCard, modalDoctorList, listView },
    async created() {
      this.categoryList();
      this.preBookingReq();
    },
    watch: {
      "$i18n.locale": {
        handler(newLocale, oldLocale) {
          if (newLocale === oldLocale)
            return;
          this.locale = newLocale;
          if (oldLocale !== undefined) this.categoryList();
        },
        immediate: true,
      },
    },
    methods: {
      updCardListModal(list) { this.list = list; },
      updCardModal(uid) { this.selfInfo = uid; },
      chgCat(cat) {
        if (cat.code === this.catSel) {
          this.catSel = this.categoryPre.code;
          this.catObj = this.categoryPre;
        } else {
          this.catSel = cat.code;
          this.catObj = cat;
        }
      },
      preBookingReq() {
        fetch(`${this.$store.state.apihost}${this.$i18n.locale}/vhapi/category/PRE_BOOKING/`).
        then(response => response.json()).
        then(data => { this.categoryPre = data; }).
        catch((error) => { console.log(error); }).
        finally(() => { this.chgCat(this.categoryPre); });
      },
      categoryList() {
        fetch(`${this.$store.state.apihost}${this.$i18n.locale}/vhapi/category/`).
        then(response => response.json()).
        then(data => { this.category = data.results; }).
        catch((error) => { console.log(error); this.results = null;});
      },
      selected(sel, price) {
        this.prselect = sel;
        this.price = price;
      },
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
    > .block-left
      > div:first-child
        margin-left: 16px
</style>
