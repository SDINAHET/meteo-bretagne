# # import ollama

# # resume_meteo = """
# # Prévision Bretagne - Rennes :
# # Température : 12°C
# # Pluie cumulée : 8 mm
# # Rafales : 62 km/h
# # Risque météo : modéré
# # """

# # response = ollama.chat(
# #     model="llama3.1:8b",
# #     messages=[
# #         {
# #             "role": "user",
# #             "content": f"""
# # Tu es un assistant météo français.
# # Explique simplement cette prévision météo pour un utilisateur :

# # {resume_meteo}
# # """
# #         }
# #     ]
# # )

# # print(response["message"]["content"])

# import ollama

# response = ollama.chat(
#     model="llama3.1:8b",
#     messages=[
#         {
#             "role": "user",
#             "content": f"""
# Tu es un assistant météo français.

# Rédige un résumé météo clair pour la ville témoin.

# Structure :
# 1. Météo actuelle
# 2. Prévisions J+1, J+2, J+3
# 3. Conseils pratiques
# 4. Alerte danger si nécessaire

# Règles d'alerte :
# - Si vigilance Météo-France orange ou rouge : commence par "⚠️ ALERTE MÉTÉO"
# - Si rafales > 70 km/h : conseille d'éviter les déplacements inutiles
# - Si pluie forte > 20 mm : signale un risque de ruissellement
# - Si température > 32°C : conseille hydratation, ombre, éviter efforts
# - Si aucun danger : indique simplement que la situation reste sans vigilance particulière

# Contraintes :
# - 10 à 15 lignes maximum
# - Ton simple et utile
# - Ne dis pas que tu es une IA
# - N'invente aucune valeur

# Données météo :

# {resume_meteo}
# """
#         }
#     ]
# )

# print(response["message"]["content"])

import ollama

resume_meteo = """
Ville témoin : Rennes

Vigilance Météo-France : orange canicule
Indice UV : 8
Qualité de l'air : moyenne

Aujourd'hui :
- Température : 34.5°C
- Pluie : 0 mm
- Rafales : 34.6 km/h
- Risque local : faible
- Orage : non
- Brouillard : non

J+1 :
- Température : 30.9°C
- Pluie : 0 mm
- Rafales : 32.4 km/h

J+2 :
- Température : 28°C
- Pluie : 2 mm
- Rafales : 35 km/h

J+3 :
- Température : 26°C
- Pluie : 4 mm
- Rafales : 40 km/h
"""

response = ollama.chat(
    model="llama3.1:8b",
    messages=[
        {
            "role": "user",
            "content": f"""
Tu es un assistant météo français.

Rédige un résumé météo clair pour la ville témoin.

Structure :
1. Météo actuelle
2. Prévisions J+1, J+2, J+3
3. Conseils pratiques
4. Alerte danger si nécessaire

Règles d'alerte :
- Si vigilance Météo-France jauune ou orange ou rouge : commence par "⚠️ ALERTE MÉTÉO FRANCE"
- Si température > 32°C : signale un risque de forte chaleur / canicule
- Si température < -3°C : signale un risque de gel
- Si rafales > 70 km/h : signale un risque de vents violents
- Si rafales > 100 km/h : signale une tempête potentielle
- Si pluie > 20 mm : signale un risque de fortes pluies
- Si pluie > 50 mm : signale un risque d'inondation
- Si orage = oui : signale un risque orageux
- Si brouillard = oui : signale une visibilité réduite
- Si indice UV >= 7 : conseille une protection solaire
- Si qualité de l'air est mauvaise : conseille de limiter les efforts physiques
- Si aucun danger : indique que la situation reste sans vigilance particulière

Contraintes :
- Rédige exactement 4 paragraphes.
- Minimum 120 mots.
- Ne fais pas une seule phrase courte.
- Développe les conseils pratiques.
- Mentionne aujourd'hui, J+1, J+2 et J+3 séparément.
- 20 à 25 lignes minimum
- Ton simple, utile et professionnel
- Ne dis pas que tu es une IA
- N'invente aucune valeur absente
- Donne des conseils concrets pour les habitants

Données météo :

{resume_meteo}
"""
        }
    ]
)

print(response["message"]["content"])
