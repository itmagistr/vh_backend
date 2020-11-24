<template>
    <div class="d-flex flex-column mar">
        <div class="bgz">
            <div></div>
            <div></div>
        </div>
        <div class="tittle-of-service">Услуги</div>
        <div class="service">
            <div class="card-tooth active"><img src="/img/teeth/Orthodontics.svg"/><div>Ортодонтия</div></div>
            <div class="card-tooth"><img src="/img/teeth/Surgery.svg"/><div>Хирургия</div></div>
            <div class="card-tooth"><img src="/img/teeth/Treatment.svg"/><div>Лечение</div></div>
            <div class="card-tooth"><img src="/img/teeth/Whitening.svg"/><div>Отбеливание</div></div>
            <div class="card-tooth"><img src="/img/teeth/Prosthetics.svg"/><div>Протезирование</div></div>
            <div class="card-tooth"><img src="/img/teeth/Implantation.svg"/><div>Имплантация</div></div>
        </div>
        <div class="block-2">
            <div class="block-top">
                <div class="tittle">
                    Ортодонтия
                </div>
                <div class="text">
                    Значимость этих проблем настолько очевидна, что реализация намеченных плановых заданий обеспечивает
                    широкому кругу (специалистов) участие в формировании систем массового участия. Повседневная практика
                    показывает, что сложившаяся структура организации позволяет выполнять важные задания по разработке
                    форм развития. Разнообразный и богатый опыт сложившаяся структура организации в значительной степени
                    обуславливает создание направлений прогрессивного развития.
                </div>
            </div>
            <div class="accordion">

            </div>
        </div>
        <div class="block-3">
            <div class="block-left">
                <div>Цены на услуги</div>
                <table class="table table-borderless">
                    <tbody>
                        <tr v-for="c in results" class="product" :class="[{spec: c.code.length > 5}, { active: c.uuid === select}]" :key="c.uuid" @click="selected(c.uuid)">
                            <td class="pr-code">{{ c.code }}</td>
                            <td class="pr-tittle">{{ c.title }}</td>
                            <td class="pr-price">{{ c.price | currencyFormat("RUB")}}</td>
                            <td class="pr-duration">{{ c.duration | timeFormat("ru-RU")}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="block-right">
                <div class="doctor-card">
                    <div class="d-tittle">Очень длинное название процедуры, очень длинное врач Василенко Л.И.</div>
                    <div class="d-card">
                        <div id="icd"> </div>
                        <div id="nmd">
                          <div>Врач</div>
                          <div>Василенко Л.И.</div>
                        </div>
                        <button class="btn" id="btn-d"><i class="fas fa-caret-right"></i></button>
                    </div>
                </div>
                <div class="description">
                    <div>Описание процедуры</div>
                    <div>
                        Идейные соображения высшего порядка, а также начало повседневной работы по формированию позиции
                        обеспечивает широкому кругу (специалистов) участие в формировании модели развития. С другой
                        стороны начало повседневной работы по формированию позиции влечет за собой процесс внедрения.
                    </div>
                </div>
                <div class="recomende">
                    <div>Рекомендации перед процедурой</div>
                    <div><i class="profi"></i> Не кушать и не пить за 2 часа до процедуры</div>
                    <div><i class="profi"></i> Принять антигистаминный препарат</div>
                    <div><i class="profi"></i> Ограничить физическую активность за день до процедуры</div>
                    <div><i class="profi"></i> Хорошо очистить полость рта</div>
                </div>
                <div class="recomende">
                    <div>Рекомендации после процедуры</div>
                    <div><i class="profi"></i> Не кушать и не пить 3 часа после процедуры</div>
                    <div><i class="profi"></i> Очистка полости рта ирригатором</div>
                    <div><i class="profi"></i> Ограничить физическую активность на 3 дня после процедуры</div>
                </div>
                <div class="photo">
                    <div>Фото</div>
                    <div class="accordion">
                        <button class="btn btn-accord"><i class="fas fa-caret-left"></i></button>
                        <div></div>
                        <button class="btn btn-accord"><i class="fas fa-caret-right"></i></button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import currencyFormat from '@/helpers/currencyFormat';
import timeFormat from "@/helpers/timeFormat";

export default {
    data() {
        return {
            select: this.$store.state.Booking.Procedure,
            cat: [
                {uuid: '41b6e7a0-e395-45d3-bccb-ad097c427643', code: '01.01', tittle: 'Установка брекетов', price: 150000, duration: 90},
                {uuid: '951a9eb9-e0a4-444c-a060-a1d6a1e65181', code: '01.02', tittle: 'Замена брекет-системы', price: 3000, duration: 30},
                {uuid: '86862dce-dcee-4fed-9f84-5568cd2ce088', code: '01.03', tittle: 'Очень длинное название процедуры, очень длинное', price: 10000, duration: 120},
                {uuid: '222acbed-7f8b-45c4-b113-2b0df57f2b74', code: '01.03.01', tittle: 'Очень длинное название процедуры, очень длинное врач Василенко Л.И.', price: 10000, duration: 90},
                {uuid: '9e165e33-0205-4f10-b57a-94cc7009037a', code: '01.03.02', tittle: 'Очень длинное название процедуры, очень длинное врач Василенко Л.И.', price: 15000, duration: 90},
                {uuid: '181c9634-de66-44fa-a4fe-d7a59f8842ce', code: '01.04', tittle: 'Изготовление Капп', price: 500, duration: 15},
                {uuid: '5d44c307-cab4-43d8-b540-ef6921d3b97b', code: '01.05', tittle: 'Установка брекетов', price: 150000, duration: 90},
                {uuid: 'bb3a405d-e4a6-4b92-a769-3093b42405cd', code: '01.06', tittle: 'Замена брекет-системы', price: 3000, duration: 30},
                {uuid: '9629cb75-07b6-419f-bb53-b0e5b76b21f9', code: '01.07', tittle: 'Очень длинное название процедуры, очень длинное', price: 10000, duration: 120},
                {uuid: '1fd48dc3-6ff6-419e-8e80-a9c6e74b4516', code: '01.07.01', tittle: 'Очень длинное название процедуры, очень длинное врач Иванова Л.В.', price: 15000, duration: 90},
                {uuid: '2eef030f-0e18-424b-a506-dd814e0884e5', code: '01.04.02', tittle: 'Очень длинное название процедуры, очень длинное врач Василенко Л.И.', price: 13000, duration: 90},
                {uuid: 'e8ea70b7-6f8e-4815-bfb9-95abc4db836e', code: '01.08', tittle: 'Изготовление Капп', price: 500, duration: 15},
            ],
            loading: true,
            errored: false,
            results: null
        }
    },
    async created() {
        await this.getMedProc("Орто", "2020-11-24", "bf0f0856-f57d-48c6-b99c-b3c8a2e3ea82");
    },
    methods: {
        getMedProc(cat, date, docUID) {
            const options = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({"txt": cat, "dt": date, "doctor_uid": docUID})
            };
            fetch(`http://localhost:8000/ru/vhapi/medproc/list/`, options).
            then(response => response.json()).
            then(data => {
            this.results = data;
            console.log(data);
            }).
            catch((error) => { console.log(error); this.results = null;}).
            finally(() => {
              this.loading = false;
            });
        },
    },
    filters: {
        currencyFormat, timeFormat
    },
}
</script>

