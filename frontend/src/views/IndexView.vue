<script setup>
import Card from '../components/Card.vue'
import {ref, onMounted} from 'vue'
import axios from 'axios';
import categoriesComponent from '../components/categoriesView.vue'

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
        articles.value = fetchedArticles; // Assign the fetched articles to the ref
    } 
    catch (error) {
        console.error('Error in onMounted:', error);
    }
});

</script>

<template>
        <categoriesComponent/>

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
    align-items: center;
  }
}

/* categories componenet css */

.categories { 
    display: flex;
    justify-content: space-evenly;
    text-align: center;
}
.categories button { 
    color: black;
    margin: 2em;
    border: 1px solid black;
    border-radius: 30px;
    padding: 0.2em;

}


.categories button:hover {
  box-shadow: rgba(0, 0, 0, 0.25) 0 8px 15px;
  transform: translateY(-2px);
}
</style>