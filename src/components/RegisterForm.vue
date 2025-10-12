<template>
  <form class="form" @submit.prevent="handleSubmit">
    <!-- Sélection du nom -->
    <label>
      Nom
      <input
        type="text"
        v-model="selectedName"
        list="participants-list"
        @input="fetchByName"
        required
      />
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
      <div v-if="!participants.includes(selectedName) && selectedName !== ''">
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
        À la cérémonie
      </label>

      <label class="checkbox">
        <input type="checkbox" v-model="form.repas" />
        Au repas
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
          placeholder="Notez vos allergies ou restrictions alimentaires"
        ></textarea>
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
      responses: [],
      selectedName: "",
      form: {
        name: "",
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
      if (!this.selectedName) {
        this.status = "Tu n'as pas indiqué ton nom."
        return
      }

      if (!this.participants.includes(this.selectedName) && !this.form.affiliation) {
        this.status = "Tu as oublié de nous dire la personne que tu accompagnes."
        return
      }

      this.status = "⏳ Envoi en cours..."

      const payload = { ...this.form, name: this.selectedName }

      try {
        const base_url = import.meta.env.VITE_BASE_URL
        const response = await fetch(base_url, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        })

        if (!response.ok) throw new Error("Erreur serveur " + response.status)

        this.status = `✅ Merci, ${this.selectedName}, votre réponse a été enregistrée !`

        this.selectedName = ""
        Object.assign(this.form, {
          name: "",
          attending: "no",
          ceremonie: false,
          repas: false,
          menu: "standard",
          allergies: "",
          affiliation: "",
          customMessage: ""
        })
      } catch (err) {
        this.status = "❌ Une erreur est survenue : " + err.message
      }
    },

    /** Remplissage automatique du formulaire depuis la DB **/
    fetchByName() {
      const guest = this.responses.findLast(el => el.name === this.selectedName)

      if (!guest) {
        // reset propre (réactif)
        Object.assign(this.form, {
          name: "",
          attending: "no",
          ceremonie: false,
          repas: false,
          menu: "standard",
          allergies: "",
          affiliation: "",
          customMessage: ""
        })
        return
      }

      // Remplit chaque champ de manière réactive
      Object.assign(this.form, {
        name: guest.name || "",
        attending: guest.attending || "no",
        ceremonie: !!guest.ceremonie,
        repas: !!guest.repas,
        menu: guest.menu || "standard",
        allergies: guest.allergies || "",
        affiliation: guest.affiliation || "",
        customMessage: guest.customMessage || ""
      })
    }
  },

  async mounted() {
    try {
      const base_url = import.meta.env.VITE_BASE_URL
      const res = await fetch(base_url)
      if (!res.ok) throw new Error("Erreur réseau " + res.status)
      const data = await res.json()
      this.responses = Array.isArray(data) ? data : Object.values(data)
    } catch (err) {
      this.status = "Erreur de chargement : " + err.message
    }
  }
}
</script>
