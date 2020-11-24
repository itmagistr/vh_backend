<template>
    <div class="row">
        <div class="col doctor-choice">
            <div class="table-wrapper-scroll-y my-custom-scrollbar">
                  <div class="menu">
                        <button class="btn" @click="backToBooking()"><i class="fas fa-long-arrow-alt-left"/> Назад</button>
                        <div class="input-group">
                            <input type="text" class="form-control" placeholder="Найти процедуру..." aria-describedby="ba2">
                            <div class="input-group-append">
                                <button class="btn" type="button" id="ba2"><i class="fas fa-search"></i></button>
                            </div>
                        </div>
                  </div>
                  <div v-if="loading">Загрузка...</div>
                  <div class="doctor-clip" v-for="data in docs" :key="data.uid" :class="[select === data.uid ? 'active':'' ]"  @click="selected(data.uid)">
                        <div class="d-flex clip-header">
                            <div class="d-flex">
                                <div class="clip-photo"></div>
                                <div class="clip-bk1">
                                    <div class="clip-tittle">{{ data.tittle }}</div>
                                    <div class="clip-name">{{ data.fName }} {{ data.lName }} <br> {{ data.tName }}</div>
                                </div>
                            </div>
                            <div class="d-flex ml-auto flex-column clip-info">
                                <div>{{ data.arg1 }}</div>
                                <div>{{ data.arg2 }}</div>
                                <div>{{ data.arg3 }}</div>
                            </div>
                        </div>
                        <div class="clip-body">
                            <div class="clip-accordion">Процедуры <i class="fas fa-caret-down"></i></div>
                            <div class="clip-accordion">Фото работ <i class="fas fa-caret-down"></i></div>
                            <div class="clip-accordion">Youtube <i class="fas fa-caret-down"></i></div>
                            <div class="clip-accordion">Сертификаты <i class="fas fa-caret-down"></i></div>
                            <div class="clip-accordion">Образование <i class="fas fa-caret-down"></i></div>
                        </div>
                        <div class="d-flex clip-footer">
                            <div class="d-flex clip-rating">
                                  <i class="fas fa-star star-full"></i>
                                  <i class="fas fa-star star-full"></i>
                                  <i class="fas fa-star star-full"></i>
                                  <i class="fas fa-star star-half"></i>
                                  <i class="fas fa-star star-none"></i>
                            </div>
                            <div class="d-flex clip-review">{{ data.countReview }} отзыва</div>
                            <div class="d-flex ml-auto clip-icons">
                                <i class="fas fa-phone" style="transform: scaleX(-1)"/>
                                <i class="far fa-comment-alt"/>
                                <i class="fas fa-heart"/>
                            </div>
                        </div>
                  </div>
            </div>
            <button class="btn" @click="send()">Выбрать врача</button>
        </div>
    </div>
</template>

<script>
import currencyFormat from '@/helpers/currencyFormat';
import timeFormat from "@/helpers/timeFormat";

