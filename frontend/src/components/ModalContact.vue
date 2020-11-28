<template>
    <div class="modal fade" id="mdl-contacts" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog modal-ctm modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Контакты</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div class="gp-mc-contact">
              <div class="mc-contact">
                <div>Адрес</div>
                <div>г. Москва, ул. Улица, д. 145</div>
              </div>
              <div class="mc-contact">
                <div>Телефон</div>
                <div>+7 (495) 123-45-67</div>
              </div>
              <div class="mc-contact">
                <div>E-mail</div>
                <div>Tohollywood@gmail.com</div>
              </div>
            </div>
            <div class="social-directions">
              <div class="icon"><i class="fab fa-instagram"></i></div>
              <div class="icon"><i class="fab fa-youtube"></i></div>
              <div class="icon"><i class="fab fa-facebook-f"></i></div>
              <div class="icon"><i class="fab fa-vk"></i></div>
              <div class="input-group">
                <input type="text" class="form-control form-control-lg" placeholder="Показать проезд от адреса" aria-describedby="button-addon4">
                <div class="input-group-append" id="button-addon4">
                  <button class="btn" type="button"><span class="material-icons">
    directions_bus
    </span></button>
                  <button class="btn" type="button"><span class="material-icons">
    directions_car
    </span></button>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <iframe src="https://api-maps.yandex.ru/frame/v1/-/CVh7YBYg?lang=en_RU" frameborder="0"></iframe>
            <button type="button" class="btn btn-ok">Обратная связь</button>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            results: null
        }
    }
}
</script>

<style lang="sass">
#mdl-contacts
  > .modal-ctm
    max-width: 688px
    > .modal-content
      background: #FEFDFB
      border-radius: 0.5rem
  .modal-header, .modal-footer
    border: none
  .modal-header
    padding-bottom: 8px
    > .modal-title
      margin: auto
      margin-top: 8px
      font-family: Montserrat
      font-weight: 500
      font-size: 21px
      line-height: 26px
    > .close
      position: absolute
      right: 16px
      top: 16px
      color: #DFB971
      &:hover
        color: #9CC6BE
  .modal-body
    margin: 0.5rem 0px
    padding: 0.5rem
    > .gp-mc-contact
      display: flex
      margin-bottom: 24px
      > .mc-contact
        max-width: 223px
        margin: auto
        > div:first-child
          font-family: FuturaBookC
          font-size: 14px
          line-height: 16px
          color: #DFB971
        > div:last-child
          font-family: FuturaBookC
          font-size: 16px
          line-height: 21px
    > .social-directions
      > div
        vertical-align: middle
        text-align: center
      > .icon
        display: inline-block
        padding: 18px
        width: 64px
        height: 64px
        color: #DFB971
        > i
          font-size: 24px
      > .input-group
        display: inline-flex
        width: 59%
        box-shadow: 0px 4px 12px 0px rgba(218,172,84,0.08)
        > .form-control-lg
          background: #FEFDFB
          border: none
          padding: 1.5rem 1rem
          &::placeholder
            font-family: FuturaBookC
            font-size: 1rem
            line-height: 21px
            color: #EED199
        .btn
          background: #FEFDFB
          border: none
          color: #DFB971

  .modal-footer
    padding: 0.5rem
    > iframe
      width: 100%
      height: 271px
      border-radius: 8px
      margin-right: 0px
    > .btn-ok
      position: absolute
      bottom: -25px
      left: 35%
      width: 202px
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
.modal-backdrop
  background: #cef2e9
  backdrop-filter: blur(16px)
</style>