<template>
  <div class="search">
    <modalDoctorList :data="list"/>
    <modalDocCard :selfInfo="selfInfo"/>
    <h3 class="resLabel">
        Найдено {{ res.length }} результатов по запросу "{{ q }}"
    </h3>
    <template v-for="c in res">
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
      <info v-if="prselect === c.uid"
            :key="'block-'+c.uid"
            class="hm-block"
            :info="prselect"
            v-on:showDocM="updCardModal" v-on:showListDocM="updCardListModal"/>
    </template>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import currencyFormat from "@/helpers/currencyFormat";
import timeFormat from "@/helpers/timeFormat";
import info from "@/components/ServicePageInfoProc";
import modalDocCard from "@/components/ModalDocCard";
import modalDoctorList from "@/components/ModalDoctorList";

export default {
  data(){
    return {
      q: this.$store.state.question,
      res: [],
      prselect: '',
      selfInfo: '',
      list: [],
    }
  },
  components:{
    info, modalDocCard, modalDoctorList
  },
  created() {
    this.search();
  },
  computed: mapState(['question']),
  watch: {
    question: {
      handler(newLocale, oldLocale) {
        if (newLocale === oldLocale)
          return;
        this.q = newLocale;
        this.search();
      },
      immediate: true,
    },
  },
  methods: {
      updCardListModal(list) {
        this.list = list;
      },
      updCardModal(uid) {
        this.selfInfo = uid;
      },
    selected(sel, price) {
      if(this.prselect === sel) {
        this.prselect = null;
        this.price = null;
      } else {
        this.prselect = sel;
        this.price = price;
      }
    },
    truncate(str, len) {
      return (str.length > len) ? str.substr(0, len) : str;
    },
    search() {
      return new Promise( () => {
        if (this.q.length < 3) {
          return [];
        }

        const options = {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({"q": this.q})
        };
        fetch(`${this.$store.state.apihost}${this.$i18n.locale}/vhapi/mpsearch/`, options)
        .then(response => response.json()).then(data => {
          this.res = data;
        }).catch((error) => {
          console.log(error);
          this.results = null;
        }).finally(() => {
          console.log(this.res)
          this.loading = false;
        });
        return false;
      });
    },
    clear(){
      this.res = [];
      this.q = '';
    },
  },
  filters: {
      currencyFormat, timeFormat
  },
}
</script>

<style lang="sass">
.search
  background: #FEFDFB
  border-radius: 1rem
  margin: 1rem
  height: calc(100vh - 168px)
  overflow: auto
  &.col
    flex-basis: auto
  > .resLabel
    margin: 1rem 2rem .25rem 2rem
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
  .hm-block
    margin-bottom: 0
@media (max-width: 1399px)
  .search
    margin: 1rem 0
    height: calc(100vh - 96px)

</style>