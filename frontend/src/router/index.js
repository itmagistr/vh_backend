import Vue from 'vue'
import VueRouter from 'vue-router'
import test from "@/pages/test.vue";
import testPayment from "@/pages/testPayment.vue";
import MainPage from "@/pages/MainPage";
import NotFoundPage from "@/pages/NotFoundPage";
import Booking from "@/pages/BookingPage";
import Service from "@/pages/ServicePage.vue"
import Doctors from "@/pages/DoctorsPage.vue"

Vue.use(VueRouter);

const routes = [
    // {name: 'openSoon', component: OpenSoon, path: '/'},
    {name: 'main', component: MainPage, path: '/secret_place/'},
    {name: 'service', component: Service, path: '/secret_place/service'},
    // {name: 'test', component: test, path: '/test/:id'},
    {name: 'booking', component: Booking, path: '/secret_place/booking'},
    {name: 'doctors', component: Doctors, path: '/secret_place/doctors'},
    {name: 'test', component: test, path: '/secret_place/test'},
    {name: 'testPayment', component: testPayment, path: '/secret_place/testPayment'},
    {name: 'notFound', component: NotFoundPage, path: '*'}
];

const router = new VueRouter({
    mode: 'history',
    hash: false,
    routes
});

export default router;