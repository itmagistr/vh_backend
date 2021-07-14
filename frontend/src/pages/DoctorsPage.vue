<template>
    <div class="d-flex flex-column doc">
        <modalDocCard :selfInfo="selfInfo"/>
        <div class="tittle-of-doctor">{{ $t('doctorpage.doc_header') }}</div>
        <div class="filter">
            <div @click="allFilters" :class="{active: allBtn.st}">
              <img src="http://localhost:8000/media/uploads/doctorspec/defaultTeeth.svg">{{ $t('doctorpage.all') }}
            </div>
            <div :class="{active: c.st}" v-for="(c, index) in category" :key="index" @click="updCat(index)">
                <img :src="c.img"/>{{ c.title }}
            </div>
        </div>
        <div class="algo">
            <div class="card-doc" v-for="c in doc" :key="c.uid">
                <div class="docPhoto">
                  <img :src="'http://localhost:8000' + c.img"/>
                </div>
                <div class="info">
                    <div class="top">
                        <div class="icon"><img :src="'http://localhost:8000' + c.special_img"></div>
                        <div class="bk1">
                            <div class="tittle">{{ c.special }}</div>
                            <div class="education">{{ expFormat(c.experience) }}, {{ c.level }}</div>
                        </div>
                    </div>
                    <div class="bottom">
                        <div class="name">{{ c.firstName }} {{ c.lastName }}</div>
                        <StarRating class="clip-rating" :rating="parseFloat(c.rating)" :read-only="true" :increment="0.1"
                                    active-color="#DFB971" inactive-color="#F1EEE6"
                                    :show-rating="false" :star-size="22"/>
                        <div class="clip-review">{{ c.reviewCount }} {{ $t('doctorchoice.review') }}</div>
                    </div>
                </div>
                <button class="btn" data-toggle="modal" data-target="#mdl-doc-card" @click="updCardModal(c.uid)">{{$t('doctorpage.details')}}</button>
            </div>
        </div>
       <input type="range" min="1" :max="(doc.length - 1) * 312" value="1" id="slider" @input="check">
    </div>
</template>

<script>
import currencyFormat from '@/helpers/currencyFormat';
import timeFormat from "@/helpers/timeFormat";
import StarRating from "vue-star-rating";
import modalDocCard from "@/components/ModalDocCard.vue";

export default {
  data() {
    return {
      select: this.$store.state.Booking.Procedure,
      allBtn: {
        st: false
      },
      category: [],
      doc: [],
      loading: true,
      errored: false,
      results: null,
      selfInfo: null,
      sliderLen: 0,
      slider: 0,
      locale: this.$i18n.locale,
    }
  },
  async created() {
    await this.docList("", this.$store.state.Booking.Date, this.vuel);
    this.specList();
  },
  components: {
    StarRating, modalDocCard,
  },
  filters: {
    currencyFormat, timeFormat
  },
  computed: {
    vuel() {
      let tmp = [];
      for(let i = 0; i < this.category.length; i++)
        if(this.category[i].st)
          tmp.push({ code: this.category[i].code })
      return tmp;
    },
    otro() {
      if(document.getElementsByClassName("algo")[0].offsetWidth <= this.doc.length * 348 - 32)
        return 0;
      else
        return 1;
    }
  },
  methods: {
    allFilters(){
      if(this.allBtn.st === false){
        this.allBtn.st = !this.allBtn.st;
        for(let i = 0; i < this.category.length; i++)
          this.category[i].st = true;
      } else{
         this.allBtn.st = false;
        for(let i = 0; i < this.category.length; i++)
          this.category[i].st = false;
      }
      this.docList("", this.$store.state.Booking.Date, this.vuel);
    },
    expFormat(v) {
      if (v >= 5) return "" + this.$t('doctorpage.experience') + " " + v + " "+ this.$t('doctorpage.exp5')
      if ([2, 3, 4].indexOf(v) >= 0) return "" + this.$t('doctorpage.experience') + " " + v + " " + this.$t('doctorpage.exp2')
      if (v == 1) return "" + this.$t('doctorpage.experience') + " " + v + " " + this.$t('doctorpage.exp1')
    },
    updCardModal(uid){
      this.selfInfo = uid;
    },
    docList(cat, date, specs) {
      const options = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({"txt": cat, "dt": date, "spec": specs})
      };
      fetch(`${this.$store.state.apihost}${this.$i18n.locale}/vhapi/doctor/list/`, options).
      then(response => response.json()).
      then(data => {
      this.doc = data;
      console.log(data);
      }).
      catch((error) => { console.log(error); this.results = null; }).
      finally(() => {
        for (let i = 0; i < this.doc.length; i++) {
          if(this.doc[i].img === null)
            this.doc[i].img = '/media/uploads/human/defaultAvatar.png';
          if(this.doc[i].special_img === null || this.doc[i].special_img === undefined)
            this.doc[i].special_img = '/media/uploads/doctorspec/defaultTeeth.svg';
        }
        this.loading = false;
      });
    },
    specList() {
      fetch(`${this.$store.state.apihost}${this.$i18n.locale}/vhapi/doctor/spec/list/`).
      then(response => response.json()).
      then(data => {
        this.category = [];
        for (let i = 0; i < data.count; i++){
          const buf = data.results[i];
          let img = buf.img;
          if(img === null)
            img = `${this.$store.state.apihost}media/uploads/doctorspec/defaultTeeth.svg`;
          this.category.push({ code: buf.code, title: buf.title, img: img, st: false });
        }
      }).
      catch((error) => { console.log(error); this.results = null;}).
      finally(() => {
        this.loading = false;
      });
    },
    updCat(el){
      this.category[el].st = !this.category[el].st;
      for (let i = 0; i < this.category.length; i++){
        if (this.category[i].st === false) {
          this.allBtn.st = false;
          break;
        }
        if(this.category.length - 1 === i && this.category[i].st === true)
          this.allBtn.st = true;
      }
      this.docList("", this.$store.state.Booking.Date, this.vuel);
    },
    check(e) {
      console.log(e);
    }
  },
  mounted() {
    const slider = document.getElementById("slider");
    const acco = document.getElementsByClassName("algo")[0];
    console.log(document.getElementsByClassName("algo"));
    this.sliderLen = acco.scrollWidth + 60;
    acco.addEventListener('scroll', function() {
      console.log(acco.scrollLeft + " " + acco.scrollWidth);
      slider.value = acco.scrollLeft;
    });
    slider.oninput = function() {
      acco.scrollTo(this.value, 0);
    }
    this.$watch( "$i18n.locale",
      (newLocale, oldLocale) => {
        if (newLocale === oldLocale) {
          return
        }
        this.locale = newLocale;
        this.docList("", this.$store.state.Booking.Date, this.vuel);
        this.specList();
      },
      { immediate: true }
    )
  },
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"
$minW: 769px
body.chg-doc
  background: #F6F3ED
  > header
    background: #F6F3ED
