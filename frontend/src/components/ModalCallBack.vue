<template>
<div class="modal fade" id="mdl-call-back" tabindex="-1" role="dialog" aria-hidden="true">
  <div class="modal-dialog modal-ctm modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <div>
          <h5 class="modal-title">Обратный звонок</h5>
          <h6 class="sec-title">Оставьте заявку и мы перезвоним в удобное для вас время</h6>
        </div>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <form action="" method="post">
          <input type="text" class="form-control form-ctm" placeholder="Ваше имя">
          <input type="text" class="form-control form-ctm" placeholder="Номер телефона">
          <h6>Удобное время для звонка</h6>
          <div class="sel-schedule">
            <div class="btn-chg-group">
              <button class="btn">
              <i class="fas fa-caret-up"></i>
              </button>
            <button class="btn">
              <i class="fas fa-caret-down"></i>
              </button>
            </div>
            <input type="text" class="form-vertical" value="11">
            <input type="text" class="form-vertical" value="35">
            <div class="btn-chg-group">
              <button class="btn">
                <i class="fas fa-caret-up"></i>
                </button>
              <button class="btn">
                <i class="fas fa-caret-down"></i>
              </button>
            </div>
          </div>
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
#mdl-call-back
  > .modal-ctm
    max-width: 360px
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
        width: 230px
        font-family: FuturaBookC
        line-height: 21px
    > .close
      position: absolute
      right: 1rem
      top: 1rem
      color: #DFB971

  .modal-body
    margin: 0.5rem 0px
    padding: 0.5rem 2rem
    form
      input
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
          &:last-child
            margin-bottom: 24px
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
            width: 40px
            height: 64px
            border-radius: .5rem
            margin: 0px 4px
            font-family: FuturaBookC
            font-size: 16px
            line-height: 21px
            color: #071013
            text-align: center

  .modal-footer
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