import { createRouter, createWebHistory } from 'vue-router'
import Home from './components/Home.vue'        // ta page principale
import Admin from './components/Admin.vue'  // la future page admin

const routes = [
  { path: '/', component: Home },
  { path: '/admin', component: Admin }
]

const router = createRouter({
  history: createWebHistory('/'), // attention au base si GitHub Pages
  routes
})

export default router
