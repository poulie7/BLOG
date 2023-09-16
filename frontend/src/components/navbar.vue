<script setup>
    import {RouterLink} from 'vue-router'
    import {ref} from 'vue'
    import settings from '../components/settings.vue'
   
 
</script>

<template>   
   <header>
        <nav>
            <ul class="navigation">
                <div class="page_navigation">
                    <li><RouterLink active-class="active" to='/'>Home</RouterLink></li>
                    <li><RouterLink active-class="active" to='/articles'>Articles</RouterLink></li>
                    <li><RouterLink active-class="active" to='/about'>About</RouterLink></li>
                    <li><RouterLink active-class="active" to='/create'>Create post</RouterLink></li>
                </div>
                <div class="user_navigation">
                    <li><RouterLink active-class="active" to='/signup'>Sign Up</RouterLink></li>
                    <li><RouterLink active-class="active" to='/login'>Login</RouterLink></li>
                    <li><RouterLink active-class="active" to='/logout'>Logout</RouterLink></li>
                </div>
            </ul>
        </nav>
    </header>
      
      <settings/>
</template>

<style scoped>

.active {
    font-weight: 900;
}

header {
    background-color: black;   
    padding: 1em;
}

a {
    text-decoration: none;
    color: white;
}

a:hover {
    color: rgb(201, 185, 185);

}

.navigation li {
    list-style-type: none;
    padding: 1em;
}

.navigation {
    display: flex;
    justify-content: space-between;
}

.page_navigation {
    display: flex;
}

.user_navigation { 
    display: flex;
}





</style>