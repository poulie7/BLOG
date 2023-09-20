<script setup>


</script>

<template>
    <main>
        <h1>Your article was changed</h1>
        <div class="content">
            <p>You have succesfuly changed your article. You can return Home
            <RouterLink to="/">HERE</RouterLink>
            </p>
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