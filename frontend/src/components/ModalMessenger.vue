<template>
  <div class="modal fade" id="mdl-messenger" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog modal-ctm modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Онлайн-чат</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body" id="chatting">
          <div v-for="msg in msgs" :key="msg.uid" ref="mesrefs" :class="msg.type === -1 ? 'left' : 'right'">
            <img src="@/assets/defaultAvatar.png">
            <div>
              <div>
                <h6 class="ch-name">{{ msg.name }}</h6>
                <h6 class="ch-time">{{ msg.time }}</h6>
              </div>
              <h6 class="ch-msg">{{ msg.msg }}</h6>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <div class="inner-addon right-addon">
            <input type="text" placeholder="Введите сообщение..." aria-label="Message"
                   class="form-control" v-model="msg">
            <i class="fas" aria-hidden="true" @click="fun"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default{
  data() {
    return {
      msgs: [
        { uid: 0, name: 'Анастасия', time: '16:32',
          msg: 'Здравствуйте, чем я могу вам помочь?', type: -1 },
        { uid: 1, name: 'Наталья Ковалева', time: '16:33',
          msg: 'Здравствуйте, какой вид анастезии использует ваша клиника?', type: 1 },
      ],
      chatInfo: [
        { img: '@/assets/defaultAvatar.png', name: 'Анастасия', type: -1 },
        { img: '@/assets/defaultAvatar.png', name: 'Наталья Ковалева', type: 1 }
      ],
      msg: null,
    }
  },
  methods: {
    fun(){
      if(this.msg !== null){
        console.log(this.msg);
        this.msgs.push({ uid: this.msgs.length, name: 'Наталья Ковалева', time: Math.random(), msg: this.msg, type: 1 });
        this.msg = null;
        this.scrollingTo();
      }
    },
    scrollingTo(){
      let scroll = document.getElementById("chatting");
      console.log(scroll);
      scroll.scrollTo({ top: scroll.scrollHeight, behavior: 'smooth' });
    },
  },
}
</script>

<style lang="sass">
#mdl-messenger
  > .modal-ctm
    max-width: 400px
    > .modal-content
      background: #FEFDFB
      border: none
      border-radius: 0.5rem
  .modal-header
    border-bottom: none
    padding-bottom: 0
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
    margin: 2rem 0 1rem
    padding: 0 2rem
    overflow: auto
    height: 450px
    > div
      display: flex
      justify-content: space-between
      margin-bottom: 1rem
      > img
        width: 2rem
        height: 2rem
        border-radius: .25rem
      > div
        font-family: FuturaBookC
        box-shadow: 0px 4px 12px 0px rgba(218,172,84,0.08)
        padding: 16px
        width: 280px
        > div
          display: flex
          flex-direction: row
          justify-content: space-between
          > h6
            font-size: 14px
            line-height: 1rem
            &.ch-name
              color: #EED199
            &.ch-time
              color: #9CC6BE
        > .ch-msg
          line-height: 21px
          color: #071013
      &.left
        flex-direction: row
        margin-right: 1rem
        > div
          border-radius: 0 1rem 1rem 1rem
      &.right
        flex-direction: row-reverse
        margin-left: 1rem
        > div
          border-radius: 1rem 0 1rem 1rem
  .modal-footer
    border-top: none
    padding: 0px 32px 32px
    > div
      box-shadow: 0px 4px 12px 0px rgba(218,172,84,0.08)
      width: 100%
      > i
        position: absolute
        bottom: 36px
        right: 36px
        transform: scaleY(1)
        height: 38px
        width: 38px
        background-image: url(/img/arrow.svg)
        background-position: center
        background-repeat: no-repeat
        pointer-events: auto
      > input
        padding-right: 38px

@media (max-width: 450px)
  #mdl-messenger
    > .modal-ctm
      display: block
      height: 100%
      max-width: inherit
      margin: 0
      > .modal-content
        height: 100%
        border-radius: 0px
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
          padding: 0 1rem
</style>
