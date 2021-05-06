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
                  <div class="doctor-clip" v-for="data in results" :key="data.uid" :class="[select === data.uid ? 'active':'' ]"  @click="selected(data.uid)">
                        <div class="d-flex clip-header">
                            <div class="d-flex">
                                <div class="clip-photo"></div>
                                <div class="clip-bk1">
                                    <div class="clip-tittle">{{ data.special }}</div>
                                    <div class="clip-name">{{ data.firstName }} {{ data.lastName }} <br> {{ data.midName }}</div>
                                </div>
                            </div>
                            <div class="d-flex flex-column clip-info">
                                <div>{{ data.experience }}</div>
                                <div>{{ data.level }}</div>
                                <div>{{ data.degree }}</div>
                            </div>
                        </div>
                        <div class="clip-body">
                            <div class="clip-accordion">{{ $t('doctorchoice.procedure') }} <i class="fas fa-caret-down"></i></div>
                            <div class="clip-accordion">{{ $t('doctorchoice.photo') }} <i class="fas fa-caret-down"></i></div>
                            <div class="clip-accordion">Youtube <i class="fas fa-caret-down"></i></div>
                            <div class="clip-accordion">{{ $t('doctorchoice.certificate') }} <i class="fas fa-caret-down"></i></div>
                            <div class="clip-accordion">{{ $t('doctorchoice.education') }} <i class="fas fa-caret-down"></i></div>
                        </div>
                        <div class="d-flex clip-footer">
                            <div>
                                <StarRating class="clip-rating" :rating="parseFloat(data.rating)" :read-only="true" :increment="0.1"
                                        active-color="#DFB971" inactive-color="#F1EEE6"
                                        :show-rating="false" :star-size="22"/>
                                <div class="d-flex clip-review">{{ data.reviewCount }} {{ $t('doctorchoice.review') }}</div>
                            </div>
                                <div class="d-flex clip-icons">
                                    <i class="fas fa-phone" style="transform: scaleX(-1)"/>
                                    <img src="/img/chat.svg"/>
                                    <i class="fas fa-heart"/>
                                </div>
                        </div>
                  </div>
            </div>
            <button class="btn" @click="send()">{{ $t('doctorchoice.choose') }}</button>
        </div>
    </div>
</template>

<script>
import currencyFormat from '@/helpers/currencyFormat';
import timeFormat from "@/helpers/timeFormat";
import StarRating from "vue-star-rating";

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
    components: {
      StarRating,
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

.doctor-clip
  display: flex
  flex-direction: column
  border: 1px solid rgba(238, 209, 153, 0.32)
  border-radius: 8px
  width: 624px
  margin-bottom: 16px
  padding: 24px
  &:hover, &.active
      border: 2px solid #42E1C5
  > .clip-header
    justify-content: space-between
    margin-bottom: 16px
    .clip-photo
      width: 64px
      height: 64px
      background: $active-link-line
      border-radius: 4px
      margin-right: 12px
    .clip-bk1
      vertical-align: top
      .clip-tittle
        font-family: FuturaBookC
        font-size: 14px
        line-height: 16px
        color: #B8882F
        padding-top: 4px
        padding-bottom: 4px
      .clip-name
        font-family: Montserrat
        font-size: 19px
        line-height: 19px
        color: #071013
    .clip-info
      text-align: right
      font-family: FuturaBookC
      font-size: 16px
      line-height: 21px
      color: #071013
  > .clip-body
    display: flex
    flex-direction: column
    margin-bottom: 1.5rem
    .clip-accordion
      font-family: FuturaBookC
      font-size: 16px
      line-height: 21px
      letter-spacing: 0.08em
      text-transform: uppercase
      color: #071013
      margin: .25rem 0
      > i
       margin-left: 8px
       color: $blue_three
  > .clip-footer
    justify-content: space-between
    vertical-align: middle
    > div
      display: flex
      >.clip-rating
        font-size: 22px
        line-height: 22px
        margin-right: .5rem
        display: inline-flex
        > div
          > span
            margin-right: 4px!important
    .clip-review, .clip-icons
      vertical-align: bottom
      font-family: FuturaBookC
      font-size: 16px
      line-height: 21px
      color: $blue_three
    .clip-icons
      font-size: 22px
      line-height: 22px
      color: $blue_three
      > i, img
        margin-left: 16px

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
