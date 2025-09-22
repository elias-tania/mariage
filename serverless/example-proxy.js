// Exemple Node.js proxy serverless pour Doodle
/*
exports.handler = async (event) => {
  const body = JSON.parse(event.body || '{}')
  const DOODLE_TOKEN = process.env.DOODLE_TOKEN

  const createResp = await fetch('https://api.doodle.com/api/v2/polls', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${DOODLE_TOKEN}`
    },
    body: JSON.stringify({
      title: body.title
    })
  })

  const data = await createResp.json()

  return {
    statusCode: 200,
    body: JSON.stringify({ url: data.public_url || data.url || null })
  }
}
*/