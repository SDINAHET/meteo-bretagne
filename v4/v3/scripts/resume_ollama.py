import ollama

resume_meteo = """
Prévision Bretagne - Rennes :
Température : 12°C
Pluie cumulée : 8 mm
Rafales : 62 km/h
Risque météo : modéré
"""

response = ollama.chat(
    model="llama3.1:8b",
    messages=[
        {
            "role": "user",
            "content": f"""
Tu es un assistant météo français.
Explique simplement cette prévision météo pour un utilisateur :

{resume_meteo}
"""
        }
    ]
)

print(response["message"]["content"])
