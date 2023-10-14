import { serve } from '@hono/node-server'
import { Hono } from 'hono'

const app = new Hono()

app.get('/', (c) => c.text('Hello Hono!'))
app.get('/api/hello', (c) => {
    return c.json({
        ok : true,
        message : "Returning Json",
    })
})


serve({
    fetch: app.fetch,
    port: 8787,
})
