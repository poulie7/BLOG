<script setup>
import Card from '../components/categorieCard.vue'
import {ref, onMounted} from 'vue'
import axios from 'axios';
import categoriesComponent from '../components/categoriesView.vue'
import { useRoute } from 'vue-router';

const route = useRoute();
const articleId = parseInt(route.params.id);
const articles = ref([]);
const categorie = ref([]);

const getPosts = async () => {
    try {
        const response = await axios.get(
           'http://127.0.0.1:8000/api'
        );
        return response.data; // Return the fetched articles
    } catch (error) {
      
        console.error('Error fetching articles:', error);
        return []; // Return an empty array in case of error
    }
};

const findArticleByCategorie = (categorie) => {
    return articles.value.filter(article => article.article_categorie === categorie);
};

onMounted(async () => {
    try {
        const fetchedArticles = await getPosts();
        articles.value = fetchedArticles; // Assign the fetched articles to the ref
        categorie.value = findArticleByCategorie(articleId);
    } 
    catch (error) {
        console.error('Error in onMounted:', error);
    }
});

</script>

<template>
    <main>
        <categoriesComponent :change="findArticleByCategorie"/>
        <div class="card-container">
            <Card v-for="c in categorie" :key="c.id" :c="c"/>
        </div>
    </main>
</template>

<style scoped>

.card-container{
  display: flex;
  justify-content: space-evenly;
 flex-wrap: wrap;

}
@media screen and (max-width: 1200px) {
 .card-container{
    display: flex;
    flex-direction: column;
    align-items: center;
  }
}


</style>