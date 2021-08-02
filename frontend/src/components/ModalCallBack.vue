<template>
<div class="modal fade" id="mdl-call-back" tabindex="-1" role="dialog" aria-hidden="true">
  <div class="modal-dialog modal-ctm modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <div v-if="success">
          <h5 class="modal-title">Ваша заявка отправлена</h5>
          <h6 class="sec-title">Спасибо за обращене, мы ответим вам в ближайшее время</h6>
        </div>
        <div v-else >
          <h5 class="modal-title">{{ $t('callback.call') }}</h5>
          <h6 class="sec-title">{{ $t('callback.text') }}</h6>
        </div>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <div v-if="success" class="checkmark-circle">
          <svg class="sucess" viewBox="0 0 130.2 130.2">
            <polyline class="path check" fill="none" stroke="#42E1C5" stroke-width="20" stroke-miterlimit="10" points="100.2,40.2 51.5,88.8 29.8,67.5 "/>
          </svg>
<!--      <div class="checkmark draw"></div>-->
        </div>
        <div v-else class="form">
          <input type="text" class="form-control form-ctm"
                 v-model="name" :placeholder="$t('callback.yourname')">
          <input type="phone" class="form-control form-ctm"
                 v-model="phone" :placeholder="$t('callback.phonenumber')">
          <h6>{{ $t('callback.time') }}</h6>
          <div class="sel-schedule">
            <div class="btn-chg-group">
              <button class="btn" @click="hrMinFun('hrIncr')">
              <i class="fas fa-caret-up"></i>
              </button>
            <button class="btn" @click="hrMinFun('hrDecr')">
              <i class="fas fa-caret-down"></i>
              </button>
            </div>
            <select class="form-vertical" v-model="hr">
              <option value="6">06</option>
              <option value="7">07</option>
              <option value="8">08</option>
              <option value="9">09</option>
              <option value="10">10</option>
              <option value="11">11</option>
              <option value="12">12</option>
              <option value="13">13</option>
              <option value="14">14</option>
              <option value="15">15</option>
              <option value="16">16</option>
              <option value="17">17</option>
              <option value="18">18</option>
              <option value="19">19</option>
              <option value="20">20</option>
              <option value="21">21</option>
              <option value="22">22</option>
            </select>
            
            <select class="form-vertical" v-model="min">
              <option value="0">00</option>
              <option value="5">05</option>
              <option value="10">10</option>
              <option value="15">15</option>
              <option value="20">20</option>
              <option value="25">25</option>
              <option value="30">30</option>
              <option value="35">35</option>
              <option value="40">40</option>
              <option value="45">45</option>
              <option value="50">50</option>
              <option value="55">55</option>
            </select>
            <div class="btn-chg-group">
              <button class="btn" @click="hrMinFun('minIncr')">
                <i class="fas fa-caret-up"></i>
                </button>
              <button class="btn" @click="hrMinFun('minDecr')">
                <i class="fas fa-caret-down"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
      <div v-if="!success" class="modal-footer">
        <div>{{ $t('callback.confident') }}</div>
        <button type="button" class="btn btn-ok" @click="send()">
          {{ $t('callback.send-btn') }}
        </button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default{
  data(){
    return {
      name: null,
      phone: null,
      hr: null,
      min: null,
      results: null,
      success: false,
    }
  },
  created() {
    this.hr = new Date().getHours();
    if(this.hr >= 23 || this.hr < 6)
      this.hr = 6;
    this.min = new Date().getMinutes() - new Date().getMinutes() % 5;
  },
  mounted() {
    document.getElementById("mdl-call-back").addEventListener("click", this.close);
  },
  methods: {
    truncate(str, len) {
      return (str.length > len) ? str.substr(0, len) : str;
    },
    close(){
      this.success = false;
    },
    async send() {
      await this.$recaptchaLoaded();
      const token = await this.$recaptcha('feedbackCall');
      if(this.name !== null && this.phone !== null && this.phone.length >= 10 && this.hr !== null && this.min !== null) {
        const options = {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({
            "name": this.name,
            "phone": this.phone,
            "hr": this.hr,
            "min": this.min,
            'recap': this.truncate(token, 1024)
          })
        };
        fetch(`${this.$store.state.apihost}ru/vhapi/feedback/call/`, options).then(response => response.json()).then(data => {
          this.results = data;
          console.log(data);
        }).catch((error) => {
          console.log(error);
          this.results = null;
        }).finally(() => {
          this.loading = false;
          this.success = true;
        });
      }
    },
    hrMinFun(str){
      switch(str){
        case 'hrIncr': this.hr = (this.hr + 1 <= 22) ? this.hr + 1 : this.hr; break;
        case 'hrDecr': this.hr = (this.hr - 1 >= 6) ? this.hr - 1 : this.hr; break;
        case 'minIncr': this.min = (this.min + 5 <= 55) ? this.min + 5 : this.min; break;
        case 'minDecr': this.min = (this.min - 5 >= 0) ? this.min - 5 : this.min; break;
        default: break;
      }
    },
  },
}
</script>

