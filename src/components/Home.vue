<template>
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
</template>

<script>
import FirebaseViewer from './FirebaseViewer.vue';
import Header from './Header.vue'
import RegisterForm from './RegisterForm.vue'
import RegistryCard from './RegistryCard.vue'

export default {
  name: 'Home',
  components: { Header, RegisterForm, RegistryCard, FirebaseViewer }
}
</script>