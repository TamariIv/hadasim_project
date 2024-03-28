import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import Users from '../components/Users.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Users',
      component: Users,
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
  ]
})

export default router