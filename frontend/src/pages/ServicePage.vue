<template>
    <div class="d-flex flex-column mar">
        <div class="bgz-main"></div>
        <div class="tittle-of-service">{{ $t('servicepage.service') }}</div>
        <div class="service">
            <div class="card-tooth active"><img src="/img/teeth/Orthodontics.svg"/><div>{{ $t('servicepage.card1') }}</div></div>
            <div class="card-tooth"><img src="/img/teeth/Surgery.svg"/><div>{{ $t('servicepage.card2') }}</div></div>
            <div class="card-tooth"><img src="/img/teeth/Treatment.svg"/><div>{{ $t('servicepage.card3') }}</div></div>
            <div class="card-tooth"><img src="/img/teeth/Whitening.svg"/><div>{{ $t('servicepage.card4') }}</div></div>
            <div class="card-tooth"><img src="/img/teeth/Prosthetics.svg"/><div>{{ $t('servicepage.card5') }}</div></div>
            <div class="card-tooth"><img src="/img/teeth/Implantation.svg"/><div>{{ $t('servicepage.card6') }}</div></div>
        </div>
        <div class="block-2">
            <div class="block-top">
                <div class="tittle">
                    {{ $t('servicepage.title') }}
                </div>
                <div class="text">
                    {{ $t('servicepage.text') }}
                </div>
            </div>
            <div class="accordion">

            </div>
        </div>
        <div class="block-3">
            <div class="block-left">
                <div>{{ $t('servicepage.price') }}</div>
                <table class="table table-borderless">
                    <tbody>
                        <template v-for="c in results">
                            <tr class="product" :class="[{spec: c.code.length > 5}, { active: c.uid === prselect}]" :key="c.uid" @click="selected(c.uid)">
                                <td class="pr-code">{{ c.code }}</td>
                                <td class="pr-tittle">{{ c.title }}</td>
                                <td class="pr-price">{{ c.price | currencyFormat("RUB")}}</td>
                                <td class="pr-duration">{{ c.duration | timeFormat("ru-RU")}}</td>
                            </tr>
                            <tr v-if="prselect === c.uid" :key="'block-'+c.uid">
                                <div class="hm-block">
                                    <div class="doctor-card">
                                        <div class="d-tittle">Очень длинное название процедуры, очень длинное врач Василенко Л.И.</div>
                                        <div class="d-card">
                                            <div id="icd"> </div>
                                            <div id="nmd">
                                              <div>Врач</div>
                                              <div>Василенко Л.И.</div>
                                            </div>
                                            <button class="btn" id="btn-d"><i class="fas fa-caret-right"></i></button>
                                        </div>
                                    </div>
                                    <div class="description">
                                        <div>Описание процедуры</div>
                                        <div>
                                            Идейные соображения высшего порядка, а также начало повседневной работы по формированию позиции
                                            обеспечивает широкому кругу (специалистов) участие в формировании модели развития. С другой
                                            стороны начало повседневной работы по формированию позиции влечет за собой процесс внедрения.
                                        </div>
                                    </div>
                                    <div class="recomende">
                                        <div>Рекомендации перед процедурой</div>
                                        <div><i class="profi"></i> Не кушать и не пить за 2 часа до процедуры</div>
                                        <div><i class="profi"></i> Принять антигистаминный препарат</div>
                                        <div><i class="profi"></i> Ограничить физическую активность за день до процедуры</div>
                                        <div><i class="profi"></i> Хорошо очистить полость рта</div>
                                    </div>
                                    <div class="recomende">
                                        <div>Рекомендации после процедуры</div>
                                        <div><i class="profi"></i> Не кушать и не пить 3 часа после процедуры</div>
                                        <div><i class="profi"></i> Очистка полости рта ирригатором</div>
                                        <div><i class="profi"></i> Ограничить физическую активность на 3 дня после процедуры</div>
                                    </div>
                                    <div class="photo">
                                        <div>Фото</div>
                                        <div class="accordion">
                                            <button class="btn btn-accord"><i class="fas fa-caret-left"></i></button>
                                            <div></div>
                                            <button class="btn btn-accord"><i class="fas fa-caret-right"></i></button>
                                        </div>
                                    </div>
                                </div>
                            </tr>
                        </template>
                    </tbody>
                </table>
            </div>
            <div class="block-right">
                <div class="doctor-card">
                    <div class="d-tittle">Очень длинное название процедуры, очень длинное врач Василенко Л.И.</div>
                    <div class="d-card">
                        <div id="icd"> </div>
                        <div id="nmd">
                          <div>Врач</div>
                          <div>Василенко Л.И.</div>
                        </div>
                        <button class="btn" id="btn-d"><i class="fas fa-caret-right"></i></button>
                    </div>
                </div>
                <div class="description">
                    <div>Описание процедуры</div>
                    <div>
                        Идейные соображения высшего порядка, а также начало повседневной работы по формированию позиции
                        обеспечивает широкому кругу (специалистов) участие в формировании модели развития. С другой
                        стороны начало повседневной работы по формированию позиции влечет за собой процесс внедрения.
                    </div>
                </div>
                <div class="recomende">
                    <div>Рекомендации перед процедурой</div>
                    <div><i class="profi"></i> Не кушать и не пить за 2 часа до процедуры</div>
                    <div><i class="profi"></i> Принять антигистаминный препарат</div>
                    <div><i class="profi"></i> Ограничить физическую активность за день до процедуры</div>
                    <div><i class="profi"></i> Хорошо очистить полость рта</div>
                </div>
                <div class="recomende">
                    <div>Рекомендации после процедуры</div>
                    <div><i class="profi"></i> Не кушать и не пить 3 часа после процедуры</div>
                    <div><i class="profi"></i> Очистка полости рта ирригатором</div>
                    <div><i class="profi"></i> Ограничить физическую активность на 3 дня после процедуры</div>
                </div>
                <div class="photo">
                    <div>Фото</div>
                    <div class="accordion">
                        <button class="btn btn-accord"><i class="fas fa-caret-left"></i></button>
                        <div></div>
                        <button class="btn btn-accord"><i class="fas fa-caret-right"></i></button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import currencyFormat from '@/helpers/currencyFormat';
