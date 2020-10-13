<template>
  <div id="app">
    <section v-if="errored">
      <p>We're sorry, we're not able to retrieve this information at the moment, please try back later</p>
    </section>
    <section v-else>
      <div v-if="loading">Загрузка...</div>
      <h2>Test requests</h2>
      <div>
        <button v-on:click="daystatus">API daystatus</button> <button v-on:click="tslots">API timeslots</button>
        <button v-on:click="medproc">API medprocs</button> <button v-on:click="doctors">API doctors</button>
        <div>{{results}}</div>
      </div>
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
          errored: false,
          results: null
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
  },
  // определяйте методы в объекте `methods`
  methods: {
     daystatus: function () {
      fetch('http://localhost:8000/ru/vhapi/daystatus/2020-10-10/2020-10-31/').then(stream => stream.json()).then(response => this.results = response.results).catch((error) => {
                    console.log(error);
                });
    },
     tslots: function () {
      fetch('http://localhost:8000/ru/vhapi/timetatus/2020-10-10/').then(stream => stream.json()).then(response => this.results = response.results).catch((error) => {
                    console.log(error);
                });
    },
    medproc: function () {
      fetch('http://localhost:8000/ru/vhapi/medproc/').then(stream => stream.json()).then(response => this.results = response.results).catch((error) => {
                    console.log(error);
                });
    },
    doctors: function () {
      fetch('http://localhost:8000/ru/vhapi/doctor/').then(stream => stream.json()).then(response => this.results = response.results).catch((error) => {
                    console.log(error);
                });
    }

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