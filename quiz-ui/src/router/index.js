import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import Admin from '../views/Admin.vue'
import QuestionsList from '../views/QuestionsList.vue'
import QuestionAdminDisplay from '../views/QuestionAdminDisplay.vue'
import QuestionEdition from '../views/QuestionEdition.vue'
import NewQuizPage from '../views/NewQuizPage.vue';
import QuestionsManager from '../views/QuestionsManager.vue';
import YourScorePage from '../views/YourScorePage.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: HomePage,
    },
    {
      path: "/admin",
      name: "Admin",
      component: Admin,
    },
    {
      path: '/new-quiz',
      name: 'NewQuizPage',
      component: NewQuizPage
    },
    {
      path: '/your-score',
      name: 'your-score',
      component: YourScorePage
    },      
    {
      path: '/questions',
      name: 'Questions',
      component: QuestionsManager
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
      path: "/questionEdition/:questionId?",
      name: "QuestionEdition",
      component: QuestionEdition,
    },
    // ... autres routes
  ]
})

export default router