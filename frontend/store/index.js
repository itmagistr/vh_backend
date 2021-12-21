export const state = () => ({
    counter: 0,
    resize: false,
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
    apihostImg: 'http://localhost:8000'
})

export const getters = {
    question: state => state.question,
    resize: state => state.resize
}

export const mutations = {
    setResize(state, bool) {
        state.resize = bool;
    },
    increment(state, Phase) {
        state.counter+=Phase
    },
    setQuestion(state, q) {
        state.question = q;
    },
    updDoc(state, Doctor) {
        state.Booking.Doctor = Doctor;
    },
    updProc(state, Procedure) {
        state.Booking.Procedure = Procedure;
    },
    updPrice(state, Price) {
        state.Booking.Price = Price;
    },
    updDate(state, Date) {
        state.Booking.Date = Date;
    },
    updHour(state, Hour) {
        state.Booking.Hour = Hour;
    },
    updPhase(state, Phase) {
        state.phase = Phase;
    },
    updUT (state, payload) {
        state.usefulTips = payload;
    }
} 