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
  </main>
    <Footer/> 
</template>

<style scoped>

.container { 
  min-height: 100vh;
}

</style>