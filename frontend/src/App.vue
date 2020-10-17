<template>
  <body>
    <noscript>
      <strong>We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled.
        Please enable it to continue.</strong>
    </noscript>
    <Header></Header>
    <main>
      <div class="container">
        <div class="d-flex align-items-center justify-content-between">
          <div class="d-flex flex-column">
            <button class="social-btn"><i class="fab fa-instagram"></i></button>
            <button class="social-btn"><i class="fab fa-youtube"></i></button>
            <button class="social-btn"><i class="fab fa-facebook-f"></i></button>
            <button class="social-btn"><i class="fab fa-vk"></i></button>
          </div>
          <div class="d-flex ">
            <router-view/>
          </div>
          <div class="d-flex flex-column">
            <button class="social-btn"><i class="far fa-comment-alt"></i></button>
            <button class="social-btn"><i class="fas fa-map-marker-alt"></i></button>
            <button class="social-btn"><i class="fas fa-route"></i></button>
            <button class="social-btn"><i class="fas fa-phone-alt"></i></button>
            <button class="social-btn"><i class="fab fa-telegram-plane"></i></button>
          </div>
        </div>
      </div>
    </main>
  </body>
</template>

<script>
import Header from "@/components/Header.vue";

export default {
  components: { Header },
};
</script>

<style lang="sass">

</style>