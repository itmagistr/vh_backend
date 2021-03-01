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
                <div>г. Москва, пл. Новая, д. 8с2</div>
              </div>
              <div class="mc-contact">
                <div>Телефон</div>
                <div>+7 (495) 123-45-67</div>
              </div>
              <div class="mc-contact">
                <div>E-mail</div>
                <div>tohlwdmsk@gmail.com</div>
              </div>
            </div>
            <div class="social-directions">
              <div class="icons">
                <a class="icon" href="https://www.instagram.com/tohwddent" target="_blank"><i class="fab fa-instagram"></i></a>
                <a class="icon" href="https://www.youtube.com/channel/UCeyxKBqdLFA79kCTH29RDsQ" target="_blank"><i class="fab fa-youtube"></i></a>
                <a class="icon" href="https://www.facebook.com/ToHwdDent" target="_blank"><i class="fab fa-facebook-f"></i></a>
                <a class="icon" href="https://vk.com/tohwddent" target="_blank"><i class="fab fa-vk"></i></a>
              </div>
              <div class="input-group">
                <input type="text" class="form-control form-control-lg" placeholder="Показать проезд от адреса" aria-describedby="button-addon4">
                <div class="input-group-append" id="button-addon4">
                  <button class="btn" type="button"><img src="/img/bus.svg"/></button>
                  <button class="btn" type="button"><img src="/img/car.svg"/></button>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <iframe src="https://yandex.ru/map-widget/v1/?um=constructor%3A7a99b0b6bc976ab39bf895d707cb8aa60139b2c512dab621df6fbfb62d999caf&amp;source=constructor" frameborder="0"></iframe>
            <button type="button" class="btn btn-ok" data-dismiss="modal" data-toggle="modal" data-target="#mdl-leave-request">Обратная связь</button>
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
      border: none
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
      > span
        font-size: 2rem
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
      > div.icons
        display: inline-flex
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
        width: calc(100% - 256px)
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
    padding: 0px
    > iframe
      width: 100%
      height: 271px
      border-radius: 8px
      margin: 8px
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

@media (max-width: 1399px)
  #mdl-contacts
    > .modal-ctm
      display: block
      height: 100%
      > .modal-content
        height: 100%
        > .modal-header
          height: 64px
          border-bottom: 1px solid #DFB971
          padding: 20px 16px
          > .modal-title
            margin: 0px
          > .close
            position: relative
            padding: 0px
            top: 20px
            line-height: 1rem
        > .modal-body
          > .social-directions
            > div.icons
              display: block
            > .input-group
              width: 100%
        > .modal-footer
          height: 100%
          > iframe
            height: calc(100% - 130px)
            margin: 0px
          > .btn
            position: static
            margin: 32px auto 50px
            left: auto
            bottom: auto
@media (max-width: 450px)
  #mdl-contacts
    > .modal-ctm
      > .modal-content
        > .modal-body
          > .gp-mc-contact
            margin-top: 16px
            display: block
            > .mc-contact
              margin: 0 0 8px
        > .modal-footer
          > iframe
            height: calc(100% - 76px)
            margin-bottom: 76px
          > .btn
            margin: 0px
            position: absolute
            left: 50%
            bottom: 30px
            transform: translate(-50%, -50%)
</style>
