import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        Booking: {
            Procedure: null,
            Doctor: null,
            Date: null,
            Hour: null,
        },
        usefulTips: true,
        phase: 2,
    },
    mutations: {
        updDoc(state, Doctor){
            state.Booking.Doctor = Doctor;
        },
        updProc(state, Procedure){
            state.Booking.Procedure = Procedure;
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
        updateUT(state, payload){
            state.usefulTips = payload;
        }
    }
});