<script setup>
import Card from '../components/Card.vue'
import axios from 'axios'
import {ref, onMounted} from 'vue'
import createForm from '../components/createForm.vue'

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