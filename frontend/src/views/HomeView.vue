<script setup>
import Card from '../components/Card.vue'
import axios from 'axios'
import {ref, onMounted} from 'vue'
import createForm from '../components/createForm.vue'


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
    <main>
        <h1>Welcome to our Blog</h1>
        <div class="content">
            <p>Here are the latest post. All articles are available 
            under articles card.</p>
        </div>
       
        </main>
</template>

<style scoped>

main { 
    text-align: center;
}

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