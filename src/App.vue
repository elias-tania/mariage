<template>
  <div class="site">
    <Header />
    <main class="container">
      <RouterView />
    </main>
    <footer class="footer">
      <p>Avec amour — <strong>Les futurs mariés</strong></p>
    </footer>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import { RouterView, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'

export default {
  name: 'App',
  components: { Header, RouterView },

  setup() {
    const page = ref(null)
    const router = useRouter() // <-- accède au router pour rediriger

    const updatePage = () => {
      const params = new URLSearchParams(window.location.search)
      page.value = params.get('page')

      if (page.value) {
        // Redirige vers la route correspondante, par exemple '/admin'
        router.push(`/${page.value}`).catch(() => {}) 
        // catch pour éviter les erreurs si la route est la même
      }
    }

    onMounted(() => {
      updatePage()
      // Pour gérer les changements d'URL avec les boutons du navigateur
      window.addEventListener('popstate', updatePage)
    })

    return { page }
  }
}
</script>