.tittle-of-doctor
  text-align: center
  font-family: FuturaBookC
  font-size: 64px
  line-height: 61px
  color: $button-color
  margin-bottom: 56px
  margin-top: 27px

.doc
  width: 100%
  @media (min-width: 1400px)
    width: calc(100% - 248px)
  margin: auto
  > .filter
    display: flex
    flex-wrap: wrap
    justify-content: center
    > div
      height: 32px
      margin: 8px
      padding: 6px 16px
      line-height: 1rem
      background: #F3E9D4
      border-radius: 27px
      color: $none
      > img
        height: 18px
        margin-right: 8px
      &.active
        background: $active-link-line
        color: $white
      &:hover
        background: #A5E8DC
        color: $white
    &::-webkit-scrollbar
      display: none
  > .algo
    margin: 40px auto auto
    @media (min-width: $minW)
      overflow: auto
      width: 100%
      display: flex
      height: 486px
    &::-webkit-scrollbar
      display: none
    > .card-doc
      position: relative
      width: 316px
      height: 452px
      background: $white
      border-radius: 8px
      border: none
      margin: 0px 16px
      @media (min-width: $minW)
        &:first-child
            margin-left: 0px
        &:last-child
            margin-right: 0px
      > .info
        padding: 16px 24px
        > .top
          display: flex
          margin-bottom: 16px
          > .icon
            background: $active-link-line
            width: 40px
            height: 40px
            margin-right: 8px
            border-radius: 4px
            padding: 8px
            text-align: center
            vertical-align: middle
            display: inline-block
            > img
              width: 24px
              height: 24px
          > .bk1
            display: inline-block
            vertical-align: middle
            > .tittle
              font-family: FuturaBookC
              font-size: 16px
              line-height: 21px
              color: $button-color
              padding-bottom: 4px
            > .education
              font-family: Montserrat
              font-size: 14px
              line-height: 16px
        > .bottom
          > .name
            font-family: Montserrat
            font-weight: 500
            font-size: 21px
            line-height: 26px
          > .clip-rating
            font-size: 22px
            line-height: 22px
            margin: 1rem .5rem auto auto
            display: inline-flex
            > div
              > span
                margin-right: 4px!important
          > .clip-review, .clip-icons
            vertical-align: bottom
            font-family: FuturaBookC
            font-size: 16px
            line-height: 21px
            color: $blue_three
            display: inline-flex
      > div.docPhoto
        display: flex
        justify-content: center
        background: $backgroundImage
        width: 316px
        height: 240px
        border-radius: 8px
        border: none
        > img
          height: 240px
      .btn
        position: absolute
        font-family: FuturaBookC
        font-size: 16px
        line-height: 21px
        letter-spacing: 0.08em
        text-transform: uppercase
        color: $white
        background: $active-link-line
        border-radius: 8px
        padding: 12px 32px
        bottom: -20px
        left: 25%
        border: none
  > #slider
    -webkit-appearance: none
    width: 320px
    height: 8px
    margin: 1rem auto 0
    border-radius: 8px
    background: #D2E9E5
    outline: none
    &::-webkit-slider-thumb
      -webkit-appearance: none
      appearance: none
      width: 80px
      height: 8px
      border-radius: 8px
      background: #42E1C5
      cursor: pointer
    &::-moz-range-thumb
      width: 25px
      height: 25px
      background: #42E1C5
      cursor: pointer

@media (max-width: 768px)
  .doc
    width: 100%
    > .algo
      max-width: 696px
      display: flex
      flex-wrap: wrap
      align-content: center
      margin: 32px auto auto
      > .card-doc
        margin: auto auto 52px
    > #slider
      display: none
</style>
