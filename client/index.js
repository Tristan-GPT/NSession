const fs = require("fs");
const path = require("path");

const filePath = path.join(__dirname, "./config.json");

/**
 * @param {number} port 
 */
function setPORT(port) {
    fs.readFile(filePath, "utf8", (err, data) => {
        if (err) {
            console.error("Erreur lors de la lecture du fichier JSON :", err);
            return;
        }

        // Convertir le contenu JSON en objet JavaScript
        const env = JSON.parse(data);

        // Modifier la valeur de l'attribut "port"
        env.port = port;

        // Convertir l'objet JavaScript en JSON
        const updatedData = JSON.stringify(env, null, 2);

        // Écrire les modifications dans le fichier JSON
        fs.writeFile(filePath, updatedData, "utf8", err => {
            if (err) {
                console.error("Erreur lors de l'écriture du fichier JSON :", err);
                return;
            }

            console.log("Modification du port effectuée avec succès !");
        });
    });
}

module.exports.setPORT = setPORT