<template>
  <div class="modal fade" id="mdl-future-ok" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog modal-ctm modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <div>
            <h5 class="modal-title">{{ $t('modalfuture.info') }}</h5>
            <h6 class="sec-title">{{name}}</h6>
          </div>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div>
            {{ $t('modalfuture.soon') }}
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-ok" data-dismiss="modal">Ok</button>
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
            results: null,
        }
    },
    methods: {
        send(){
            /*alert(`POST: /feedback/message/${JSON.stringify({"name": this.name, "phone": this.phone, "mail": this.mail, "message": this.msg})}`);*/
            const options = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({"name": this.name, "phone": this.phone, "email": this.mail, "message": this.msg})
            };
            fetch(`${this.$store.state.apihost}ru/vhapi/feedback/msg/`, options).
            then(response => response.json()).
            then(data => {
            this.results = data;
            console.log(data);
            }).
            catch((error) => { console.log(error); this.results = null;}).
            finally(() => {
              this.loading = false;
              this.results = 200;
            });
        },
    },
}
</script>

<style lang="sass">
#mdl-future-ok
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
        box-shadow: 0px 4px 12px 0px rgba(218,172,84,0.08)
        &.form-ctm
          margin-bottom: 8px
          &.mail
            color: #42E1C5
            &::placeholder
              color: #42E1C5
          &.area
            height: 96px
          &:last-child
            margin-bottom: 0px
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