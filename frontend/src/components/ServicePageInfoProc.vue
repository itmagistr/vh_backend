<template>
  <div>
      <div class="doctor-card">
          <div class="d-tittle">Очень длинное название процедуры, очень длинное врач Василенко Л.И.</div>
          <div class="d-card">
              <img id="icd" src="@/assets/defaultAvatar.png">
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
</template>

<script>

</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.hm-block
  width: 100%
  border-radius: 0px
  margin-bottom: 24px
  background: #F3E9D4
.block-right
  border-radius: 0px 16px 16px 0px
  background: #F3E9D4
.block-right, .hm-block
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
      img#icd
        position: relative
        top: 8px
        left: 8px
        width: 56px
        height: 56px
        border-radius: .25rem
        vertical-align: initial
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
        top: -17px
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
      width: 100%
      background:  #F1EEE6
      border-radius: 4px
      overflow: hidden
      > div
        display: inline-block
        width: calc(100% - 32px)
      .btn-accord
        display: inline-block
        width: 16px
        height: 136px
        background: #42E1C5
        border-radius: 4px
        border: none
        color: $white
        &:hover
          background: #EED199
          box-shadow: none
</style>
