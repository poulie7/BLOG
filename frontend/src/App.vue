<script setup>
import Nav from './components/navbar.vue'
import Footer from './components/Footer.vue'
import  { useInfiniteScroll } from '@vueuse/core'
import { RouterView } from 'vue-router'
</script>

<template>
  <main class="container">
    <Nav/> 
<RouterView/>
    <!-- <RouterView /> -->
   
  </main>

  <Footer/> 
</template>

<style>

.container { 
  min-height: 100vh;
}

.card-container {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  margin-top: 5em;
}
</style>