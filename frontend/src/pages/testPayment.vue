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
          <button type="button" class="btn" v-on:click="medproc">API medprocs</button>
          <button type="button" class="btn" v-on:click="invcreate">API invoice</button>
          <input v-model="mp_uid">
        </div>
        <div v-if="invoice">
          <ul>
            <li>{{invoice.invoice_id}}</li>
            <li>{{invoice.invoice_expire}}</li>
            <li>{{invoice.invoice_status}}</li>
            <li>{{invoice.invoice_title}}</li>
            <li>{{invoice.invoice_email}}</li>
            <li>{{invoice.invoice_token | truncate(50, '...')}}</li>
            </ul>
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
          results: null,
          payform: false,
          invoice: null,
          mp_uid: this.$store.state.Booking.Procedure,
          
      };
  },
  filters: {
        truncate: function (text, length, suffix) {
            if (text.length > length) {
                return text.substring(0, length) + suffix;
            } else {
                return text;
            }
        },
    },
  async created() {
    await fetch('http://localhost:8000/ru/vhapi/timestatus/2020-10-10/')
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
     
    medproc: function () {
      fetch('http://localhost:8000/ru/vhapi/medproc/').
      then(stream => stream.json()).
      then((response) => {this.invoice=false; this.results = response.results;}).
      catch((error) => {
                    console.log(error);
                });
    },
    invcreate: function () {
      fetch('http://localhost:8000/ru/vhapi/invoice/create/', {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({medproc_uid: this.mp_uid}) //<!-- '41b6e7a0-e395-45d3-bccb-ad097c427643' -->
  }).then(response => response.json())
    .then((data) => {this.invoice = data; this.results='';}).
      catch((error) => {
                    console.log(error);
                });
    },
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