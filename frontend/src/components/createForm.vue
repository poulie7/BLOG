<script setup>
import axios from 'axios'
import {ref, onMounted} from 'vue'
import Editor from '@tinymce/tinymce-vue'
const articleHeader = ref("");
const articleContent = ref("");
const articleCategory = ref("");

function  submitPost() {
  const token = localStorage.getItem('authToken');
  console.log(token)
  axios.post('http://127.0.0.1:8000/api/create/',{
    article_header: articleHeader.value,
    article: articleContent.value,
    article_categorie: articleCategory.value,
  }, {
            headers: {
                Authorization: `Token ${token}`,
            },
        });
};



</script>



<template>
    <main>
        <h1>Create Post</h1>
        <div class="createFormContainer">
            <form method="post" class="createForm" >
                <label for="articleHeaderInput"></label>
                <input type="text" id="articleHeaderInput" v-model="articleHeader" placeholder="Article Header" required :articleHeader="articleHeader">
                <Editor id="editor" api-key="aa17q26lds0pcwb2mx5piir1xy1jfj51h2nn4mnvdcn82g4v" v-model="articleContent" :articleContent="articleContent"> </Editor>
                <label for="articleCategorySelect">Article Category</label>
                <select name="" id="articleCategorySelect" v-model="articleCategory" required :articleCategory="articleCategory">
                    <option value="1">Categorie 1</option>
                    <option value="3">Categorie 2</option>
                    <option value="4">Categorie 3</option>
                    <option value="5">Categorie 4</option>
                    <option value="6">Categorie 5</option>
                </select>
            </form>
            <RouterLink to="/articles" class="createButton" @click="submitPost"> SUBMIT </RouterLink>

        </div>
    </main>
</template>

<style scoped >
main { 
    text-align: center;
}
h1 { 
    margin: 2em;
}


.createForm { 
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 50%;
}

.createFormContainer { 
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
   
}

#articleHeaderInput { 
    height: 2em;
    width: 75%;
}

#editor { 
    width: 75%;
}

#articleCategorySelect {
    width: 75%;
}

/* button css */
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
  margin: 1em;
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