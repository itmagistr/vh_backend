<template>
    <header>
      <nav class="navbar navbar-expand navbar-light">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
              <a class="nav-link" href="#">Услуги <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link active" href="#">Записаться</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Врачи</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Виртуальный тур</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Документация</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Контакты</a>
            </li>
          </ul>
          <ul class="logo navbar-nav mr-auto">TO HOLLYWOOD</ul>
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
                <a class="dropdown-item" href="#">Русский</a>
                <a class="dropdown-item" href="#">English</a>
              </div>
            </li>
          </ul>
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="#">Профиль <i class="fas fa-user"></i></a>
            </li>
          </ul>
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link number" href="#">+7 900 881 88 88</a>
              <a class="nav-link order-call" href="#" style="color: #00C0BB">Заказать звонок</a>
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
$header_text: #B8882F
$button-color: #DFB971

$active-text-link: #00C0BB
$active-link-line: #42E1C5
body
  background: url('/img/img1.png') no-repeat center center fixed
  background-size: cover

header
  background: rgba(254, 253, 251, 0.64)
  backdrop-filter: blur(32px)

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

.order-call
  text-align: right
  color: $active-text-link!important

.right-side
  position: absolute
  right: 7.3%
  top: 304px

.social-btn
  display: block
  width: 64px
  height: 64px
  background: rgba(254, 253, 251, 0.64)!important
  backdrop-filter: blur(24px)!important
  border: none
  border-radius: 4px
  color: $header_text
  font-size: 22px
  margin: 12px 0px

.logo
    font-family: Josefin Sans
    font-style: normal
    font-weight: 300
    font-size: 28.925px
    line-height: 29px
    color: #000
    position: relative
    text-align: center


@media screen and (max-width: 1550px)
  header
    display: none

@media screen and (max-width: 991px)
  .registration
    display: none

@media screen and (min-width: 1200px)
  .container
    max-width: 1560px

@media screen and (max-width: 1200px)
  .container
    max-width: none
</style>