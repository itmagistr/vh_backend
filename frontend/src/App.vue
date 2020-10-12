<template>
  <div id="app">
    <section v-if="errored">
      <p>We're sorry, we're not able to retrieve this information at the moment, please try back later</p>
    </section>
    <section v-else>
      <div v-if="loading">Загрузка...</div>
      <table class="table">
        <thead>
          <th>Время</th>
          <th>Статус</th>
        </thead>
        <tbody>
          <tr v-for="(info, index) in shedule" :key="index">
            <td>{{ info.t }}</td>
            <td>{{ info.s }}</td>
          </tr>
        </tbody>
      </table>
      <h1>Response "results"</h1>
      <div>{{ shedule }}</div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
      return {
          shedule: null,
          loading: true,
          errored: false
      };
  },
  async created() {
    await fetch('http://localhost:8000/ru/vhapi/timetatus/2020-10-10/')
        .then(stream => stream.json())
        .then(response => {
          this.shedule = response.results;
        })
        .catch(error => {
          console.error(error);
          this.errored = true
        })
    .finally(() => (this.loading = false));
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>