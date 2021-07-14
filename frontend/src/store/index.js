import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        Booking: {
            Procedure: null,
            Doctor: null,
            Date: new Date().toLocaleString('en-CA', { dateStyle: 'short' }),
            Hour: null,
            Price: null,
        },
        usefulTips: false,
        phase: 2,
        apihost: 'http://localhost:8000/',
    },
    mutations: {
        updDoc(state, Doctor){
            state.Booking.Doctor = Doctor;
        },
        updProc(state, Procedure){
            state.Booking.Procedure = Procedure;
        },
        updPrice(state, Price){
            state.Booking.Price = Price;
        },
        updDate(state, Date){
            state.Booking.Date = Date;
        },
        updHour(state, Hour){
            state.Booking.Hour = Hour;
        },
        updPhase(state, Phase){
            state.phase = Phase;
        },
        updUT (state, payload){
            state.usefulTips = payload;
        }
    }
});
