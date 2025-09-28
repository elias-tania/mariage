<template>
  <form class="card form" @submit.prevent="handleSubmit">
    <!-- Sélection du nom ou "Autre" -->
    <label>
      Nom
      <select v-model="selectedName" required>
        <option v-for="p in participants" :key="p" :value="p">{{ p }}</option>
        <option value="other">Autre</option>
      </select>
    </label>

    <!-- Si "Autre" est sélectionné -->
    <div v-if="selectedName === 'other'">
      <label>
        Votre nom complet
        <input v-model="form.name" placeholder="Nom complet" required />
      </label>

      <label>
        Personne affiliée dans la liste
        <select v-model="form.affiliation" required>
          <option value="" disabled>Choisissez une personne</option>
          <option v-for="p in participants" :key="p" :value="p">{{ p }}</option>
        </select>
      </label>

      <label>
        Message obligatoire
        <textarea v-model="form.customMessage" placeholder="Un petit mot..." required />
      </label>
    </div>

    <label>
      Présence
      <select v-model="form.attending">
        <option value="yes">Je viendrai</option>
        <option value="no">Je ne peux pas</option>
      </select>
    </label>

    <div v-if="form.attending === 'yes'">
      <label>
        Je serai présent durant
        <div class="checkbox">
          <input v-model="form.ceremonie" type="checkbox" /> La cérémonie
          <input v-model="form.repas" type="checkbox" /> Le repas
        </div>
      </label>

      <label>
        Menu (préférence)
        <select v-model="form.menu">
          <option value="standard">Standard</option>
          <option value="vegetarian">Végétarien</option>
        </select>
      </label>

      <label>
        Allergies (optionnel)
        <textarea v-model="form.allergies" placeholder="Notez si vous avez des allergies ou des choses que vous ne pouvez pas manger." />
      </label>
    </div>

    <div class="actions">
      <button type="submit" class="btn">Envoyer</button>
    </div>

    <p v-if="status" class="status">{{ status }}</p>
  </form>
</template>

<script>
export default {
  name: "RegisterForm",
  data() {
    return {
      participants: [
        "Laurent Gajo", "Anne-Lise Gajo", "Roberto Tripiciano", "Corinne Tripiciano",
        "Matthias Gajo", "Coraline Gajo", "Elyo Gajo", "Nicolas Gajo",
        "Anais Gajo", "Andrea Gajo", "Daniela Olivera", "Marie Gajo",
        "Laura Tripiciano-Leo", "Jacopo Tripiciano-Leo",
      ],
      selectedName: "",
      form: {
        name: "", // utilisé si "Autre"
        attending: "no",
        ceremonie: false,
        repas: false,
        menu: "standard",
        allergies: "",
        affiliation: "",
        customMessage: ""
      },
      status: ""
    }
  },
  methods: {
    async handleSubmit() {
      // Validation si "Autre"
      if (this.selectedName === 'other' && (!this.form.name || !this.form.affiliation || !this.form.customMessage.trim())) {
        this.status = "❌ Merci de remplir votre nom, la personne affiliée et un message."
        return
      }

      this.status = "⏳ Envoi en cours..."

      const payload = { ...this.form }

      if (this.selectedName !== 'other') {
        payload.name = this.selectedName
        payload.affiliation = null
        payload.customMessage = null
      }

      try {
        const base_url = import.meta.env.VITE_BASE_URL
        const response = await fetch(base_url, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        })

        if (!response.ok) {
          throw new Error("Erreur serveur " + response.status)
        }

        this.status = "✅ Merci, votre réponse a été enregistrée !"

        // Réinitialiser le formulaire
        this.selectedName = ""
        this.form = {
          name: "",
          attending: "yes",
          ceremonie: false,
          repas: false,
          menu: "standard",
          allergies: "",
          affiliation: "",
          customMessage: ""
        }
      } catch (err) {
        this.status = "❌ Une erreur est survenue : " + err.message
      }
    }
  }
}
</script>
