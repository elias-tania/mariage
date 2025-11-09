<template>
  <form class="form" @submit.prevent="handleSubmit" @keydown.enter.prevent>
    <!-- Sélection du nom -->
    <label>
      Nom
      <ComboBox
        v-model="selectedName"
        :options="participants"
        placeholder="Entrez votre nom"
        @update:modelValue="fetchByName"
      />
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
import ComboBox from './ComboBox.vue'

export default {
  name: "RegisterForm",
  components: { ComboBox },
  data() {
    return {
      participants: [
        "Elias Gajo", "Anne-Lise Gajo", "Anais Gajo", "Marie Gajo", "Nicolas Gajo", "Andrea Gajo", "Matthias Gajo", "Corinne Tripiciano", "Laura Tripiciano Leo", "Daniel Crot", "Sébastien Crot", "Eliasabeth Crot", "Chloé Leibundgut", "Jeremy Leibundgut", "Romain Gajo", "Adrien Gajo", "Joyce Ducommun", "Whitney Ducommun", "Bastien Gajo", "Mylena Gajo", "Caroline Tripiciano", "Luca Auteri", "Gabriel Ciullo", "Vincet Tripiciano", "Stefano Tripiciano", "Sandra Tripiciano", "Alain Praz", "Laurent Praz", "Leticia Praz", "Santa Tripiciano", "Madeleine Praz", "Michel Crot", "Lino Gajo", "Damien Bousquet", "Eliot Bovey", "Stéphane Borel", "Melika Borel", "Constantin Bacha", "Floriane Bacha", "Nora Bacha", "Antonio Di Dio", "Davide Di Dio", "Noemi Di Dio", "Marco Bearzi", "Martine Monney", "Eleonore Fleury", "Yasmin Koubaa", "Coralie Amez-Droz", "Luca Meyer", "Matthieu Volet", "Sylvie Gonçalves", "Diana Gonçalves", "Catia Niderhauser", "Cédric Niderhauser", "Danny Niderhauser", "Typhanie Niderhauser", "Dereck Crevoisier", "Morgan Crevoisier", "Bryan Crevoisier", "Philipe Crevoisier", "Clara Gajo", "Carmela Sgrò", "Remo Sgrò", "Pippo Sgrò", "Marlyse Reith",
        "Tania Tripiciano", "Laurent Gajo", "Daniela Oliveira", "Coraline Gajo", "Roberto Tripiciano", "Jacopo Tripiciano Leo", "Chantal Crot", "Julie (copine de Sébastien)", "Micheline Ducommun", "Luigi Auteri", "Giada (copine de Luca)", "Joëlle (copine de Gabriel)", "Loris Tripiciano", "Claudia Tripiciano", "Hugo Martinez", "Anna Praz", "Christiane Praz", "Nick (copain de Leticia)", "Edith Crot", "Malou (copine de Lino)", "Masha (copine de Damien)", "Antonietta Di Dio", "Léa (copine de Davide)", "Elba Xheladini", "-", "Aurélie Volet", "Loic (copain de Sylvie)", "Quentin (copain de Diana)", "Pierrick Niderhauser", "Viviane Crevoisier",
        "Elyo Gajo", "Valentina (enfant de Stefano et Claudia)", "Leandro Martinez", "Santiago Martinez", "Julie (enfant de Leticia et Nick)", "Aquilian (enfant de Noemie et Elba)", "Jade (enfant de Matthieu et Aurelie)"
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

        this.status = `✅ Merci, ${this.selectedName}`

        const successMessage = `✅ Merci ${this.selectedName} ! ta réponse a bien été enregistrée !`
        this.$router.push({ path: "/", query: { message: successMessage } })

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
