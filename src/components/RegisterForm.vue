<template>
  <form class="form" @submit.prevent="handleSubmit">
    <!-- Sélection du nom ou "Autre" -->
    <label>
      Nom
      <input type="text" v-model="selectedName" list="participants-list" required>
      </input>
      <datalist id="participants-list">
        <option v-for="p in participants" :key="p" :value="p"></option>
      </datalist>
    </label>

    

    <label>
      Présence
      <select v-model="form.attending">
        <option value="yes">Je viendrai</option>
        <option value="no">Je ne peux pas</option>
      </select>
    </label>

    <div v-if="form.attending === 'yes'">
      <!-- Si "Autre" est sélectionné -->
    <div v-if="!participants.includes(selectedName) && selectedName!=''">
      <label>
        Je viendrai avec
        <select v-model="form.affiliation">
          <option value="" disabled>Choisissez une personne</option>
          <option v-for="p in participants" :key="p" :value="p">{{ p }}</option>
        </select>
      </label>
    </div>
      <label class="checkbox">
        <input type="checkbox" v-model="form.ceremonie" /> 
        A La cérémonie
      </label>
      <label class="checkbox">
        <input type="checkbox" v-model="form.repas" /> 
        <div>Au repas</div>
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
        <textarea v-model="form.allergies" placeholder="Notez si vous avez des allergies ou des choses que vous ne pouvez pas manger."></textarea>
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
      if (this.selectedName === 'other' && !this.form.name) {
        this.status = "Tu n'as pas indiqué ton nom."
        return
      }

      if (this.selectedName === 'other' && !this.form.affiliation) {
        this.status = "Tu as oublier de nous dire la personne que tu acompagnes"
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

        this.status = "✅ Merci, " + this.selectedName + " votre réponse a été enregistrée !"

        // Réinitialiser le formulaire
        this.selectedName = ""
        this.form = {
          name: "",
          attending: "no",
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
