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
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMDIyNjgzOCwianRpIjoiMmM2NjU1YTgtNzc0MC00OWFiLWJhNTQtYzZiNGM5MGU5NjEzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJAZ21haWwuY29tIiwibmJmIjoxNzIwMjI2ODM4LCJjc3JmIjoiZTgzNWNjZmUtODA2Mi00MTRjLWJmOWMtZWNmOTg4ZTdlYTIyIiwiZXhwIjoxNzIwMzEzMjM4fQ.-dPRlRi3UMkBZeHYIWJtZ0vab5VJIrLIUv-9Eex8mt4',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMDIyNjg3MSwianRpIjoiODljNDQxNDQtMTM4My00Y2M2LTlkZGYtY2JhNGFlMWZmZDg1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXIxQGdtYWlsLmNvbSIsIm5iZiI6MTcyMDIyNjg3MSwiY3NyZiI6IjAyY2IxN2RiLTFkMmYtNDUzNC1iY2U2LTJkOGFlMzRmOTdiOCIsImV4cCI6MTcyMDMxMzI3MX0.izHnnek7D8OP5sV-j-ram10Cuwz_oSDHXp8Yybodw8Q',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMDIyNjkxMywianRpIjoiNmEyNzUzY2EtYjYzOS00ZDk1LWFjNTMtNTU4NzFjNDQxMjU0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImxhbW90dGVseW1vaGFtZWRAZ21haWwuY29tIiwibmJmIjoxNzIwMjI2OTEzLCJjc3JmIjoiMDJhY2M0NGYtZTJkZC00NDRkLWFjMTctMjlmYzY3ODc5ZmZjIiwiZXhwIjoxNzIwMzEzMzEzfQ.gpjcRzsEa3SjNyf1jNT9BqbW9z86zF25wgOPTY9GD1I',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMDIyNjk0NiwianRpIjoiODI1ZGY1ZDYtNmRiNS00ZDVjLTk0NTUtMjk3ZDE1Mjc5NmFhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Im91c21hbmVjb2x5NTQzQGdtYWlsLmNvbSIsIm5iZiI6MTcyMDIyNjk0NiwiY3NyZiI6IjFmOGQ4MjA2LTY3MzgtNDE4ZS05YzA0LTNjY2Y1NjIxYmRmOSIsImV4cCI6MTcyMDMxMzM0Nn0.9QfkiwLxPseX1On-JTy8riy0tZDXAqaovGm_3o6Pb04'
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
