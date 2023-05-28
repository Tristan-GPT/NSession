import express from "express";
import cors from "cors";
import bodyparser from "body-parser";
import config from "./config.json"

const client = express()

client.use(express.json())
client.use(bodyparser.json())
client.use(cors())

client.listen(config.port, async () => {
    console.log(`[PyIronSession Logger] - Client est connecté au port ${config.port}`)
});

export default client;