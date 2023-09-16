<script>

</script>

<template>
    <main>
        <h1>Sign Up</h1>
    <div class="formContainer">
        <form>
            <div class="form-group">
                <label for="first-name">First Name:</label>
                <input type="text" id="first-name" name="first-name" required>
            </div>
            <div class="form-group">
                <label for="last-name">Last Name:</label>
                <input type="text" id="last-name" name="last-name" required>
            </div>
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-group">
                <button type="submit">Sign Up</button>
            </div>
        </form>
    </div>
        
    </main>
</template>

<style scoped>
h1{
    margin-top: 2em;
    margin-bottom: 1em;
}
main { 
    text-align: center;
}

.formContainer {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 2px solid #000000;
    border-radius: 10px;
    background-color: #ffffff;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
}

.form-group input {
    width: 100%;
    padding: 10px;
    border: 1px solid #000000;
    border-radius: 5px;
}

.form-group button {
    background-color: #000000;
    color: #ffffff;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

.form-group button:hover {
    background-color: #333333;
}

</style>