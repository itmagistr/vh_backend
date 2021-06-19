<template>
    <div class="row">
        <div class="col doctor-choice">
            <div class="table-wrapper-scroll-y ctm-scroll">
                  <div class="menu">
                        <button class="btn" @click="backToBooking()"><i class="fas fa-long-arrow-alt-left"/> {{ $t('doctorchoice.back') }}</button>
                        <div class="input-group">
                            <input type="text" class="form-control" placeholder="Найти процедуру..." aria-describedby="ba2">
                            <div class="input-group-append">
                                <button class="btn" type="button" id="ba2" data-toggle="modal" data-target="#mdl-future-ok"><i class="fas fa-search"></i></button>
                            </div>
                        </div>
                  </div>
                  <div v-if="loading">{{ $t('doctorchoice.dwnld') }}</div>
                  <Card v-for="data in results"
                        :key="data.uid"
                        :data="data"
                        :class="[select === data.uid ? 'active':'' ]"
                        v-on:select="selected"/>
            </div>
            <button class="btn" @click="send()">{{ $t('doctorchoice.choose') }}</button>
        </div>
    </div>
</template>

<script>
import currencyFormat from '@/helpers/currencyFormat';
import timeFormat from "@/helpers/timeFormat";
import Card from "@/components/DoctorCardChoice.vue";
export default {
    props: ['value'],
    data() {
        return {
            select: this.$store.state.Booking.Doctor || 'cc3c3aa6-590a-49c2-b9d1-faf4cf3505a0',
            loading: true,
            errored: false,
            results: null
        }
    },
    async created() {
        await this.docList('', this.$store.state.Booking.Date, []);
    },
    watch: {
      "$i18n.locale": {
        handler(newLocale, oldLocale) {
          if (newLocale === oldLocale)
            return;
          this.docList('', this.$store.state.Booking.Date, []);
        },
        immediate: true,
      },
    },
    components: {
      Card,
    },
    filters: {
      currencyFormat, timeFormat
    },
    methods: {
        docList(cat, date, medProcUID) {
            const options = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({"txt": cat, "dt": date, "spec": medProcUID})
            };
            fetch(`http://localhost:8000/${this.$i18n.locale}/vhapi/doctor/list/`, options).
            then(response => response.json()).
            then(data => {
            this.results = data;
            console.log(data);
            }).
            catch((error) => { console.log(error); this.results = null;}).
            finally(() => {
              for (let i = 0; i < this.results.length; i++)
                if(this.results[i].img === null)
                  this.results[i].img = '/media/uploads/human/defaultAvatar.png';
              this.loading = false;
            });
        },
        backToBooking(){
            this.select = this.$store.state.Booking.Doctor;
            this.$emit('pageDoctor', this.select, 2);
        },
        selected(val){
            this.select = val;
        },
        send(){
            this.$store.commit("updDoc", this.select);
            this.$emit('pageDoctor', this.select, 2);
        },
    }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.doctor-choice
  /*background: linear-gradient(180deg, #FEFDFB 0%, #FEFDFB 78.65%, rgba(254, 253, 251, 0.16) 92.71%, rgba(254, 253, 251, 0.08) 100%)*/
  background: $white
  border-radius: 8px
  height: 536px
  .ctm-scroll
    position: relative
    height: 100%
    padding: 32px
    overflow: auto
    display: flex
    flex-direction: column
  &::-webkit-scrollbar
    display: none

.menu
  height: 48px
  margin-bottom: 24px
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

.doctor-choice
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

@media (max-width: 1399px)
  .doctor-choice
    margin-bottom: 0px!important
    height: 100%
    @media (min-width: 451px)
      .menu
        margin-bottom: 32px
    > .ctm-scroll
      padding: 8px 16px
    > .btn
      display: block
      margin: 50px auto 64px
  .doctor-clip
    width: 100%
@media (max-width: 450px)
  .doctor-choice
    > .btn
      margin: 40px auto 78px
    > .ctm-scroll
      padding: 8px 0px
</style>
