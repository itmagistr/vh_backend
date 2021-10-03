<template>
  <div class="listView">
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
            <div v-if="infoButton" @click="detail(c.uid)" class="pr-info"><i class="fas fa-info-circle"></i></div>
            <div class="pr-price">{{ c.price | currencyFormat("RUB")}}</div>
            <!--<div class="pr-duration">{{ c.duration | timeFormat("ru-RU")}}</div>-->
            <div class="pr-duration">{{ c.duration }} {{$t("servicepage.min")}}</div>
          </div>
      </div>
      <info v-if="prselect === c.uid && resize && infoBlock"
            :key="'block-' + c.uid" class="hm-block" :info="prselect"
            v-on:showDocM="updCardModal" v-on:showListDocM="updCardListModal"/>
    </template>
  </div>
</template>

<script>
import currencyFormat from '@/helpers/currencyFormat';
import timeFormat from "@/helpers/timeFormat";
import info from "@/components/ServicePageInfoProc";

export default {
    props: {
      categoryCode: String,
      doctorUID: String,
      resize: Boolean,
      infoButton: Boolean,
      infoBlock: Boolean
    },
    data() {
      return {
        select: this.$store.state.Booking.Procedure,
        prselect: this.$store.state.Booking.Procedure,
        list: [],
        catSel: null,
        docSel: null,
        price: null,
        loading: true,
        errored: false,
        results: null,
        locale: this.$i18n.locale
      }
    },
    components: { info },
    mounted() {
      if(this.categoryCode !== undefined)
        this.medProcListByCat();
      else if(this.doctorUID !== undefined)
        this.medProcListByDoc();
    },
    watch: {
      "$i18n.locale": {
        handler(newLocale, oldLocale) {
          if (newLocale === oldLocale)
            return;
          this.locale = newLocale;
          if (this.categoryCode !== undefined)
              this.medProcListByCat();
          else if (this.doctorUID !== undefined)
              this.medProcListByDoc();
        },
        immediate: true,
      },
      categoryCode(newValue, oldValue) {
        if (newValue === oldValue)
          return;
        this.catSel = newValue;
        this.medProcListByCat();
      },
      doctorUID(newValue, oldValue) {
        if (newValue === oldValue)
          return;
        this.docSel = newValue;
        this.medProcListByDoc();
      },
    },
    methods: {
      detail(uid){
        console.log(uid);
      },
      updCardModal(next) { this.$emit('showDocM', next); },
      updCardListModal(next) { this.$emit('showListDocM', next); },
      medProcListByCat() {
        if (this.catSel === null)
          return;
        const options = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({"dt": this.$store.state.Booking.Date, "category": [{code: this.catSel}]})
        };
        fetch(`${this.$store.state.apihost}${this.locale}/vhapi/medproc/list/`, options)
            .then(response => response.json())
            .then(data => {
              this.results = data;
              if (!this.resize && this.results.length > 0 && this.infoBlock)
                this.selected(this.results[0].uid, 0);
            })
            .catch((error) => { console.log(error); this.results = null; })
            .finally(() => {
              this.loading = false;
            });
      },
      medProcListByDoc() {
        if (this.docSel === null)
          return;
        fetch(`${this.$store.state.apihost}${this.$i18n.locale}/vhapi/doctor/${this.docSel}/medprocs/`).
        then(response => response.json()).
        then(data => {
          this.results = data.results;
          console.log(data);
        }).
        catch((error) => { console.log(error); this.results = null;}).
        finally(() => {
          this.loading = false;
        });
      },
      selected(sel, price) {
        if (this.prselect === sel) {
          this.prselect = null;
          this.price = null;
        } else {
          this.prselect = sel;
          this.price = price;
        }
        this.$emit('input', sel);
      },
      send() {
        this.$store.commit("updProc", this.prselect);
        this.$store.commit("updPrice", this.price);
      }
    },
    filters: { currencyFormat, timeFormat },
}
</script>

<style lang="sass">
.listView
  > .product
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
        margin-right: 1rem
        > i
          display: none
          font-size: 16px
          color: #42E1C5
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

@media (max-width: 450px)
  .listView
    > .product
      padding: .25rem 1rem
      > .sr-end
        margin-left: .5rem
        flex-direction: column
        > .pr-price
          margin-right: 0
</style>