<template>
    <header>
      <nav class="navbar navbar-expand navbar-light">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <router-link class="nav-link" to="#">Услуги <span class="sr-only">(current)</span></router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link active" :to="{name: 'booking'}">Записаться</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="#">Врачи</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="#">Виртуальный тур</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="#">Документация</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="#">Контакты</router-link>
            </li>
          </ul>
          <ul class="navbar-nav mr-auto"><router-link class="nav-link active" :to="{name: 'main'}"><img class="logo" src="/img/logo-sm.svg"/></router-link></ul>
          <ul class="navbar-nav">
            <li class="nav-item">
              <div class="inner-addon right-addon">
                <i class="fas fa-search"></i>
                <input class="form-control" type="search" placeholder="Search" aria-label="Search"/>
              </div>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="nDML" role="button" data-toggle="dropdown"
                 aria-haspopup="true" aria-expanded="false"> Ru </a>
              <div class="dropdown-menu" aria-labelledby="nDML">
                <router-link class="dropdown-item" to="#">Русский</router-link>
                <router-link class="dropdown-item" to="#">English</router-link>
              </div>
            </li>
          </ul>
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link class="nav-link" to="#">Профиль <i class="fas fa-user"></i></router-link>
            </li>
          </ul>
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link class="nav-link number" to="#">+7 900 881 88 88</router-link>
              <router-link class="nav-link" id="order-call" to="#">Заказать звонок</router-link>
            </li>
          </ul>
        </div>
      </nav>
    </header>
</template>

<script>
export default {

}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

body
  background: url('/img/img1.png') no-repeat center center fixed
  background-size: cover

header
  background: rgba(254, 253, 251, 0.64)
  backdrop-filter: blur(32px)

.logo
  width: 250px

#order-call
  text-align: right
  color: $active-text-link!important

.active a
  color: $active-text-link

.navbar-light a, .navbar-light
  font-family: FuturaBookC
  font-style: normal
  font-weight: normal
  font-size: 14px
  line-height: 21px
  letter-spacing: 0.05em
  color: $header_text!important

.mr-auto a
  text-transform: uppercase

nav
  max-width: 1560px
  margin: auto
  height: 136px

.btn-outline
  color: $header_text
  background: #FFF

.btn-outline
  &:hover
    color: $header_text



// Change standart color of input
.form-control
  border: none
  color: $header_text

.form-control
  &::placeholder
    color: $header_text

.btn.focus, .btn, .social-btn
  &:focus
    outline: 0
    box-shadow: 0 0 0 0.2rem rgba(184,136,47,.25)

.form-control, .social-btn
  &:focus, &:hover
    outline: 0
    box-shadow: 0 0 0 0.2rem rgba(184,136,47,.25)
    color: $header_text

.container
  margin-top: 127px

.inner-addon
  position: relative

.inner-addon .fas
  position: absolute
  padding: 12px
  pointer-events: none
  transform: scaleX(-1)

.right-addon .fas
  right: 0px

.right-addon input
  padding-right: 30px

.number
  font-size: 21px!important
  line-height: 16px!important
  text-align: right

.right-side
  position: absolute
  right: 7.3%
  top: 304px


</style>