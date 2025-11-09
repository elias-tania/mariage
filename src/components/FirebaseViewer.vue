<template>
  <div class="responses-container">
    <h2>📋 Liste des inscriptions</h2>

    <!-- Filtres -->
    <div class="filters">
      <input
        type="text"
        v-model="searchName"
        placeholder="Filtrer par nom..."
      />
      <select v-model="filterAttending">
        <option value="">Tous</option>
        <option value="yes">Viendra</option>
        <option value="no">Ne viendra pas</option>
      </select>
    </div>

    <!-- Tableau -->
    <table class="responses-table">
      <thead>
        <tr>
          <th>Nom</th>
          <th>Présence</th>
          <th>Avec</th>
          <th>Cérémonie</th>
          <th>Repas</th>
          <th>Menu</th>
          <th>Allergies</th>
          <th>Message</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(response, key) in filteredResponses"
          :key="key"
        >
          <td>{{ response.name }}</td>
          <td>
            <span v-if="response.attending === 'yes'">✅</span>
            <span v-else>❌</span>
          </td>
          <td>{{ response.affiliation || '-' }}</td>
          <td>
            <span v-if="response.ceremonie">✅</span>
          </td>
          <td>
            <span v-if="response.repas">✅</span>
          </td>
          <td><span v-if="response.noViande">❌</span>🥩 | <span v-if="response.noPoisson">❌</span>🐟</td>
          <td>{{ response.allergies || '-' }}</td>
          <td>{{ response.message || '-' }}</td>
        </tr>
      </tbody>
    </table>

    <div v-if="loading" class="loading">⏳ Chargement...</div>
    <div v-if="error" class="error">{{ error }}</div>
  </div>
</template>

<script>
export default {
  name: "ResponsesTable",
  data() {
    return {
      responses: [],
      loading: true,
      error: null,
      searchName: "",
      filterAttending: ""
    }
  },
  computed: {
    filteredResponses() {
      return this.responses.filter(r => {
        const matchesName = r.name.toLowerCase().includes(this.searchName.toLowerCase())
        const matchesAttending = this.filterAttending
          ? r.attending === this.filterAttending
          : true
        return matchesName && matchesAttending
      })
    }
  },
  async mounted() {
    try {
      const base_url = import.meta.env.VITE_BASE_URL
      const res = await fetch(base_url)
      if (!res.ok) throw new Error("Erreur réseau " + res.status)

      const data = await res.json()
      // Si c’est un objet, on transforme en tableau
      this.responses = Array.isArray(data) ? data : Object.values(data)
    } catch (err) {
      this.error = err.message
    } finally {
      this.loading = false
    }
  }
}
</script>
