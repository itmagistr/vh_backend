<template>
  <div class="d-flex ">
    <div class="row registration">
      <section v-if="errored">
        <p>We're sorry, we're not able to retrieve this information at the moment, please try back later</p>
      </section>
      <section v-else>
        <div v-if="loading">Загрузка...</div>
        <h2>Test requests</h2>
        <div class="btn-group" role="group">
          <button type="button" class="btn" v-on:click="daystatus">API daystatus</button>
          <button type="button" class="btn" v-on:click="tslots">API timeslots</button>
          <button type="button" class="btn" v-on:click="medproc">API medprocs</button>
          <button type="button" class="btn" v-on:click="doctors">API timeslots</button>
        </div>
        <div> {{results}} </div>
        <!--<table class="table">
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
        <div>{{ shedule }}</div>-->
      </section>
    </div>
  </div>
</template>

<script>
export default {
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
      fetch('http://localhost:8000/ru/vhapi/daystatus/2020-10-10/2020-10-31/').
      then(stream => stream.json()).
      then(response => this.results = response.results).
      catch((error) => {
                    console.log(error);
                });
    },
     tslots: function () {
      fetch('http://localhost:8000/ru/vhapi/timetatus/2020-10-10/').
      then(stream => stream.json()).
      then(response => this.results = response.results).
      catch((error) => {
                    console.log(error);
                });
    },
    medproc: function () {
      fetch('http://localhost:8000/ru/vhapi/medproc/').
      then(stream => stream.json()).
      then(response => this.results = response.results).
      catch((error) => {
                    console.log(error);
                });
    },
    doctors: function () {
      fetch('http://localhost:8000/ru/vhapi/doctor/').
      then(stream => stream.json()).
      then(response => this.results = response.results).
      catch((error) => {
                    console.log(error);
                });
    }
  }
}
</script>

<style lang="sass" scoped>
section
  font-family: Avenir, Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  text-align: center
  color: #2c3e50

.row
  padding: 10px

.btn
  background: #42E1C5
  color: #FEFDFB

  font-family: FuturaBookC
  font-style: normal
  font-weight: normal
  font-size: 16px
  line-height: 21px
  letter-spacing: 0.08em
  text-transform: uppercase

</style>