<style lang="sass" scoped>
@import "@/styles/_variables.sass"

.bgz
    div:first-child
        position: absolute
        z-index: -1
        background: rgba(254, 253, 251, 0.64)
        backdrop-filter: blur(16px)
        width: 100%!important
        height: 242px
        left: 0px
        top: 136px
    div:last-child
        position: absolute
        z-index: -1
        background: #F6F3ED
        width: 100%!important
        height: 182%
        left: 0px
        top: 378px

.mar
    > div
        margin-right: auto
        margin-left: auto
        width: 1362px
        text-align: center
        display: flex
    .tittle-of-service
        display: block!important
        font-family: FuturaBookC
        font-size: 64px
        line-height: 61px
        color: $button-color
        margin-bottom: 56px
        margin-top: -100px

.card-tooth
    &:first-child
        margin-left: 1px
    &:last-child
        margin-right: 1px
    vertical-align: middle
    width: 200px
    height: 200px
    padding: 40px
    background: #F3E9D4
    border-radius: 8px
    margin: 0px 16px
    &.active
        background: $active-link-line
    &.active > div
        color: $white
    > img
        margin-bottom: 36px
    > div
        color: $button-color


.block-2
    margin-top: 64px
    text-align: center
    display: block!important
    .tittle
        font-family: FuturaBookC
        font-size: 48px
        line-height: 56px
        color: $button-color
    .text
        font-family: FuturaBookC
        font-size: 16px
        line-height: 21px
    .accordion
        margin-top: 38px
        margin-left: auto
        margin-right: auto
        width: 1084px
        height: 236px
        background: #00C0BB55
        border-radius: 16px


