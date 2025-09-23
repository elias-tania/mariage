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
        <input v-model="form.ceremonie" type="checkbox"></input> La cérémonie
        <input v-model="form.repas" type="checkbox"></input> Le repas
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
      <textarea v-model="form.allergies" placeholder="Notez is vous avez des allergies ou des choses que vous ne pouvez pas manger." />
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
  name: 'RegisterForm',
  data() {
    return {
      form: {
        name: '',
        attending: 'yes',
        guests: 0,
        menu: 'standard',
        message: ''
      },
      status: ''
    }
  },
  methods: {
    async handleSubmit() {
      this.status = 'Envoi en cours...'

      try {
        const resp = await fetch('/api/inscriptions', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.form)
        })

        if (!resp.ok) throw new Error('Erreur réseau')

        this.status = 'Merci ! Votre inscription a bien été reçue.'
      } catch (err) {
        this.status = 'Impossible d\'envoyer le formulaire. Réessayez plus tard.'
        console.error(err)
      }
    },

    async createDoodle() {
      this.status = 'Ouverture des créneaux...'
      try {
        const resp = await fetch('/api/doodle/create-poll', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ title: 'Disponibilités mariage', choices: [ '12 Jul 2026 15:00', '13 Jul 2026 18:00' ] })
        })

        if (!resp.ok) throw new Error('Erreur création Doodle')

        const data = await resp.json()
        if (data && data.url) window.open(data.url, '_blank')
        this.status = ''
      } catch (err) {
        this.status = 'Impossible d\'accéder à Doodle pour le moment.'
        console.error(err)
      }
    }
  }
}
</script>