<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';
import Editor from '@tinymce/tinymce-vue'



const article = ref([]); // Initialize as null since we're looking for a single article
const articles = ref([]);
const route = useRoute();
const articleId = parseInt(route.params.id);
const editFieldVisible = ref(false);
const articleHeader = ref("");
const articleContent = ref("");
const articleCategory = ref("");


function  submitPost() {
  axios.post('http://127.0.0.1:8000/api/edit/',{
    article_header: articleHeader.value,
    article: articleContent.value,
    article_categorie: articleCategory.value,
  });
};





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


function edit() {
    editFieldVisible.value = !editFieldVisible.value;
}


onMounted(async () => {
    try {
        const fetchedArticles = await getPosts();
        articles.value = fetchedArticles; 

        // Find the article with the matching ID
        article.value = findArticleById(articleId);

    } catch (error) {
        console.error('Error in onMounted:', error);
    }
});


</script>

<template>
    <main>
        <h1>{{ article.article_header }}</h1>
        <div class="text">
            <p>{{article.article}}</p>
        </div>
        <div class="editFormContainer">
            <button class="editButton" @click="edit"> EDIT </button>
            <form method="post" class="editForm">
             
                <input type="text" v-model="articleHeader">
                <input type="text" v-model="articleContent">
                <select name="" id="" v-model="articleCategory">
                    <option value="1">1</option>
                    <option value="3">2</option>
                    <option value="4">3</option>
                    <option value="5">4</option>
                    <option value="6">5</option>
                </select>
            </form>
            <!-- <Editor v-if="editFieldVisible" v-model="message"/> -->
            <button class="editButton" @click="submitPost"> SUBMIT </button>
        </div>
        </main>
</template>

<style scoped>
.editForm { 
    display: flex;
    flex-direction: column;

}
.editForm input { 
    height: 5em;
    margin: 1em;
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


.editFormContainer { 
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
}


/* edit button css */
.editButton {
  appearance: none;
  background-color: #000000;
  border: 2px solid #1A1A1A;
  border-radius: 15px;
  box-sizing: border-box;
  color: #FFFFFF;
  cursor: pointer;
  display: inline-block;
  font-family: Roobert,-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";
  font-size: 16px;
  font-weight: 600;
  line-height: normal;
  margin: 0;
  min-height: 60px;
  min-width: 0;
  outline: none;
  padding: 16px 24px;
  text-align: center;
  text-decoration: none;
  transition: all 300ms cubic-bezier(.23, 1, 0.32, 1);
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  width: 10em;
  will-change: transform;
}

.editButton:disabled {
  pointer-events: none;
}

.editButton:hover {
  box-shadow: rgba(0, 0, 0, 0.25) 0 8px 15px;
  transform: translateY(-2px);
}

.editButton:active {
  box-shadow: none;
  transform: translateY(0);
}

</style>







