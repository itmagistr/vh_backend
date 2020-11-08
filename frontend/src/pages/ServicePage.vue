<template>
    <div class="d-flex service">
        <div class="card-tooth active"><img src="/img/teeth/Orthodontics.svg"/><div>Ортодонтия</div></div>
        <div class="card-tooth"><img src="/img/teeth/Surgery.svg"/><div>Хирургия</div></div>
        <div class="card-tooth"><img src="/img/teeth/Treatment.svg"/><div>Лечение</div></div>
        <div class="card-tooth"><img src="/img/teeth/Whitening.svg"/><div>Отбеливание</div></div>
        <div class="card-tooth"><img src="/img/teeth/Prosthetics.svg"/><div>Протезирование</div></div>
        <div class="card-tooth"><img src="/img/teeth/Implantation.svg"/><div>Имплантация</div></div>
    </div>
</template>

<script>
export default {

}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.service
    width: 1362px
    text-align: center

.card-tooth:first-child
    margin-left: 1px
.card-tooth:last-child
    margin-right: 1px
.card-tooth
    vertical-align: middle
    width: 200px
    height: 200px
    padding: 40px
    background: #F3E9D4
    border-radius: 8px
    margin: 0px 16px
.card-tooth.active
    background: $active-link-line
.card-tooth.active > div
    color: $white
.card-tooth > img
    margin-bottom: 36px
.card-tooth > div
    color: $button-color
</style>