import timeFormat from "@/helpers/timeFormat";

export default {
    props: ['resize'],
    data() {
        return {
            select: this.$store.state.Booking.Procedure,
            prselect: null,
            loading: true,
            errored: false,
            results: null,
            locale: this.$i18n.locale
        }
    },
    async created() {
        //await this.getMedProc("Орто", "2021-03-21", "bf0f0856-f57d-48c6-b99c-b3c8a2e3ea82");
        await this.getMedProc('', "2021-03-21", null);
    },
    mounted() {
      this.$watch( "$i18n.locale",
        (newLocale, oldLocale) => {
          if (newLocale === oldLocale) {
            return
          }
          this.locale = newLocale;
          this.getMedProc('', "2021-03-21", null);
        },
        { immediate: true }
      )
    },
    methods: {
        getMedProc(cat, date, docUID) {
            var docdict = {}
            if (docUID)
              docdict = { "txt": cat, "dt": date, "doctor_uid": docUID };
            else
              docdict = { "txt": cat, "dt": date };

            const options = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(docdict)
            };
            fetch(`http://localhost:8000/${this.locale}/vhapi/medproc/list/`, options).
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
        selected(sel){
          if(this.resize)
            if(this.prselect === sel)
              this.prselect = null;
            else
              this.prselect = sel;
        },
    },
    filters: {
        currencyFormat, timeFormat
    },
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"
body.chg-proc
  backdrop-filter: blur(16px)
  > main
    background-color: rgba(254, 253, 251, 0.64)
    > .container
      padding-top: 27px
    > div
      > .modal
        height: 100vh
  > header
    backdrop-filter: none

.bgz-main
  background: #F6F3ED
  position: absolute
  z-index: -1
  width: 100%
  height: calc(100% - 378px)
  left: 0px
  top: 378px

.mar
    width: 100%
    > div.service
        overflow: auto
        width: 100%
        text-align: center
        display: -webkit-box
    .tittle-of-service
        text-align: center
        font-family: FuturaBookC
        font-size: 64px
        line-height: 61px
        color: $button-color
        margin-bottom: 56px

.card-tooth
  vertical-align: middle
  width: 200px
  height: 200px
  padding: 40px 0
  background: #F3E9D4
  border-radius: 8px
  margin: 0px 16px
  &:first-child
      margin-left: 1px
  &:last-child
    margin-right: 1px
  &.active
    background: $active-link-line
  &.active > div
    color: $white
  > img
    margin-bottom: 36px
  > div
    font-family: FuturaBookC
    font-style: normal
    font-weight: normal
    font-size: 16px
    line-height: 21px
    text-align: center
    letter-spacing: 0.08em
    text-transform: uppercase
    color: $button-color

.block-2
  margin-top: 64px
  text-align: center
  display: block!important
  .tittle
    font-family: FuturaBookC
    font-size: 48px
    line-height: 56px
    color: $button-color
  .text
    font-family: FuturaBookC
    font-size: 16px
    line-height: 21px
  .accordion
    margin-top: 38px
    margin-left: auto
    margin-right: auto
    width: calc(100% - 64px)
    height: 236px
    background: #00C0BB55
    border-radius: 16px

.block-3
  margin: 64px auto 128px
  display: flex
  .btn
    padding: 0px
  > .block-left, > .block-right
    height: 867px
    width: 681px

.block-left
  border-radius: 16px 0px 0px 16px
  background: $white
  padding: 32px
  position: relative
  text-align: left
  > div:first-child
    font-family: Montserrat
    font-weight: 500
    font-size: 21px
    line-height: 26px
    margin-bottom: 32px
  .product
    > td
      display: inline-table
      margin: 0px 8px
    > td:first-child
      margin: 0px 0px 8px
    > td:last-child
      margin-right: 0px
    > td
      margin-bottom: 8px
    &.active, &:hover
      background: rgba(238, 209, 153, 0.16)
    &.active > .pr-info > i, &:hover > .pr-info > i
      display: inline-table
    &.active > .pr-price, &:hover > .pr-price
      color: #B8882F
    &.active > .pr-duration, &:hover > .pr-duration
      color: #071013
    .pr-code
      width: 48px
      font-family: Montserrat
      font-size: 19px
      line-height: 24px
      color: #071013
    &.spec > .pr-code
      width: 120px
      font-size: 16px
      line-height: 21px
    .pr-tittle
      width: 376px
      font-family: FuturaBookC
      line-height: 16px
      color: #071013
    &.spec > .pr-tittle
      width: 300px
    .pr-price
      width: 72px
      font-family: FuturaBookC
      line-height: 21px
      text-align: right
      color: #DFB971
    .pr-duration
      width: 56px
      font-family: FuturaBookC
      line-height: 21px
      text-align: right
      color: #9CC6BE

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
      #icd
        position: relative
        top: 8px
        left: 8px
        width: 56px
        height: 56px
        background: $active-link-line
        border-radius: 4px
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
        top: -16px
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

@media (max-width: 1399px)
  .container
    >.d-flex
      >.d-flex
        &:first-child, &:last-child
          display: none!important
  .bgz-main
    height: calc(100% - 308px)
    top: 308px
  .mar
    .tittle-of-service
      text-align: center
  .block-3
    margin: 64px -16px 48px
    display: inline-grid!important
    .block-left
      padding: 32px 0px
      width: 100%
      height: 100%
      border-radius: 16px
      > div
        padding-left: 32px
      td.pr-code
        margin-left: 32px
    .block-right
      display: none
      width: 100%
      height: 100%
      border-radius: 0px

</style>
