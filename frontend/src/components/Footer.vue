<script>

</script>

<template>
    <main>
        <footer class='footer'>
        <div class="footer_menu">
            <ul>
                <li> <a href="">Link 1</a> </li>
                <li> <a href="">Link 2</a> </li>
                <li> <a href="">Link 3</a> </li>
            </ul>
            <ul>
                <li> <a href="">Link 1</a> </li>
                <li> <a href="">Link 2</a> </li>
                <li> <a href="">Link 3</a> </li>
            </ul>
            <ul>
                <li> <a href="">Link 1</a> </li>
                <li> <a href="">Link 2</a> </li>
                <li> <a href="">Link 3</a> </li>
            </ul>
        </div>
        <span class="copywrite">Copywrite Pavel Lexmaul 2023</span>
    </footer>
    </main>
</template>

<style scoped>
    .footer{
    color: white;
    background-color: black;
    display: flex;
    flex-direction: column;
    align-items: center;
    }

    .footer_menu { 
    display: flex;
    width: 100vw;
    text-align: center;
    justify-content: space-evenly;
    padding: 0.5em;
    }

    .footer ul li{
        list-style-type: none;
        padding: 0.5em; 
    }

    .copywrite {
        margin: 1em;
    }

</style>