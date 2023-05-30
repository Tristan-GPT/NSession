const express = require("express");
const cors = require("cors");
const bodyparser =  require("body-parser");
const config = require("./config.json")

const client = express()

client.use(express.json())
client.use(bodyparser.json())
client.use(cors())

client.listen(config.port, async () => {
    console.log(`[PyIronSession Logger] - Client est connecté au port ${config.port}`)
});

export default client;