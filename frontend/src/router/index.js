import Vue from 'vue'
import VueRouter from 'vue-router'
import test from "@/pages/test.vue";
import MainPage from "@/pages/MainPage";
import NotFoundPage from "@/pages/NotFoundPage";
import Registration from "@/pages/Registration";

Vue.use(VueRouter);

const routes = [
    {name: 'main', component: MainPage, path: '/'},
    // {name: 'test', component: test, path: '/test/:id'},
    {name: 'registration', component: Registration, path: '/Registration'},
    {name: 'test', component: test, path: '/test'},
    {name: 'notFound', component: NotFoundPage, path: '*'}
];

const router = new VueRouter({
    mode: 'history',
    hash: false,
    routes
});

export default router;