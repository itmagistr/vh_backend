<template>
  <div>
    <div class="clip-accordion" @click="show('proc')" :class="[states.proc ? 'active' : '']">
      {{ $t('modaldoccard.procedure') }} <i class="fas fa-caret-down"></i>
    </div>
    <listView class="listproc" v-show="states.proc" :doctorUID="selfInfo.uid"
              :infoButton="true" :resize="true" :infoBlock="true"/>
    <div class="clip-accordion" @click="show('photo')" :class="[states.photo ? 'active' : '']">
      {{ $t('modaldoccard.photo') }} <i class="fas fa-caret-down"></i>
    </div>
    <Carousel v-show="states.photo" :self-info="selfInfo.uid"/>
    <div class="clip-accordion" @click="show('social')" :class="[states.social ? 'active' : '']">
      {{ $t('modaldoccard.social') }} <i class="fas fa-caret-down"></i>
    </div>
    <div class="soc-btn-card" v-show="states.social">
      <a :href="selfInfo.insta || '#'" :target="selfInfo.insta !== null ? '_blank': ''">
        <button class="social-btn"><i class="fab fa-instagram"></i></button></a>
      <a :href="selfInfo.youtube || '#'" :target="selfInfo.youtube !== null ? '_blank': ''">
        <button class="social-btn"><i class="fab fa-youtube"></i></button></a>
      <a :href="selfInfo.fb || '#'" :target="selfInfo.fb !== null ? '_blank': ''">
        <button class="social-btn"><i class="fab fa-facebook-f"></i></button></a>
      <a :href="selfInfo.vk || '#'" :target="selfInfo.vk !== null ? '_blank': ''">
        <button class="social-btn"><i class="fab fa-vk"></i></button></a>
    </div>
    <div class="clip-accordion" @click="show('cert')" :class="[states.cert ? 'active' : '']">
      {{ $t('modaldoccard.certificate') }} <i class="fas fa-caret-down"></i>
    </div>
    <div class="cert" v-show="states.cert">
      {{selfInfo.сertificate || null}}
    </div>
    <div class="clip-accordion" @click="show('edu')" :class="[states.edu ? 'active' : '']">
      {{ $t('modaldoccard.education') }} <i class="fas fa-caret-down"></i>
    </div>
    <div class="edu" v-show="states.edu">
      {{selfInfo.education || null}}
    </div>
  </div>
</template>

<script>
import Carousel from "@/components/DoctorWorkresCarousel"
import listView from "@/components/ProcedureListView";

export default {
  props: ['selfInfo'],
  data(){
    return {
      states: {
        proc: false,
        photo: false,
        social: false,
        cert: false,
        edu: false
      },
    }
  },
  components: {
    Carousel, listView
  },
  watch: {
    selfInfo: {
      handler(newValue, oldValue) {
        if (newValue === oldValue)
          return;
        this.states = { proc: false, photo: false, social: false, cert: false, edu: false };
      },
    },
  },
  methods: {
    show(pos){
      this.states[pos] = !this.states[pos];
    },
  }
}
</script>

<style lang="sass">
@import "@/styles/_variables.sass"

.modal-body, .clip-body
  > .clip-accordion
    font-family: FuturaBookC
    font-size: 16px
    letter-spacing: 0.08em
    text-transform: uppercase
    color: $black
    height: 1.5rem
    margin-bottom: 1rem
    padding: 0px 1.5rem
    &:hover, &.active
      color: $white
      background-color: $active-link-line
      > i
        transform: scaleY(-1)
        color: $white
    > i
      margin-left: 8px
      color: $blue_three
  > .soc-btn-card
    display: flex
    margin: 0 1.5rem 1rem
    > a
      margin: 0 .5rem
      > button
        border: 1px solid $header_text
        border-radius: 4px
        margin: 0
  > .listproc
    margin-bottom: 1rem
  > .cert
    display: flex
    margin: 0 1.5rem 1rem
  > .edu
    display: flex
    margin: 0 1.5rem 3rem
</style>