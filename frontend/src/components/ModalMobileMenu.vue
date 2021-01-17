<template>
    <div class="modal fade" id="mdlm-menu" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog modal-ctm modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button class="navbar-toggler" type="button" data-toggle="modal" data-target="#mdlm-menu">
              <i class="fas fa-bars"></i>
            </button>
            <ul>
              <li class="dropdown">
                <a class="dropdown-toggle" href="#" id="nDML" role="button" data-toggle="dropdown"
                   aria-haspopup="true" aria-expanded="false"> Ru </a>
                <div class="dropdown-menu" aria-labelledby="nDML">
                  <router-link class="dropdown-item" to="#">Русский</router-link>
                  <router-link class="dropdown-item" to="#">English</router-link>
                </div>
              </li>
              <li>
                <router-link to="#">Личный кабинет <i class="fas fa-user"></i></router-link>
              </li>
            </ul>
          </div>
          <div class="modal-body">
            <ul class="navbar-nav mr-auto">
              <li class="nav-item" :id="[$route.name === 'service' ? 'active' : '']">
                <router-link class="nav-link" data-dismiss="modal" :to="{name: 'service'}">Услуги</router-link>
              </li>
              <li class="nav-item" :id="[$route.name === 'booking' ? 'active' : '']">
                <router-link class="nav-link active" data-dismiss="modal" :to="{name: 'booking'}">Записаться</router-link>
              </li>
              <li class="nav-item" :id="[$route.name === 'doctors' ? 'active' : '']">
                <router-link class="nav-link" data-dismiss="modal" :to="{name: 'doctors'}">Врачи</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" data-dismiss="modal" to="#">Виртуальный тур</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" data-dismiss="modal" to="#">Документация</router-link>
              </li>
              <li class="nav-item">
                <a class="nav-link" data-toggle="modal" data-dismiss="modal" data-target="#mdl-contacts">Контакты</a>
              </li>
            </ul>
          </div>
          <div class="modal-footer">
            <router-link :to="{name: 'main'}"><img class="logo" data-dismiss="modal" src="/img/logo_light.svg"/></router-link>
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
@import "@/styles/_variables.sass"

.navbar-light
  > .navbar-toggler
    color: #EED199
    border: none
    padding: .5rem .75rem

#mdlm-menu
  .modal-ctm
    margin: 0px
    display: block
    max-width: 481px
    border-radius: 0px 0px 8px 0px
    > .modal-content
      > .modal-header
        > .navbar-toggler
          color: $white
    > div
      border: none
      .modal-header, .modal-footer
        border: none
      .modal-body, .modal-footer
        text-align: center
        display: block
        padding: 0px
      .modal-footer
        border-radius: 0px 0px 8px 0
        .logo
          width: 240px
      .modal-header
        height: 66px
        > ul
          display: inline-flex
          list-style: none
          > li
            padding: .5rem .5rem
            > a
              color: #FEFDFB!important
      > div
        background: #42E1C5
        &.modal-body > ul
          > li
            height: 56px
            padding: 16px
            margin: 9px 0px
            > a
              padding: 0px
              color: #FEFDFB!important
            &#active, &:hover
              background: #EED199
@media (max-width: 1399px)
  .modal-backdrop
    background: rgba(254, 253, 251, 0.64)

@media (max-width: 450px)
  .mobile.logo
    width: 145px
  #mdlm-menu
    > .modal-ctm
      height: 100%
      border-radius: 0px
      > .modal-content
        height: 100%
        > .modal-header
          > .navbar-toggler
            color: $white
        > .modal-footer
          border-radius: 0px!important
      > div > div.modal-body > ul > li
        height: 45px
        padding: 10px
        margin: 6px 0px
</style>
