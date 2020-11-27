<template>
<div class="modal fade" id="mdl-leave-request" tabindex="-1" role="dialog" aria-hidden="true">
  <div class="modal-dialog modal-ctm modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <div>
          <h5 class="modal-title">Оставьте заявку</h5>
          <h6 class="sec-title">Задайте вопрос и мы ответим вам в течении суток</h6>
        </div>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form action="" method="post">
          <input type="text" class="form-control form-ctm" placeholder="Ваше имя">
          <input type="text" class="form-control form-ctm" placeholder="Номер телефона">
          <input type="text" class="form-control form-ctm mail" placeholder="Myname@yandex.ru">
          <textarea class="form-control form-ctm area" placeholder="Ваше сообщение"></textarea>
        </form>
      </div>
      <div class="modal-footer">
         <div>Нажимая кнопку, вы соглашаетесь с условиями Политики конфиденциальности</div>
        <button type="button" class="btn btn-ok">Отправить</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
    export default{

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

  .modal-body
    margin: 0px
    padding: 0.5rem 2rem
    form
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