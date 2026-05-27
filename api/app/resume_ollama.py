import os
import ollama

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
ollama_client = ollama.Client(host=OLLAMA_HOST)


def generer_resume_meteo(meteo, previsions=None, vigilance="aucune"):
    texte_previsions = ""

    for p in previsions or []:
        texte_previsions += (
            f"\n{p['jour']} {p['moment']} : "
            f"{p['temperature']}°C, "
            f"pluie {p['pluie_mm']} mm, "
            f"rafales {p['rafales_kmh']} km/h"
        )

    resume_meteo = f"""
Ville témoin : {meteo['ville']}
Vigilance Météo-France : {vigilance}

Aujourd'hui :
- Température : {meteo['temperature']}°C
- Pluie : {meteo['pluie_mm']} mm
- Rafales : {meteo['rafales_kmh']} km/h

Prévisions :
{texte_previsions}
"""

    prompt = f"""
Tu es un assistant météo français.

Rédige un résumé météo clair pour la ville témoin.

Règles STRICTES :
- Si vigilance Météo-France jaune, orange ou rouge : commence par "⚠️ ALERTE MÉTÉO FRANCE"
- Si température >= 32°C : parle de forte chaleur / canicule
- Si rafales < 50 km/h : ne parle pas de vent dangereux
- Si rafales >= 50 km/h : parle de vent sensible
- Si rafales >= 70 km/h : parle de vent fort
- Si rafales >= 90 km/h : parle de vents violents
- Si rafales >= 110 km/h : parle de tempête possible
- Si pluie >= 20 mm : parle de fortes pluies
- Si pluie >= 50 mm : parle de risque d'inondation
- Ne jamais parler de vents violents si les rafales sont inférieures à 90 km/h
- Ne jamais parler de tempête si les rafales sont inférieures à 110 km/h
- Ne jamais inventer un danger absent des données
- Mentionne aujourd'hui, J+1, J+2 et J+3
- Donne des conseils concrets
- Résumé en 6 à 8 lignes maximum
- Ne dis pas que tu es une IA
- N'invente aucune valeur absente

Données météo :

{resume_meteo}
"""

    response = ollama_client.generate(
        model="llama3.1:8b",
        prompt=prompt,
        options={"temperature": 0.2, "num_predict": 220},
    )

    return response["response"]