<style lang="sass">
#mdl-call-back
  > .modal-ctm
    max-width: 360px
    > .modal-content
      text-align: center
      background: #FEFDFB
      border-radius: 0.5rem
      > .modal-header, > .modal-footer
        border: none
      > .modal-header
        padding-top: 32px
        padding-bottom: 8px
        > div
          margin: auto
          > .modal-title
            margin-top: 8px
            margin-bottom: 12px
            font-family: Montserrat
            font-weight: 500
            font-size: 21px
            line-height: 26px
          > .sec-title
            margin: auto
            width: 230px
            font-family: FuturaBookC
            line-height: 21px
        > .close
          position: absolute
          right: 1rem
          top: 1rem
          color: #DFB971
          &:hover
            color: #9CC6BE
      > .modal-body
        margin: 0.5rem 0px
        padding: 0.5rem 2rem
        div.form
          input, select
            font-family: FuturaBookC
            font-size: 1rem
            line-height: 1.25rem
            color: #EED199
            background: #FEFDFB
            height: 3rem
            border-radius: 0.5rem
            border: none
            box-shadow: 0px 4px 12px 0px rgba(218,172,84,0.08)
            &.form-ctm
              &:first-child
                margin-bottom: 8px
            &::placeholder
              font-family: FuturaBookC
              font-size: 1rem
              line-height: 1.25rem
              color: #EED199
          h6
            font-family: FuturaBookC
            font-style: normal
            font-weight: normal
            line-height: 21px
            margin-top: 1.5rem
            margin-bottom: 1rem
          .btn-chg-group
            vertical-align: middle
            display: inline-grid
            > .btn
              padding: 0px
              width: 2rem
              height: 2rem
              background: transparent
              color: #DFB971
          .sel-schedule
            > .form-vertical
              vertical-align: middle
              width: 40px
              height: 64px
              border-radius: .5rem
              margin: 0px 4px
              padding: 11px
              font-family: FuturaBookC
              font-size: 16px
              line-height: 21px
              color: #071013
              text-align: center
              appearance: none
      > .modal-footer
        padding: 0.5rem
        height: 124px
        > div
          width: 262px
          margin: auto
          font-family: FuturaBookC
          font-size: 14px
          line-height: 16px
          color: #9CC6BE
        > .btn-ok
          position: absolute
          bottom: -25px
          left: 27%
          width: 156px
          height: 48px
          border-radius: 0.5rem
          background: #42E1C5
          color: white
          font-family: FuturaBookC
          font-size: 1rem
          line-height: 1.25rem
          letter-spacing: 0.08em
          text-transform: uppercase
          color: #FEFDFB
</style>

<style>
.checkmark-circle {
  width: 160px;
  height: 160px;
  position: relative;
  display: inline-block;
  vertical-align: top;
}
.checkmark-circle .checkmark {
  border-radius: 5px;
}
.checkmark-circle .checkmark.draw:after {
  -webkit-animation-delay: 100ms;
  -moz-animation-delay: 100ms;
  animation-delay: 100ms;
  -webkit-animation-duration: 2s;
  -moz-animation-duration: 2s;
  animation-duration: 2s;
  -webkit-animation-timing-function: ease;
  -moz-animation-timing-function: ease;
  animation-timing-function: ease;
  -webkit-animation-name: checkmark;
  -moz-animation-name: checkmark;
  animation-name: checkmark;
  -webkit-transform: scaleX(-1) rotate(135deg);
  -moz-transform: scaleX(-1) rotate(135deg);
  -ms-transform: scaleX(-1) rotate(135deg);
  -o-transform: scaleX(-1) rotate(135deg);
  transform: scaleX(-1) rotate(135deg);
  -webkit-animation-fill-mode: forwards;
  -moz-animation-fill-mode: forwards;
  animation-fill-mode: forwards;
}
.checkmark-circle .checkmark:after {
  opacity: 1;
  height: 80px;
  width: 40px;
  -webkit-transform-origin: left top;
  -moz-transform-origin: left top;
  -ms-transform-origin: left top;
  -o-transform-origin: left top;
  transform-origin: left top;
  border-right: 20px solid #42E1C5;
  border-top: 20px solid #42E1C5;
  border-radius: 2.5px !important;
  content: "";
  left: 26.6666666667px;
  top: 80px;
  position: absolute;
}

@-webkit-keyframes checkmark {
  0% { height: 0; width: 0; opacity: 1; }
  20% { height: 0; width: 40px; opacity: 1; }
  40% { height: 80px; width: 40px; opacity: 1; }
  100% { height: 80px; width: 40px; opacity: 1; }
}
@-moz-keyframes checkmark {
  0% { height: 0; width: 0; opacity: 1; }
  20% { height: 0; width: 40px; opacity: 1; }
  40% { height: 80px; width: 40px; opacity: 1; }
  100% { height: 80px; width: 40px; opacity: 1; }
}
@keyframes checkmark {
  0% { height: 0; width: 0; opacity: 1; }
  20% { height: 0; width: 40px; opacity: 1; }
  40% { height: 80px; width: 40px; opacity: 1; }
  100% { height: 80px; width: 40px; opacity: 1; }
}
</style>
