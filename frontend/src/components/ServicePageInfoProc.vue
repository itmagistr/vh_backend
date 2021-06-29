<template>
  <div>
    <div class="doctor-card">
      <div class="d-tittle">{{results.title}} {{ doc.results.firstName }} {{ doc.results.lastName }}</div>
      <div class="d-card">
        <img id="icd" :src="doc.results.img">
        <div id="nmd">
          <div>{{ doc.results.special }}</div>
          <div>{{ doc.results.firstName }} {{ doc.results.lastName }}</div>
        </div>
        <button class="btn" id="btn-d"><i class="fas fa-caret-right"></i></button>
      </div>
    </div>
    <div class="description">
      <div>{{ $t('servicepage.description') }}</div>
      <div>{{ results.description }}</div>
    </div>
    <div class="recomende">
      <div>Рекомендации перед процедурой</div>
      <div>{{ results.recomend_before}}</div>
      <!--<div><i class="profi"></i> Не кушать и не пить за 2 часа до процедуры</div>
      <div><i class="profi"></i> Принять антигистаминный препарат</div>
      <div><i class="profi"></i> Ограничить физическую активность за день до процедуры</div>
      <div><i class="profi"></i> Хорошо очистить полость рта</div>-->
    </div>
    <div class="recomende">
      <div>Рекомендации после процедуры</div>
      <div><i class="profi"></i> {{ results.recomend_after}}</div>
      <!--<div><i class="profi"></i> Не кушать и не пить 3 часа после процедуры</div>
      <div><i class="profi"></i> Очистка полости рта ирригатором</div>
      <div><i class="profi"></i> Ограничить физическую активность на 3 дня после процедуры</div>-->
    </div>
    <!--<div class="photo">
      <div>{{ $t('servicepage.photo') }}</div>
      <div class="accordion">
        <button class="btn btn-accord"><i class="fas fa-caret-left"></i></button>
        <div></div>
        <button class="btn btn-accord"><i class="fas fa-caret-right"></i></button>
      </div>
    </div>-->
    <!--<button class="btn hid" @click="send()">{{ $t('proсchoice.select') }}</button>-->
  </div>
</template>

<script>
export default {
  props: {
    info: String,
    resize: Boolean,
  },
  data(){
    return {
      self: '',
      doc: {
        count: 0,
        results: {},
      },
      results: {
        title: '',
        description: '',
      },
      locale: this.$i18n.locale,
    }
  },
  created() {
    if(this.doc.count === 0)
      this.docUID();
  },
  watch: {
    "$i18n.locale": {
      handler(newLocale, oldLocale) {
        if (newLocale === oldLocale)
          return;
        this.locale = newLocale;
      },
      immediate: true,
    },
    info: {
      handler(newLocale, oldLocale) {
        if (newLocale === oldLocale)
          return;
        if(newLocale !== null) {
          this.self = newLocale;
          this.getMoreInfo(this.self);
          this.getMedProcDoctors(this.self);
        }
      },
      immediate: true,
    },
  },
  methods: {
    send() {
      this.$store.commit("updProc", this.prselect);
      this.$store.commit("updPrice", this.price);
    },
    docUID(){
      fetch(`http://localhost:8000/${this.locale}/vhapi/doctor/`)
      .then(stream => stream.json())
      .then(response => {
        this.doc.count = 1;
        this.doc.results = response;
      })
      .catch(error => { console.error(error); });
    },
    getMedProcDoctors(procUID) {
      fetch(`http://localhost:8000/${this.locale}/vhapi/medproc/${procUID}/doctors/`).
      then(response => response.json()).
      then(data => {
        this.doc.count = data.count;
        if(this.doc.count > 0)
          this.doc.results = data.results[0];
        else
          this.docUID();
      }).
      catch((error) => { console.log(error); this.results = null;}).
      finally(() => {
        this.loading = false;
      });
    },
    getMoreInfo(procUID) {
      fetch(`http://localhost:8000/${this.$i18n.locale}/vhapi/medproc/${procUID}/`).
      then(response => response.json()).
      then(data => {
        this.results = data;
      }).
      catch((error) => { console.log(error); this.results = null;}).
      finally(() => {
        this.loading = false;
      });
    },
  },
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.hm-block
  width: 100%
  border-radius: 0px
  margin-bottom: 24px
  background: #F3E9D4
.block-right
  border-radius: 0px 16px 16px 0px
  background: #F3E9D4
.block-right, .hm-block
  padding: 32px
  text-align: left
  .doctor-card
    margin-bottom: 24px
    .d-tittle
      font-family: Montserrat
      font-weight: 500
      font-size: 21px
      line-height: 26px
      text-align: left
      margin-bottom: 24px
    .d-card
      background: white
      height: 72px
      width: 280px
      border-radius: 8px
      > div, > button
        display: inline-block
      img#icd
        position: relative
        top: 8px
        left: 8px
        width: 56px
        height: 56px
        background: $backgroundImage
        border-radius: .25rem
        vertical-align: initial
      #nmd
        font-family: FuturaBookC
        position: relative
        top: -8px
        left: 24px
        width: 177px
        line-height: 1
        text-align: left
      #nmd > div:first-child
        color: $button-color
        font-size: 14px
      #nmd > div:last-child
        font-size: 16px
      #btn-d
        position: relative
        top: -17px
        right: -21px
        width: 26px
        height: 72px
        border: none
        border-radius: 0px 8px 8px 0px
        background: $none
        color: $white
  .description
    margin-bottom: 24px
    > div:first-child
      font-family: Montserrat
      font-size: 19px
      line-height: 24px
      color: #B8882F
      margin-bottom: 16px
    > div:last-child
      font-family: FuturaBookC
      font-size: 16px
      line-height: 21px
  .recomende
    margin-bottom: 20px
    i
      display: inline-block
      width: 8px
      height: 8px
      border-radius: 2px
    > div:first-child
      font-family: Montserrat
      font-size: 19px
      line-height: 24px
      color: #B8882F
      margin-bottom: 16px
    div
      font-family: FuturaBookC
      font-size: 16px
      line-height: 21px
      margin-bottom: 8px
  .photo
    > div:first-child
      font-family: Montserrat
      font-size: 19px
      line-height: 24px
      color: #B8882F
      margin-bottom: 16px
    .accordion
      height: 136px
      width: 100%
      background:  #F1EEE6
      border-radius: 4px
      overflow: hidden
      > div
        display: inline-block
        width: calc(100% - 32px)
      .btn-accord
        display: inline-block
        width: 16px
        height: 136px
        background: #42E1C5
        border-radius: 4px
        border: none
        color: $white
        &:hover
          background: #EED199
          box-shadow: none
.block-right, .hm-block
  > .hid
    display: none
    margin: 40px auto 1rem
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
  .hm-block
    > .hid
      display: block
</style>
