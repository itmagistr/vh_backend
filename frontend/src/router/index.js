import Vue from 'vue'
import VueRouter from 'vue-router'
import test from "@/pages/test";
import testPayment from "@/pages/testPayment";
import MainPage from "@/pages/MainPage";
import NotFoundPage from "@/pages/NotFoundPage";
import Booking from "@/pages/BookingPage";
import Service from "@/pages/ServicePage";
import Doctors from "@/pages/DoctorsPage";
import ComingSoon from "@/pages/ComingSoonPage"
import Documents from "@/pages/DocumentsPage";

Vue.use(VueRouter);

const routes = [
    {name: 'ComingSoon', component: ComingSoon, path: '/secret_place'},
    {name: 'main', component: MainPage, path: '/'},
    {name: 'service', component: Service, path: '/service'},
    // {name: 'test', component: test, path: '/test/:id'},
    {name: 'booking', component: Booking, path: '/booking'},
    {name: 'doctors', component: Doctors, path: '/doctors'},
    {name: 'documents', component: Documents, path: '/documents'},
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
