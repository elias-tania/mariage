<template>
  

    <RegisterForm />
</template>

<script>
import FirebaseViewer from './FirebaseViewer.vue';
import Header from './Header.vue'
import RegisterForm from './RegisterForm.vue'
import RegistryCard from './RegistryCard.vue'

export default {
  name: 'Inscritpion',
  components: { Header, RegisterForm, RegistryCard, FirebaseViewer }
}
</script>