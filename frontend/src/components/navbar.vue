<script>
    import {RouterLink} from 'vue-router'
</script>

<template>   
   <header>


        <nav>
            <ul class="nav_links">
                <li><RouterLink active-class="active" to='/'>Home</RouterLink></li>
                <li><RouterLink active-class="active" to='/about'>About</RouterLink></li>
            </ul>

        </nav>
        <input id='search' type="text" placeholder="Search">
    </header>
</template>

<style scoped>
.active {
    font-weight: 900;

}
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
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
#logo {
    height: 50px;
}

.nav_links li {
    list-style-type: none;
    padding: 1em;

}

.nav_links {
    display: flex;
}

#search {

    padding: 6px;
    border: none;
    margin-top: 8px;
    margin-right: 16px;
    font-size: 17px;
    border-radius: 50px;
}
</style>