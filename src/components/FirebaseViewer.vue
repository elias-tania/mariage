<template>
  <div class="p-4">
    <h2 class="text-xl font-bold mb-2">📋 Liste des réponses</h2>

    <div v-if="loading">⏳ Chargement...</div>
    <div v-else-if="error" class="text-red-500">{{ error }}</div>

    <ul v-else class="space-y-2">
      <li
        v-for="(response, key) in responses"
        :key="key"
        class="border p-2 rounded"
      >
        <strong>{{ response.name }}</strong>
        <span v-if="response.attending === 'yes'"> ✅ viendra</span>
        <span v-else> ❌ ne viendra pas</span>
        <br />

        <span v-if="response.ceremonie">🎉 Cérémonie</span>
        <span v-if="response.repas"> 🍽 Repas</span>
        <br />

        <span>Menu : {{ response.menu }}</span><br />

        <span v-if="response.allergies">
          ⚠️ Allergies : {{ response.allergies }}
        </span>
        <br />

        <span v-if="response.message">
          💌 Message : {{ response.message }}
        </span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "FireBaseViewer",
  data() {
    return {
      responses: {},
      loading: true,
      error: null
    }
  },
  async mounted() {
    try {
      var base_url = import.meta.env.VITE_BASE_URL
      const res = await fetch(base_url)
      if (!res.ok) throw new Error("Erreur réseau " + res.status)

      const data = await res.json()
      this.responses = data || {}
    } catch (err) {
      this.error = err.message
    } finally {
      this.loading = false
    }
  }
}
</script>
