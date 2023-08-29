import { createRouter, createWebHistory } from "vue-router";
import IndexView from '../views/IndexView.vue'
import AboutView from '../views/AboutView.vue'
import ArticleView from '../views/Article.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'index',
            component: IndexView
        },
        {
            path: '/about',
            name: 'about',
            component:  AboutView
        },
        {
            path: '/article/:id',
            name: 'article',
            component: ArticleView
        }
    ]
})

export default router