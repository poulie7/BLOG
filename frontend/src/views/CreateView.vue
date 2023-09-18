<script setup>
import axios from 'axios'
import createForm from '../components/createForm.vue'
// const {articleContent} = defineProps(['articleContent']);

function  submitPost() {
  axios.post('http://127.0.0.1:8000/api/create/',{
    article_header: articleHeader.value,
    article: articleContent.value,
    article_categorie: articleCategory.value,
  });
};



</script>




<template>
    <main>
        <createForm/>
    </main>
</template>




<style scoped>

</style>