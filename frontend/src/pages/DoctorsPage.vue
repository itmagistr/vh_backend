<template>
    <div class="d-flex flex-column doc">
        <div class="tittle-of-doctor">Врачи</div>
        <div class="filter">
            <div :class="{active: c.st}" v-for="c in category" :key="c.uid" @click="updCat(c.uid)">
                <img :src="c.img"/>{{ c.tittle }}
            </div>
        </div>
        <div class="algo">
            <div class="card-doc" v-for="c in doc" :key="c.uid">
                <img/>
                <div class="info">
                    <div class="top">
                        <div class="icon"><img :src="c.imgCat"></div>
                        <div class="bk1">
                            <div class="tittle">{{ c.tittle }}</div>
                            <div class="education">{{ c.arg1 }} {{ c.arg3 }} {{ c.arg2 }}</div>
                        </div>
                    </div>
                    <div class="bottom">
                        <div class="name">{{ c.fName }} {{ c.lName }} {{ c.tName }}</div>
                    </div>
                </div>
                <button class="btn" data-toggle="modal" data-target="#mdl-doc-card" @click="updCardModal(c.uid)">{{$t('doctorpage.details')}}</button>
            </div>
        </div>
       <input type="range" min="1" :max="(doc.length - 1) * 348" value="1" id="slider">
    </div>
</template>

<script>
import currencyFormat from '@/helpers/currencyFormat';
import timeFormat from "@/helpers/timeFormat";

export default {
  data() {
    return {
      select: this.$store.state.Booking.Procedure,
      category: [
        { uid: 1, img: '/img/teeth/Orthodontics.svg', tittle: 'Все', st: false},
        { uid: 2, img: '/img/teeth/Orthodontics.svg', tittle: 'Ортодонты', st: true},
        { uid: 3, img: '/img/teeth/Treatment.svg', tittle: 'Терапевты', st: true},
        { uid: 4, img: '/img/teeth/Surgery.svg', tittle: 'Хирурги', st: true},
        { uid: 5, img: '/img/teeth/Prosthetics.svg', tittle: 'Ортопеды', st: false},
        { uid: 6, img: '/img/teeth/Whitening.svg', tittle: 'Пародонтологи', st: false},
        ],
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
      fieldSize: null,
      loading: true,
      errored: false,
      results: null
    }
  },
  async created() {
    await this.docList('Орт', this.$store.state.Booking.Date, '');
    this.fieldSize = document.getElementsByClassName("algo")[0].clientWidth;
  },
  filters: {
    currencyFormat, timeFormat
  },
  methods: {
    updCardModal(uid){
      console.log(uid);
    },
    docList(cat, date, docUID) {
      const options = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({"txt": cat, "dt": date, "doctor_uid": docUID})
      };
      fetch(`http://localhost:8000/ru/vhapi/doctor/list/`, options).
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
    updCat(el){
      for(let i = 0; i<this.category.length; i++){
        if (this.category[i].uid === el){
          this.category[i].st = !this.category[i].st;
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
    margin: 56px auto 132px
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
@media (max-width: 727px)
  .doc
    > .algo
      margin: 32px auto auto
      > .card-doc
        display: block
        margin: auto auto 52px
</style>
