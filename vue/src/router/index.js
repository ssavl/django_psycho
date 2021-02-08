import Vue from 'vue'
import VueRouter from 'vue-router'
import DoctorsList from "@/views/DoctorsList"
import DoctorsDetail from "@/views/DoctorsDetail"
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';


Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'doctorsList',
        component: DoctorsList
    },
    {
        path: '/doctor/:id',
        name: 'doctorsDetail',
        component: DoctorsDetail,
        props: true
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
