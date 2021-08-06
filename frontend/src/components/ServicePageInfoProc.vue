<template>
  <div>
    <div class="doctor-card">
      <div class="d-tittle">{{results.title}}</div>
      <div class="d-flex" style="overflow-y: auto;">
        <div v-for="c in doc.results" :key="c.uid">
          <div class="d-card">
            <img id="icd" :src="c.img">
            <div id="nmd">
              <div>{{ c.special }}</div>
              <div>{{ c.firstName }} {{ c.lastName }}</div>
            </div>
            <button class="btn" id="btn-d" data-toggle="modal" data-target="#mdl-doc-card" @click="updCardModal(c.uid)">
              <i class="fas fa-caret-right"></i></button>
          </div>
        </div>
      </div>
    </div>
    <div class="description">
      <div>{{ $t('servicepage.description') }}</div>
      <div>{{ results.description }}</div>
    </div>
    <div class="recomende">
      <div>{{ $t('servicepage.rec1') }}</div>
      <div><i class="profi"></i> {{ results.recomend_before}}</div>
      <!--<div><i class="profi"></i> Не кушать и не пить за 2 часа до процедуры</div>
      <div><i class="profi"></i> Принять антигистаминный препарат</div>
      <div><i class="profi"></i> Ограничить физическую активность за день до процедуры</div>
      <div><i class="profi"></i> Хорошо очистить полость рта</div>-->
    </div>
    <div class="recomende">
      <div>{{ $t('servicepage.rec2') }}</div>
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
  // name: 'Field',
  props: {
    info: String,
    resize: Boolean,
  },
  data(){
    return {
      selfProcUid: null,
      doc: {
        count: 0,
        results: [],
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
        if (this.selfProcUid) {
          this.getMoreInfo();
          this.getMedProcDoctors();
        }
      },
      immediate: true,
    },
    info: {
      handler(newLocale, oldLocale) {
        if (newLocale === oldLocale)
          return;
        if(newLocale !== null) {
          this.selfProcUid = newLocale;
          this.getMoreInfo();
          this.getMedProcDoctors();
        }
      },
      immediate: true,
    },
  },
  methods: {
    updCardModal(uid){
      this.$emit('showDocM', uid);
    },
    send() {
      this.$store.commit("updProc", this.prselect);
      this.$store.commit("updPrice", this.price);
    },
    docUID() {
      fetch(`${this.$store.state.apihost}${this.locale}/vhapi/doctor/`)
      .then(stream => stream.json())
      .then(response => {
        this.doc.count = 1;
        this.doc.results = [response];
      })
      .catch(error => { console.error(error); })
      .finally(()=>{
        if(this.doc.results[0].img === null)
          this.doc.results[0].img = `${this.$store.state.apihost}media/uploads/human/defaultAvatar.png`;
      });
    },
    getMedProcDoctors() {
      fetch(`${this.$store.state.apihost}${this.locale}/vhapi/medproc/${this.selfProcUid}/doctors/`).
      then(response => response.json()).
      then(data => {
        this.doc.count = data.count;
        if(this.doc.count > 0)
          this.doc.results = data.results;
        else
          this.docUID();
      }).
      catch((error) => { console.log(error); this.results = null;}).
      finally(() => {
        this.loading = false;
      });
    },
    getMoreInfo() {
      fetch(`${this.$store.state.apihost}${this.$i18n.locale}/vhapi/medproc/${this.selfProcUid}/`).
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
  border-radius: 0
  margin-bottom: 1.5rem
  background: #F3E9D4
.block-right
  border-radius: 0 1rem 1rem 0
  background: #F3E9D4
.block-right, .hm-block
  padding: 2rem
  text-align: left
  .doctor-card
    margin-bottom: 1.5rem
    .d-tittle
      font-family: Montserrat
      font-weight: 500
      font-size: 21px
      line-height: 26px
      text-align: left
      margin-bottom: 1.5rem
    .d-card
      background: white
      height: 72px
      width: 280px
      border-radius: .5rem
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
        border-radius: 0 .5rem .5rem 0
        background: $none
        color: $white
  .description
    margin-bottom: 1.5rem
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
      width: .5rem
      height: .5rem
      border-radius: 2px
    > div:first-child
      font-family: Montserrat
      font-size: 19px
      line-height: 24px
      color: #B8882F
      margin-bottom: 16px
    div
      font-family: FuturaBookC
      font-size: 1rem
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
      border-radius: .25rem
      overflow: hidden
      > div
        display: inline-block
        width: calc(100% - 32px)
      .btn-accord
        display: inline-block
        width: 16px
        height: 136px
        background: #42E1C5
        border-radius: .25rem
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
    height: 3rem
    background: $active-link-line
    border: none
    border-radius: 8px
    color: $white
@media (max-width: 1399px)
  .hm-block
    > .hid
      display: block
@media (max-width: 450px)
  .block-3
    > .block-left
     > .hm-block
        padding: 1rem
</style>