.block-3
    margin-top: 64px
    margin-bottom: 128px
    display: flex
    .btn
        padding: 0px
    > .block-left, > .block-right
        height: 867px
        width: 681px
.block-left
    border-radius: 16px 0px 0px 16px
    background: $white
    padding: 32px
    text-align: left
    > div:first-child
        font-family: Montserrat
        font-weight: 500
        font-size: 21px
        line-height: 26px
        margin-bottom: 32px
    .product
        > td
            display: inline-table
            margin: 0px 8px
        > td:first-child
            margin: 0px 0px 8px
        > td:last-child
            margin-right: 0px
        > td
            margin-bottom: 8px
        &.active, &:hover
            background: rgba(238, 209, 153, 0.16)
        &.active > .pr-info > i, &:hover > .pr-info > i
            display: inline-table
        &.active > .pr-price, &:hover > .pr-price
            color: #B8882F
        &.active > .pr-duration, &:hover > .pr-duration
            color: #071013
        .pr-code
            width: 48px
            font-family: Montserrat
            font-size: 19px
            line-height: 24px
            color: #071013
        &.spec > .pr-code
            width: 120px
            font-size: 16px
            line-height: 21px
        .pr-tittle
            width: 376px
            font-family: FuturaBookC
            line-height: 16px
            margin-right: 32px
            color: #071013
        &.spec > .pr-tittle
            width: 300px
        .pr-price
            width: 72px
            font-family: FuturaBookC
            line-height: 21px
            text-align: right
            color: #DFB971
        .pr-duration
            width: 56px
            font-family: FuturaBookC
            line-height: 21px
            text-align: right
            color: #9CC6BE

.block-right
    border-radius: 0px 16px 16px 0px
    background: #F3E9D4
    padding: 32px
    text-align: left
    .doctor-card
        margin-bottom: 24px
        .d-tittle
            font-family: Montserrat
            font-weight: 500
            font-size: 21px
            line-height: 26px
            text-align: left
            margin-bottom: 24px
        .d-card
            background: white
            height: 72px
            width: 280px
            border-radius: 8px
            > div, > button
                display: inline-block
            #icd
                position: relative
                top: 8px
                left: 8px
                width: 56px
                height: 56px
                background: $active-link-line
                border-radius: 4px
            #nmd
                font-family: FuturaBookC
                position: relative
                top: -8px
                left: 24px
                width: 177px
                line-height: 1
                text-align: left
            #nmd > div:first-child
                color: $button-color
                font-size: 14px
            #nmd > div:last-child
                font-size: 16px
            #btn-d
                position: relative
                top: -16px
                right: -21px
                width: 26px
                height: 72px
                border: none
                border-radius: 0px 8px 8px 0px
                background: $none
                color: $white
    .description
        margin-bottom: 24px
        > div:first-child
            font-family: Montserrat
            font-size: 19px
            line-height: 24px
            color: #B8882F
            margin-bottom: 16px
        > div:last-child
            font-family: FuturaBookC
            font-size: 16px
            line-height: 21px
    .recomende
        margin-bottom: 20px
        i
            display: inline-block
            width: 8px
            height: 8px
            border-radius: 2px
        > div:first-child
            font-family: Montserrat
            font-size: 19px
            line-height: 24px
            color: #B8882F
            margin-bottom: 16px
        div
            font-family: FuturaBookC
            font-size: 16px
            line-height: 21px
            margin-bottom: 8px

    .photo
        > div:first-child
            font-family: Montserrat
            font-size: 19px
            line-height: 24px
            color: #B8882F
            margin-bottom: 16px
        .accordion
            height: 136px
            width: 621px
            background:  #F1EEE6
            border-radius: 4px
            overflow: hidden
            > div
                display: inline-block
                width: 589px
            .btn-accord
                display: inline-block
                width: 16px
                height: 136px
                background: #42E1C5
                border-radius: 4px
                border: none
                color: $white
</style>