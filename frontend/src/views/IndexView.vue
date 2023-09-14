<script setup>
import Card from '../components/Card.vue'
import {ref, onMounted} from 'vue'
import axios from 'axios';
import { useInfiniteScroll } from '@vueuse/core'


//  Fetching data from database
const articles = ref([]);
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

onMounted(async () => {
    try {
        const fetchedArticles = await getPosts();
        const shortArticleList = fetchedArticles.slice(0,24);
        articles.value = shortArticleList; // Assign the fetched articles to the ref
    } 
    catch (error) {
        console.error('Error in onMounted:', error);
    }
});

</script>

<template>
    <div class="card-container" id="cards-container"> 
      <Card v-for="article in articles" :key="article.id" :article="article"/>
    </div>
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
  }
}
</style>