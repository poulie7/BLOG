<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';
import Editor from '@tinymce/tinymce-vue'
import settings from '../components/settings.vue'
import editForm from '../components/editform.vue'
import {defineProps} from 'vue'

const article = ref([]); 
const articles = ref([]);
const route = useRoute();
const articleId = parseInt(route.params.id);
const {createVisible} = defineProps(['createVisible'])


const getPosts = async () => {
    try {
        const response = await axios({
            method: 'GET',
            url: 'http://127.0.0.1:8000/api',
        });
        return response.data; 
    } catch (error) {
        console.error('Error fetching articles:', error);
        return [];
    }
};


const findArticleById = (id) => {
    return articles.value.find(article => article.id === id);
};


onMounted(async () => {
    try {
        const fetchedArticles = await getPosts();
        articles.value = fetchedArticles; 

        article.value = findArticleById(articleId);

    } catch (error) {
        console.error('Error in onMounted:', error);
    }
});
</script>

<template>
    
    <main>
        <settings/>
        <editForm v-if="createVisible"/>
        <div v-if="article">
            <h1>{{ article.article_header }}</h1>
        <div class="text">
            <p>{{article.article}}</p>
        </div>
        </div>
        <div v-else>
            <h1>No article found.</h1>
        </div>
        
        <editForm/>
        </main>
</template>

<style scoped>

h1{
    text-align: center;
    margin: 2em;
    text-transform: uppercase;
}
.text { 
    margin: 1em;
    text-indent: 50px;
    text-align: justify;
    border: 1px solid gray;
    padding: 8px;
}
</style>







