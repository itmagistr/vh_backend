import Vue from 'vue'
import VueRouter from 'vue-router'
import test from "@/pages/test.vue";
import MainPage from "@/pages/MainPage";
import NotFoundPage from "@/pages/NotFoundPage";
import Booking from "@/pages/BookingPage";
import Service from "@/pages/ServicePage.vue"

Vue.use(VueRouter);

const routes = [
    {name: 'main', component: MainPage, path: '/'},
    {name: 'service', component: Service, path: '/service'},
    // {name: 'test', component: test, path: '/test/:id'},
    {name: 'booking', component: Booking, path: '/booking'},
    {name: 'test', component: test, path: '/test'},
    {name: 'notFound', component: NotFoundPage, path: '*'}
];

const router = new VueRouter({
    mode: 'history',
    hash: false,
    routes
});

export default router;