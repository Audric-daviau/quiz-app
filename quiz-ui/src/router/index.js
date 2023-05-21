import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import AboutPage from '../views/AboutView.vue'
import Admin from '../views/Admin.vue'
import QuestionsList from '../views/QuestionsList.vue'
import QuestionAdminDisplay from '../views/QuestionAdminDisplay.vue'
import QuestionEdition from '../views/QuestionEdition.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: "/about",
      name: "AboutPage",
      component: AboutPage,
    },
    {
      path: "/admin",
      name: "Admin",
      component: Admin,
    },
    {
      path: "/questionAdminDisplay/:questionId",
      name: "QuestionAdminDisplay",
      component: QuestionAdminDisplay,
    },
    {
      path: "/questionsList",
      name: "QuestionsList",
      component: QuestionsList,
    },
    {
      path: "/questionEdition/:questionId",
      name: "QuestionEdition",
      component: QuestionEdition,
    },
    // ... autres routes
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router