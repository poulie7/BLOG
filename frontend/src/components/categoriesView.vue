<script setup>

</script>

<template>
    <main>
        <div class="categories">
            <RouterLink to="/" style="text-decoration: none">categorie 1</RouterLink>
            <RouterLink to="/" style="text-decoration: none">categorie 2</RouterLink>
            <RouterLink to="/" style="text-decoration: none">categorie 3</RouterLink>
            <RouterLink to="/" style="text-decoration: none">categorie 4</RouterLink>
            <RouterLink to="/" style="text-decoration: none">categorie 5</RouterLink>
        </div>
    </main>
</template>

<style scoped>

.categories { 
    display: flex;
    justify-content: space-evenly;
    text-align: center;
}
.categories a { 
    color: black;
    margin: 2em;
    border: 1px solid black;
    border-radius: 30px;
    padding: 0.2em;

}


.categories a:hover {
  box-shadow: rgba(0, 0, 0, 0.25) 0 8px 15px;
  transform: translateY(-2px);
}

</style>