<script setup>
import {ref, onMounted} from 'vue'
import Editor from '@tinymce/tinymce-vue'
const articleHeader = ref("");
const articleContent = ref("");
const articleCategory = ref("");

</script>



<template>
    <main>
        <div class="createFormContainer">
            <form method="post" class="createForm" >
                <input type="text" v-model="articleHeader">
                <Editor id="editor" api-key="aa17q26lds0pcwb2mx5piir1xy1jfj51h2nn4mnvdcn82g4v" v-model="articleContent"> </Editor>
                <select name="" id="" v-model="articleCategory">
                    <option value="1">1</option>
                    <option value="3">2</option>
                    <option value="4">3</option>
                    <option value="5">4</option>
                    <option value="6">5</option>
                </select>
                <button class="createButton" @click="submitPost"> SUBMIT </button>
            </form>
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

}
.createForm input { 
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


.createFormContainer { 
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
}


/* edit button css */
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