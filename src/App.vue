<template>
  <div class="site">
    <Header />
    <ClustersList />

    <main class="container">
      <section class="hero">
        <div class="hero-content">
          <h1>Vous êtes invité·e</h1>
          <p>Nous serions ravis de vous compter parmi nous pour célébrer avec nous. Merci de confirmer votre présence grâce au formulaire ci dessous</p>
          <a class="btn" href="#inscription">Répondre</a>
        </div>
        <div class="hero-side">
          <RegistryCard />
        </div>
      </section>

      <section id="inscription" class="form-section">
        <h2>Formulaire d'inscription</h2>
        <RegisterForm />
      </section>

      <footer class="footer">
        <p>Avec amour — <strong>Les futurs mariés</strong></p>
      </footer>
    </main>
  </div>
</template>

<script>
import ClustersList from './components/ClustersList.vue';
import Header from './components/Header.vue'
import RegisterForm from './components/RegisterForm.vue'
import RegistryCard from './components/RegistryCard.vue'

export default {
  name: 'App',
  components: { Header, RegisterForm, RegistryCard, ClustersList }
}
</script>