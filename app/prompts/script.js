const prompts = [
    {
        "title": "Création de personnage",
        "text": "Décrivez un personnage qui vient d'un monde de fantasy.",
        "tags": "fantasy, personnage, description"
    },
    {
        "title": "Scène de combat",
        "text": "Écrivez une scène de combat épique entre un chevalier et un dragon.",
        "tags": "combat, épique, chevalier, dragon"
    },
    {
        "title": "Dialogue intense",
        "text": "Imaginez un dialogue intense entre un détective et un suspect.",
        "tags": "dialogue, détective, suspect, tension"
    },
    {
        "title": "Monde futuriste",
        "text": "Décrivez une ville dans un monde futuriste en l'an 2200.",
        "tags": "futuriste, ville, science-fiction"
    },
    {
        "title": "Déclaration d'amour",
        "text": "Écrivez une déclaration d'amour émotive sous la pluie.",
        "tags": "romance, déclaration, amour, pluie"
    },
    {
        "title": "Rêve étrange",
        "text": "Racontez un rêve étrange et mystérieux.",
        "tags": "rêve, étrange, mystérieux"
    },
    {
        "title": "Première rencontre",
        "text": "Décrivez la première rencontre entre deux personnages qui tomberont amoureux.",
        "tags": "rencontre, amour, personnages"
    },
    {
        "title": "Aventure en mer",
        "text": "Écrivez une histoire d'aventure sur un bateau pirate.",
        "tags": "aventure, mer, pirate, bateau"
    },
    {
        "title": "Découverte scientifique",
        "text": "Imaginez une découverte scientifique révolutionnaire.",
        "tags": "découverte, science, révolutionnaire"
    },
    {
        "title": "Mystère à résoudre",
        "text": "Écrivez une enquête pour résoudre un mystère dans une petite ville.",
        "tags": "mystère, enquête, petite ville"
    },
    {
        "title": "Retour dans le temps",
        "text": "Racontez l'histoire d'une personne qui retourne dans le passé pour changer un événement.",
        "tags": "retour, passé, changement, histoire"
    },
    {
        "title": "Créature mythologique",
        "text": "Décrivez une rencontre avec une créature mythologique.",
        "tags": "créature, mythologique, rencontre"
    },
    {
        "title": "Apocalypse zombie",
        "text": "Écrivez une histoire se déroulant pendant une apocalypse zombie.",
        "tags": "apocalypse, zombie, survie"
    },
    {
        "title": "Secret de famille",
        "text": "Racontez l'histoire d'un secret de famille révélé.",
        "tags": "secret, famille, révélation"
    },
    {
        "title": "Vie extraterrestre",
        "text": "Imaginez une rencontre avec des extraterrestres.",
        "tags": "extraterrestre, rencontre, science-fiction"
    },
    {
        "title": "Héros du quotidien",
        "text": "Décrivez un héros du quotidien qui fait une différence dans sa communauté.",
        "tags": "héros, quotidien, communauté"
    },
    {
        "title": "Voyage interstellaire",
        "text": "Écrivez une aventure dans l'espace à bord d'un vaisseau interstellaire.",
        "tags": "espace, aventure, interstellaire, vaisseau"
    },
    {
        "title": "Renaissance magique",
        "text": "Imaginez un monde où la magie est réapparue après des siècles.",
        "tags": "magie, renaissance, monde"
    },
    {
        "title": "Évasion de prison",
        "text": "Racontez l'évasion d'un prisonnier de la prison la plus sécurisée au monde.",
        "tags": "évasion, prison, prisonnier"
    },
    {
        "title": "Compétition sportive",
        "text": "Décrivez une compétition sportive intense entre deux rivaux.",
        "tags": "compétition, sport, rivaux, intense"
    }
];

const apiUrl = 'http://127.0.0.1:5000';
const tokens = [
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTY2MjQ3MCwianRpIjoiNDQyMGQ2NDYtZTBmYi00YjhlLWFkYzItZmIwMWJjNTU1ZDM0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXIxQGdtYWlsLmNvbSIsIm5iZiI6MTcxOTY2MjQ3MCwiY3NyZiI6IjhlMTljZmMyLTBiNDctNGIxZC05YjIxLWM3ZmYyNDE5ZjE4YSIsImV4cCI6MTcyMDA5NDQ3MH0.KG163vkD2eocaHYAhdBvbLC1mlhZxnKwclr_GWaElok',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTY2MjQ4OCwianRpIjoiNDQwM2ZiNDEtNWJjMi00MmRhLTgwMWUtMmM0N2I1MDk5ZmM4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXIyQGdtYWlsLmNvbSIsIm5iZiI6MTcxOTY2MjQ4OCwiY3NyZiI6IjBjYjI4ZThjLTExZTEtNDI1OC05NGY2LWQ3NjMzODRlODJlMyIsImV4cCI6MTcyMDA5NDQ4OH0.6nQ1SGy3PpwiTFH_L8ZQ8DRIt3TssTFBP50e06xOSOg',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTY2MjUwMywianRpIjoiZTEwODczOWMtODk0ZC00ZWZhLTk2YmItNDNhMThkMmU3NDFjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXIzQGdtYWlsLmNvbSIsIm5iZiI6MTcxOTY2MjUwMywiY3NyZiI6ImU3ZTVmNTljLWZjNDktNGFmYS04MDA4LWM5ZjVlOTg3Y2I1MyIsImV4cCI6MTcyMDA5NDUwM30.7GKUsZOIJbcwiigWaDGJlo-e_HhepV0xSm5N45SJZ9M',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTY2MjU1OSwianRpIjoiNGFlZDBjM2MtNmNlMC00NWQ0LWEzNjEtODgyMjY3NjFmMjdlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXI0QGdtYWlsLmNvbSIsIm5iZiI6MTcxOTY2MjU1OSwiY3NyZiI6IjJiM2IwYzQ0LTg3NmUtNDA0ZC1iNjkyLWUwY2FmNmY2ZWM3NSIsImV4cCI6MTcyMDA5NDU1OX0.5FqQJ_Ti0-0uKBzxOZhHQw2OJw3KM3Af2k-csVh6-1k'
];

async function addPromptsForUser(userIndex) {
    const token = tokens[userIndex];

    for (let i = 0; i < prompts.length; i++) {
        const prompt = prompts[i];
        
        try {
            const response = await fetch(`${apiUrl}/prompts/new`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify(prompt)
            });

            if (response.ok) {
                console.log(`Prompt ${i + 1} added successfully for user ${userIndex + 1}`);
            } else {
                console.error(`Error adding prompt ${i + 1} for user ${userIndex + 1}: ${response.statusText}`);
            }
        } catch (error) {
            console.error(`Network error adding prompt ${i + 1} for user ${userIndex + 1}:`, error);
        }
    }
}

function addPromptsForAllUsers() {
    for (let userIndex = 0; userIndex < tokens.length; userIndex++) {
        addPromptsForUser(userIndex);
    }
}

addPromptsForAllUsers();
