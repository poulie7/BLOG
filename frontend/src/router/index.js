import { createRouter, createWebHistory } from "vue-router";
import IndexView from '../views/IndexView.vue'
import AboutView from '../views/AboutView.vue'
import ArticleView from '../views/Article.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import SignUpView from '../views/SignUpView.vue'
import HomeView from '../views/HomeView.vue'
import CreateView from '../views/CreateView.vue'
import CategorieView from '../views/CategorieView.vue'
import ArticleCreated from '../views/ArticleCreated.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/articles',
            name: 'articles',
            component: IndexView
        },
        {
            path: '/about',
            name: 'about',
            component:  AboutView
        },
        {
            path: '/create',
            name: 'create',
            component: CreateView,
            meta: { requiresAuth: true },
        },
        {
            path: '/article/:id',
            name: 'article',
            component: ArticleView
        },
        {
            path: '/categorie/:id',
            name: 'categorie',
            component: CategorieView
        },
        { 
            path: '/login',
            name: 'login',
            component: LoginView
        },
        { 
            path: '/logout',
            name: 'logout',
            component: LogoutView
        },
        { 
            path: '/signup',
            name: 'signup',
            component: SignUpView
        },
        {
            path: '/articlecreated',
            name: 'articlecreated',
            component: ArticleCreated
        },
        
    ]
})


router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const token = localStorage.getItem('authToken');
    const isAuthenticated = !!token; // Check if token exists and is truthy

    if (!isAuthenticated) {
      next('/login');
    } else {
      next(); 
    }
  } else {
    next(); 
  }
});


export default router