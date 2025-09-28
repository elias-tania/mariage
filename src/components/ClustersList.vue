<template>
  <div>
    <h2>Clusters MongoDB Atlas</h2>
    <button @click="fetchClusters" :disabled="loading">
      {{ loading ? "Chargement..." : "Recharger" }}
    </button>

    <ul v-if="clusters.length">
      <li v-for="cluster in clusters" :key="cluster.id">
        <strong>{{ cluster.name }}</strong> — état : {{ cluster.stateName }}
      </li>
    </ul>

    <p v-else-if="!loading">Aucun cluster trouvé.</p>
    <p v-if="error" style="color:red;">Erreur: {{ error }}</p>
  </div>
</template>

<script>
export default {
  name: "ClustersList",
  data() {
    return {
      clusters: [],
      loading: false,
      error: null
    };
  },
  methods: {
    async fetchClusters() {
      this.loading = true;
      this.error = null;
      this.clusters = [];

      try {
        const publicKey = "lquhprku";
        const privateKey = "55dc81a2-1d6e-435d-a844-f18012646356";

        const auth = btoa(`${publicKey}:${privateKey}`);

        const resp = await fetch("https://cloud.mongodb.com/api/atlas/v2/clusters", {
          headers: {
            "Authorization": `Basic ${auth}`
          }
        });

        if (!resp.ok) {
          throw new Error(`Erreur API: ${resp.body}`);
        }

        const data = await resp.json();
        this.clusters = data.results || [];
      } catch (err) {
        this.error = err.message;
      } finally {
        this.loading = false;
      }
    }
  },
  mounted() {
    this.fetchClusters();
  }
};
</script>