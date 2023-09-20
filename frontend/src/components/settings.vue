<script setup>
import {ref} from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios'

const logedIn = ref(true)
const createVisible = ref(true)
const route = useRoute();
const articleId = parseInt(route.params.id);

function deleteArticle() { 
  axios.delete(`http://127.0.0.1:8000/api/delete/${articleId}`)
};


function create()
{
    createVisible.value = !createVisible.value
    console.log(createVisible.value)
}

</script>

<template>
    <main>
        <div class="create" v-if="logedIn">
          <RouterLink to="../create/">
            <button class="createButton" @click="create" > Create Article </button>
          </RouterLink>
              
              <button class="createButton" @click="create" :createVisible="createVisible"> Edit Article </button>
              <a :href="`/article/${articleId}`" class="createButton" @click="deleteArticle" :createVisible="createVisible"> Delete Article </a>
        </div>
    </main>
</template>

<style scoped>

.create { 
    display: flex;
    justify-content: center;
    margin: 1em;
}




/* create button css */
.createButton {
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
  margin: 0em 1em;
}

.createButton:disabled {
  pointer-events: none;
}

.createButton:hover {
  box-shadow: rgba(0, 0, 0, 0.25) 0 8px 15px;
  transform: translateY(-2px);
}

.createButton:active {
  box-shadow: none;
  transform: translateY(0);
}

</style>