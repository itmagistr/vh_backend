<template>
  <div>
    <div v-for="c in results" class="product"
         :class="[{spec: c.code.length > 5}, { active: c.uid === select}]"
         :key="c.uid"
         @click="selected(c.uid, c.price)">
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
    </div>
</template>

<script>
import currencyFormat from '@/helpers/currencyFormat';
import timeFormat from "@/helpers/timeFormat";

export default {
  props: ['value', 'categoryCode', 'doctorUID'],
  data() {
    return {
      select: this.value,
      results: [],
    }
  },
  filters: {
      currencyFormat, timeFormat
  },
  mounted() {
    if(this.categoryCode !== undefined)
      this.medProcListByCat(this.$store.state.Booking.Date, [{code: this.categoryCode}]);
    else if(this.doctorUID !== undefined)
      this.medProcListByDoc(this.doctorUID);
  },
  watch: {
    value(newValue, oldValue) {
      if (newValue === oldValue)
        return;
      this.select = this.value;
    },
    doctorUID(newValue, oldValue) {
      if (newValue === oldValue)
        return;
      this.medProcListByDoc(this.doctorUID);
    },
  },
  methods: {
    selected(val) {
      this.$emit('input', val);
      this.select = val;
    },
    medProcListByCat(date, docUID) {
      const options = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({"dt": date, "category": docUID})
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
      });
    },
    medProcListByDoc(docUID) {
      fetch(`http://localhost:8000/${this.$i18n.locale}/vhapi/doctor/${docUID}/medprocs/`).
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
  }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

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
</style>
