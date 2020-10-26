import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        Booking: {
            Procedure: '48j0',
            Doctor: '1h34',
            Date: '2020-10-10',
            Hour: '6:30'
        },
        usefulTips: true,
    }
});