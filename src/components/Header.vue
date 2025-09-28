<template>
  <header class="header">
    <div class="brand">
      <img class="logo" src="../assets/logo.png"/>
      <div>
        <div class="title">Mariage Elias et Tania</div>
        <div class="subtitle">25 avril 2026</div>
      </div>
    </div>
    <nav class="nav">
      <a href="#inscription">S'inscrire</a>
      <router-link to="/admin">Admin</router-link>
    </nav>
  </header>
</template>

<script>
export default { name: 'Header' }
</script>