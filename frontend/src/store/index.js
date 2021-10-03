import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        Booking: {
            Procedure: null,
            Doctor: null,
            Date: new Date().toISOString().split('T')[0],
            Hour: null,
            Price: null,
        },
        question: '',
        usefulTips: false,
        phase: 2,
        apihost: 'http://localhost:8000/',
        apihostImg: 'http://localhost:8000',
    },
    getters: {
        question: state => state.question,
    },
    mutations: {
        setQuestion(state, q){
            state.question = q;
        },
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
