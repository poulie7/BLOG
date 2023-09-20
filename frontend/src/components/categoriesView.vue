<script setup>
import {ref, onMounted} from 'vue'
import axios from 'axios';
import {defineProps} from 'vue'


const {change} = defineProps(['change'])
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

const findArticleById = (id) => {
    return articles.value.find(article => article.id === id);
};

onMounted(async () => {
    try {
        const fetchedArticles = await getPosts();
        articles.value = fetchedArticles; // Assign the fetched articles to the ref
        categorie.value = findArticleById(1);
    } 
    catch (error) {
        console.error('Error in onMounted:', error);
    }
});


</script>

<template>
    <main>
        <div class="categories">
            <RouterLink to="../articles/" style="text-decoration: none" @click="change">All categories </RouterLink>
            <a href="../categorie/1" style="text-decoration: none" @click="change">categorie 1</a>
            <a href="../categorie/3" style="text-decoration: none" @click="change">categorie 2</a>
            <a href="../categorie/4" style="text-decoration: none" @click="change">categorie 3</a>
            <a href="../categorie/5" style="text-decoration: none" @click="change">categorie 4</a>
            <a href="../categorie/6" style="text-decoration: none" @click="change">categorie 5</a>
        </div>
    </main>
</template>

<style scoped>

.categories { 
    display: flex;
    justify-content: space-evenly;
    text-align: center;
}
.categories a { 
    color: black;
    margin: 2em;
    border: 1px solid black;
    border-radius: 30px;
    padding: 0.2em;

}


.categories a:hover {
  box-shadow: rgba(0, 0, 0, 0.25) 0 8px 15px;
  transform: translateY(-2px);
}

</style>