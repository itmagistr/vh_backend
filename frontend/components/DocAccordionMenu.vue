<template>
  <div>
    <div class="clip-accordion" :class="[states.proc ? 'active' : '']" @click="show('proc')">
      {{ $t('modaldoccard.procedure') }} <i class="fas fa-caret-down"></i>
    </div>
    <listView v-show="states.proc" class="listproc" :doctor-uid="selfInfo.uid"
              :info-button="true" :resize="true" :info-block="true"/>
    <div class="clip-accordion" :class="[states.photo ? 'active' : '']" @click="show('photo')">
      {{ $t('modaldoccard.photo') }} <i class="fas fa-caret-down"></i>
    </div>
    <Carousel v-show="states.photo" :self-info="selfInfo.uid"/>
    <div class="clip-accordion" :class="[states.social ? 'active' : '']" @click="show('social')">
      {{ $t('modaldoccard.social') }} <i class="fas fa-caret-down"></i>
    </div>
    <div v-show="states.social" class="soc-btn-card">
      <a :href="selfInfo.insta || '#'" :target="selfInfo.insta !== null ? '_blank': ''">
        <button class="social-btn"><i class="fab fa-instagram"></i></button></a>
      <a :href="selfInfo.youtube || '#'" :target="selfInfo.youtube !== null ? '_blank': ''">
        <button class="social-btn"><i class="fab fa-youtube"></i></button></a>
      <a :href="selfInfo.fb || '#'" :target="selfInfo.fb !== null ? '_blank': ''">
        <button class="social-btn"><i class="fab fa-facebook-f"></i></button></a>
      <a :href="selfInfo.vk || '#'" :target="selfInfo.vk !== null ? '_blank': ''">
        <button class="social-btn"><i class="fab fa-vk"></i></button></a>
    </div>
    <div class="clip-accordion" :class="[states.cert ? 'active' : '']" @click="show('cert')">
      {{ $t('modaldoccard.certificate') }} <i class="fas fa-caret-down"></i>
    </div>
    <div v-show="states.cert" class="cert">{{selfInfo.сertificate || null}}</div>
    <div class="clip-accordion" :class="[states.edu ? 'active' : '']" @click="show('edu')">
      {{ $t('modaldoccard.education') }} <i class="fas fa-caret-down"></i>
    </div>
    <div v-show="states.edu" class="edu">{{selfInfo.education || null}}</div>
  </div>
</template>

<script>
import Carousel from "@/components/DoctorWorkresCarousel"
import listView from "@/components/ProcedureListView";

export default {
  components: { Carousel, listView },
  props: { selfInfo: Object },
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
    white-space: pre-wrap
  > .edu
    display: flex
    margin: 0 1.5rem 3rem
    white-space: pre-wrap
</style>