export default {
    props: ['value'],
    data() {
        return {
            select: this.$store.state.Booking.Doctor,
            docs: [],
            loading: true,
            errored: false,
            results: null
        }
    },
    async created() {
        await this.docList('', this.$store.state.Booking.Date, 'bf0f0856-f57d-48c6-b99c-b3c8a2e3ea82');
    },
    filters: {
        currencyFormat, timeFormat
    },
    methods: {
        docList(cat, date, docUID) {
            const options = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({"txt": cat, "dt": date, "doctor_uid": docUID})
            };
            fetch(`http://localhost:8000/ru/vhapi/doctor/list/`, options).
            then(response => response.json()).
            then(data => {
            this.results = data;
            console.log(data);
            }).
            catch((error) => { console.log(error); this.results = null;}).
            finally(() => {
              this.loading = false;
              this.docs = this.temp(this.results);
            });
        },
        temp(array) {
            const buf = this.docs;
            for(let i = 0; i < array.length; i++) {
                buf.push({ uid: array[i].uid, img: '/img/Teeth/Orthodontics.svg', tittle: array[i].special,
                    fName: array[i].firstName, lName: array[i].lastName, tName: 'Ивановна', arg1: 'Стаж 26 лет',
                    arg2: 'Высшая категория', arg3: 'Кандидат медицинских наук', rating: null, countReview: 24,
                    phone: null, messenger: null,
                    results: [ {
                        procedure: [{tittle: null}, ],
                        photo: [{img: null, tittle: null}, ],
                        youtube: [{url: null}, ],
                        certificates: [{tittle: null}, ],
                        eduction: [{year: null, course: null, grade: null}, ]}, ],
                });//TODO доавить в ответ бека данные строки (img, отчество, стаж, категорию, степень, рейтинг, кол-во отзывов, телефон, чат, и results(временно пустой)).
            }
            console.log(buf);
            return buf;
        },
        backToBooking(){
            this.select = this.$store.state.Booking.Doctor;
            this.$emit('pageDoctor', this.select, 2);
        },
        selected(val){
            this.select = val;
        },
        send(){
            this.$store.commit("updDoc", this.select);
            this.$emit('pageDoctor', this.select, 2);
        },
    }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.doctor-choice
    /*background: linear-gradient(180deg, #FEFDFB 0%, #FEFDFB 78.65%, rgba(254, 253, 251, 0.16) 92.71%, rgba(254, 253, 251, 0.08) 100%)*/
    background: $white
    border-radius: 8px
    height: 536px

.my-custom-scrollbar
      position: relative
      height: 100%
      padding: 32px
      overflow: auto

::-webkit-scrollbar
      width: 0px

.menu
    height: 64px
.menu > .btn
    display: inline-block
    font-family: FuturaBookC
    font-size: 16px
    line-height: 21px
    color: #071013
    margin-right: 25px
    padding: 6px 0px
    box-shadow: none
.menu .form-control::placeholder
    color: rgba( 238,209,153,0.32)
    font-family: FuturaBookC
    font-size: 16px
    line-height: 21px
.menu .input-group
    width: 533px
    display: inline-flex
.menu input
    height: 48px
    border-radius: 8px
#ba2 .fas
    transform: scaleX(-1)
    color: #B8882F
#ba2
    background: white

.doctor-clip:hover, .doctor-clip.active
   box-shadow: 0 0 0 0.2rem #b8882f40

.clip-header
    margin-bottom: 16px
.clip-body
    margin-bottom: 24px
.clip-footer
    vertical-align: middle
.doctor-clip
    border: 1px solid rgba(238, 209, 153, 0.32)
    border-radius: 8px
    width: 624px
    min-height: 328px
    margin-bottom: 16px
    padding: 24px
.clip-photo
    width: 64px
    height: 64px
    background: $active-link-line
    border-radius: 4px
    margin-right: 12px

.clip-bk1
    vertical-align: top
    .clip-tittle
        font-family: FuturaBookC
        font-size: 14px
        line-height: 16px
        color: #B8882F
        padding-top: 4px
        padding-bottom: 4px
    .clip-name
        font-family: Montserrat
        font-size: 19px
        line-height: 19px
        color: #071013
.clip-info
    text-align: right
    font-family: FuturaBookC
    font-size: 16px
    line-height: 21px
    color: #071013


.clip-accordion
    font-family: FuturaBookC
    font-size: 16px
    line-height: 21px
    letter-spacing: 0.08em
    text-transform: uppercase
    color: #071013
    margin: 8px 0px
.clip-accordion > i
   margin-left: 8px
   color: $blue_three

.clip-rating
    font-size: 22px
    line-height: 22px
    margin-right: 12px
.clip-rating > i
    margin-right: 4px
.clip-review, .clip-icons
    font-family: FuturaBookC
    font-size: 16px
    line-height: 21px
    color: $blue_three
.clip-icons
    font-size: 22px
    line-height: 22px
    color: $blue_three
.clip-icons > i
    margin-left: 16px

.doctor-choice > .btn
    font-family: FuturaBookC
    letter-spacing: 0.08em
    text-transform: uppercase
    width: 233px
    height: 48px
    background: $active-link-line
    border: none
    border-radius: 8px
    color: $white
    position: absolute
    bottom: -9%
    right: 15%
    transform: translate(-50%, -50%)
</style>