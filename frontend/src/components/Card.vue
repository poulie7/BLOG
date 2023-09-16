<script setup>

import {defineProps} from 'vue'
import {RouterLink} from 'vue-router'
const {article} = defineProps(['article'])

</script>


<template>
    
    <div class="card">
        <RouterLink :to="`/article/${article.id}`" style="text-decoration: none;">
            <div class="cards-content">
                <h1>{{ article.article_header }}</h1>
                <p>{{ article.article }}</p>
            </div>
        </RouterLink>
    </div>
</template>

<style scoped>


.cards-content {
    width: 100%;
    height: 100%;
    color: black;
}
.card{
    width: 310px;
    height: 300px;
    border-radius: 10px;
    box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
    overflow: hidden;
    margin: 2em;
 
}

h1 {
    text-align: center;
    margin-top: 1em;
    margin-bottom: 0.5em;

}

p {

text-align: justify;
padding: 1em;

}
</style>