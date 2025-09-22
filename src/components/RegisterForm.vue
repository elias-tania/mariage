<template>
  <form class="card form" @submit.prevent="handleSubmit">
    <label>
      Nom complet
      <input v-model="form.name" required placeholder="Jean Dupont" />
    </label>

    <label>
      Présence
      <select v-model="form.attending">
        <option value="yes">Je viendrai</option>
        <option value="no">Je ne peux pas</option>
        <option value="maybe">Peut-être</option>
      </select>
    </label>

    <label>
      Nombre d'invités
      <input type="number" min="0" v-model.number="form.guests" />
    </label>

    <label>
      Menu (préférence)
      <select v-model="form.menu">
        <option value="standard">Standard</option>
        <option value="vegetarian">Végétarien</option>
        <option value="vegan">Vegan</option>
        <option value="glutenfree">Sans gluten</option>
      </select>
    </label>

    <label>
      Message (optionnel)
      <textarea v-model="form.message" placeholder="Un petit mot..." />
    </label>

    <div class="actions">
      <button type="submit" class="btn">Envoyer</button>
      <button type="button" class="btn ghost" @click="createDoodle">Voir créneaux Doodle</button>
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