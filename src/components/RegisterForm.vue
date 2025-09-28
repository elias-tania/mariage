<template>
  <form class="card form" @submit.prevent="handleSubmit">
    <datalist id="participants">
      <option value="Laurent Gajo"></option>
      <option value="Anne-Lise Gajo"></option>
      <option value="Roberto Tripiciano"></option>
      <option value="Corinne Tripiciano"></option>
      <option value="Matthias Gajo"></option>
      <option value="Coraline Gajo"></option>
      <option value="Elyo Gajo"></option>
      <option value="Nicolas Gajo"></option>
      <option value="Anais Gajo"></option>
      <option value="Andrea Gajo"></option>
      <option value="Daniela Olivera"></option>
      <option value="Marie Gajo"></option>
      <option value="Laura Tripiciano-Leo"></option>
      <option value="Jacopo Tripiciano-Leo"></option>
    </datalist>

    <label>
      Nom
      <input v-model="form.name" list="participants" id="participant" name="participant" required />
    </label>

    <label>
      Présence
      <select v-model="form.attending">
        <option value="yes">Je viendrai</option>
        <option value="no">Je ne peux pas</option>
      </select>
    </label>

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
      <textarea
        v-model="form.allergies"
        placeholder="Notez si vous avez des allergies ou des choses que vous ne pouvez pas manger."
      />
    </label>

    <label>
      Message (optionnel)
      <textarea v-model="form.message" placeholder="Un petit mot..." />
    </label>

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
      form: {
        name: "",
        attending: "yes",
        ceremonie: false,
        repas: false,
        menu: "standard",
        allergies: "",
        message: ""
      },
      status: ""
    }
  },
  methods: {
    async handleSubmit() {
      this.status = "⏳ Envoi en cours..."

      try {
        var base_url = import.meta.env.VITE_BASE_URL

        const response = await fetch(base_url, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.form)
        })

        if (!response.ok) {
          throw new Error("Erreur serveur " + response.status)
        }

        this.status = "✅ Merci, votre réponse a été enregistrée !"

        // Réinitialiser le formulaire
        this.form = {
          name: "",
          attending: "yes",
          ceremonie: false,
          repas: false,
          menu: "standard",
          allergies: "",
          message: ""
        }
      } catch (err) {
        this.status = "❌ Une erreur est survenue : " + err.message
      }
    }
  }
}
</script>
