<template>
    <div class="d-flex flex-column doc">
        <div class="tittle-of-doctor">{{ $t('doctorpage.doc_header') }}</div>
        <div class="filter">
            <div :class="{active: c.st}" v-for="(c, index) in category" :key="index" @click="updCat(index)">
                <img :src="c.img"/>{{ c.title }}
            </div>
        </div>
        <div class="algo">
            <div class="card-doc" v-for="c in doc" :key="c.uid">
                <img :src="c.img"/>
                <div class="info">
                    <div class="top">
                        <div class="icon"><img :src="c.imgCat"></div>
                        <div class="bk1">
                            <div class="tittle">{{ c.special }}</div>
                            <div class="education">{{ c.degree }}</div>
                        </div>
                    </div>
                    <div class="bottom">
                        <div class="name">{{ c.firstName }} {{ c.lastName }}</div>
                        <div class="d-flex clip-rating">
                            <i class="fas fa-star star-full"></i>
                            <i class="fas fa-star star-full"></i>
                            <i class="fas fa-star star-full"></i>
                            <i class="fas fa-star star-half"></i>
                            <i class="fas fa-star star-none"></i>
                        </div>
                        <div class="d-flex clip-review">{{ c.reviewCount }} {{ $t('doctorchoice.review') }}</div>
                    </div>
                </div>
                <button class="btn" data-toggle="modal" data-target="#mdl-doc-card" @click="updCardModal(c.uid)">{{$t('doctorpage.details')}}</button>
            </div>
        </div>
       <input type="range" min="1" :max="(doc.length - 1) * 348 - 32" value="1" id="slider">
    </div>
</template>

<script>
import currencyFormat from '@/helpers/currencyFormat';
import timeFormat from "@/helpers/timeFormat";

export default {
  data() {
    return {
      select: this.$store.state.Booking.Procedure,
      category: [],
      doc: [
        { uid: 'fa85a9ec-c7e8-466e-b3af-d852777db5f1', img: '/img/Teeth/Orthodontics.svg',
          imgCat: '/img/Teeth/Orthodontics.svg', tittle: 'Стоматлог, Ортодонт', fName: 'Лариса',
          lName: 'Василенко', tName: '', arg1: 'стаж 19 лет',
          arg2: 'высшая кат.', arg3: 'КМН', rating: 5, countReview: 24,
        },
        { uid: '6f5773c0-c8b0-475d-8851-4ca909afeca4', img: '/img/Teeth/Orthodontics.svg',
          imgCat: '/img/Teeth/Orthodontics.svg', tittle: 'Стоматлог, Ортодонт', fName: 'Лариса',
          lName: 'Василенко', tName: '', arg1: 'стаж 19 лет',
          arg2: 'высшая кат.', arg3: 'КМН', rating: 5, countReview: 24,
        },
        { uid: 'd28573a8-36a0-4293-bccf-acc6f56295e2', img: '/img/teeth/Surgery.svg',
          imgCat: '/img/teeth/Surgery.svg', tittle: 'Хирург', fName: 'Лариса',
          lName: 'Василенко', tName: '', arg1: 'стаж 19 лет',
          arg2: 'высшая кат.', arg3: 'КМН', rating: 5, countReview: 24,
        },
        { uid: 'd4da8973-0f6a-4de3-9bc0-3a7bc6f5b9fe', img: '/img/teeth/Surgery.svg',
          imgCat: '/img/teeth/Surgery.svg', tittle: 'Хирург', fName: 'Лариса',
          lName: 'Василенко', tName: '', arg1: 'стаж 19 лет',
          arg2: 'высшая кат.', arg3: 'КМН', rating: 4, countReview: 24,
        },
      ],
      loading: true,
      errored: false,
      results: null,
      locale: this.$i18n.locale
    }
  },
  async created() {
    await this.docList("", this.$store.state.Booking.Date, this.vuel);
    this.specList();
  },
  filters: {
    currencyFormat, timeFormat
  },
  computed: {
    vuel() {
      let tmp = [];
      for(let i = 0; i < this.category.length; i++)
        if(this.category[i].st)
          tmp.push({ code: this.category[i].code, title: this.category[i].title })
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
    updCardModal(uid){
      console.log(uid);
    },
    docList(cat, date, specs) {
      const options = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({"txt": cat, "dt": date, "spec": specs})
      };
      fetch(`http://localhost:8000/${this.$i18n.locale}/vhapi/doctor/list/`, options).
      then(response => response.json()).
      then(data => {
      this.doc = data;
      console.log(data);
      }).
      catch((error) => { console.log(error); this.results = null;}).
      finally(() => {
        this.loading = false;
      });
    },
    specList() {
      fetch(`http://localhost:8000/${this.$i18n.locale}/vhapi/doctor/spec/list/`).
      then(response => response.json()).
      then(data => {
        for (let i = 0; i < data.count; i++){
          const buf = data.results[i];
          this.category.push({ code: buf.code, title: buf.title, st: false });
        }
      }).
      catch((error) => { console.log(error); this.results = null;}).
      finally(() => {
        this.loading = false;
      });
    },
    updCat(el){
      for(let i = 0; i < this.category.length; i++){
        if (i === el){
          this.category[i].st = !this.category[i].st;
          this.docList("", this.$store.state.Booking.Date, this.vuel);
          break;
        }
      }
    },
  },
  mounted() {
    const slider = document.getElementById("slider");
    const acco = document.getElementsByClassName("algo")[0];
    acco.addEventListener('scroll', function(){
      console.log(acco.scrollLeft + " " + acco.offsetWidth);
      slider.value = acco.scrollLeft;
    });
    slider.oninput = function() {
      acco.scrollTo(this.value, 0);
    }
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
  .container
    padding: initial
.tittle-of-doctor
  text-align: center
  font-family: FuturaBookC
  font-size: 64px
  line-height: 61px
  color: $button-color
  margin-bottom: 56px
  margin-top: -100px

.doc
  width: 100%
  > .filter
    > div
      height: 32px
      margin: 8px
      padding: 6px 16px
      line-height: 1rem
      display: inline-block
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
      width: calc(100% - 32px)
      display: flex
      height: 486px
    &::-webkit-scrollbar
      display: none
    > .card-doc
      position: relative
      display: inline-block
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
            margin: 1rem .75rem auto auto
            display: inline-flex!important
            > i
              margin-right: 4px
          > .clip-review, .clip-icons
            font-family: FuturaBookC
            font-size: 16px
            line-height: 21px
            color: $blue_three
            display: inline-flex!important
      > img
        background: $active-link-line
        width: 316px
        height: 240px
        border-radius: 8px
        border: none
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
        left: 75px
        border: none
  > #slider
    -webkit-appearance: none
    width: 320px
    height: 8px
    margin: 56px auto 0
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
    > .algo
      max-width: 696px
      margin: 32px auto auto
      > .card-doc
        margin: 26px 16px 26px
    > #slider
      display: none
@media (max-width: 727px)
  .doc
    > .algo
      margin: 32px auto auto
      > .card-doc
        display: block
        margin: auto auto 52px
</style>
