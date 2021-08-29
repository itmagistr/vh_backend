<template>
<div class="modal fade" id="mdl-leave-request" tabindex="-1" role="dialog" aria-hidden="true">
  <div class="modal-dialog modal-ctm modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <div v-if="success">
          <h5 class="modal-title">Ваша заявка отправлена</h5>
          <h6 class="sec-title">Спасибо за обращене, мы ответим вам в ближайшее время</h6>
        </div>
        <div v-else>
          <h5 class="modal-title">{{ $t('leaverequest.app') }}</h5>
          <h6 class="sec-title">{{ $t('leaverequest.text') }}</h6>
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
          <input type="text" class="form-control" :class="{error: errorField.name}"
                 v-model="name" @keyup="checkForm('name')" :placeholder="$t('leaverequest.yourname')">
          <input type="tel" class="form-control" :class="{error: errorField.phone}"
                 v-model="phone" @keyup="checkForm('phone')" :placeholder="$t('leaverequest.phonenumber')">
          <input type="email" class="form-control mail" :class="{error: errorField.mail}"
                 v-model="mail" @keyup="checkForm('mail')" placeholder="Myname@yandex.ru" >
          <textarea class="form-control area" :class="{error: errorField.msg}"
                    v-model="msg" @keyup="checkForm('msg')" :placeholder="$t('leaverequest.yourmsg')"></textarea>
        </div>
      </div>
      <div v-if="!success" class="modal-footer">
         <div>{{ $t('leaverequest.confident') }}</div>
        <button type="button" class="btn btn-ok" @click="send()">{{ $t('leaverequest.send-btn') }}</button>
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
      mail: null,
      msg: null,
      errorField: {
        name: false,
        phone: false,
        mail: false,
        msg: false,
      },
      results: null,
      success: false,
    }
  },
  mounted() {
    document.getElementById("mdl-leave-request").addEventListener("click", this.close);
  },
  computed: {
    compCheckForm() {
      if (this.name === null)
        return false;
      else
        return true;
    }
  },
  methods: {
    checkForm(br) {
      switch (br) {
        case 'name':
          this.errorField.name = this.name === null || this.name === '';
          break;
        case 'phone':
          this.errorField.phone = this.phone === null || this.phone === '' || this.phone.length < 10;
          break;
        case 'mail':
          this.errorField.mail = this.mail === null || this.mail === '';
          break;
        case 'msg':
          this.errorField.msg = this.msg === null || this.msg === '';
          break;
        case 'all':
          this.errorField.name = this.name === null || this.name === '';
          this.errorField.phone = this.phone === null || this.phone === '' || this.phone.length < 10;
          this.errorField.mail = this.mail === null || this.mail === '';
          this.errorField.msg = this.msg === null || this.msg === '';
          break;
        default: console.log(br); break;
      }
    },
    truncate(str, len) {
      return (str.length > len) ? str.substr(0, len) : str;
    },
    close(){
      this.success = false;
    },
    async send() {
      await this.$recaptchaLoaded();
      const token = await this.$recaptcha('feedbackMsg');

      if(this.name !== null && this.phone !== null && this.mail !== null && this.msg !== null &&
          this.name !== '' && this.phone !== '' && this.mail !== '' && this.msg !== '' && this.phone.length >= 10) {
        const options = {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({
            "name": this.name,
            "phone": this.phone,
            "email": this.mail,
            "message": this.msg,
            'recap': this.truncate(token, 1024)
          })
        };
        fetch(`${this.$store.state.apihost}ru/vhapi/feedback/msg/`, options)
        .then(response => response.json()).then(data => {
          this.results = data;
          console.log(data);
        }).catch((error) => {
          console.log(error);
          this.results = null;
        }).finally(() => {
          this.loading = false;
          console.log(this.results);
          this.success = true;
        });
      } else {
        this.checkForm('all');
      }
    },
  },
}
</script>

<style lang="sass">
#mdl-leave-request
  > .modal-ctm
    max-width: 400px
    > .modal-content
      text-align: center
      background: #FEFDFB
      border-radius: 0.5rem
  .modal-header, .modal-footer
    border: none
  .modal-header
    padding-top: 32px
    padding-bottom: 8px
    > div
      margin: auto
      text-align: center
      > .modal-title
        margin-top: 8px
        margin-bottom: 12px
        font-family: Montserrat
        font-weight: 500
        font-size: 21px
        line-height: 26px
      > .sec-title
        font-family: FuturaBookC
        line-height: 21px
    > .close
      position: absolute
      right: 1rem
      top: 1rem
      color: #DFB971
      &:hover
        color: #9CC6BE

  .modal-body
    margin: 0px
    padding: 0.5rem 2rem
    div.form
      input, textarea
        font-family: FuturaBookC
        font-size: 1rem
        line-height: 1.25rem
        color: #EED199
        background: #FEFDFB
        height: 3rem
        border-radius: 0.5rem
        border: none
        box-shadow: 0 4px 12px 0 rgba(218,172,84,0.08)
        margin-bottom: 8px
        &.mail
          color: #42E1C5
          &::placeholder
            color: #42E1C5
        &.area
          height: 96px
          margin-bottom: 0
        &.error
          box-shadow: 0 0 12px 0 #FF00007F
          color: #FF0000
          &::placeholder
            color: #FF0000
        &::placeholder
          font-family: FuturaBookC
          font-size: 1rem
          line-height: 1.25rem
          color: #EED199

  .modal-footer
    padding: 0px
    height: 101px
    > div
      width: 262px
      margin: auto
      margin-bottom: 45px
      font-family: FuturaBookC
      font-size: 14px
      line-height: 16px
      color: #9CC6BE
    > .btn-ok
      position: absolute
      bottom: -25px
      left: 30%
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
// .modal-backdrop
//   background-color: #fefdfb

</style>