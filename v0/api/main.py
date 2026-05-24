# from fastapi import FastAPI

# app = FastAPI(title="Météo Bretagne IA")

# @app.get("/")
# def home():
#     return {"message": "API Météo Bretagne IA OK"}

# @app.get("/meteo/rennes")
# def meteo_rennes():
#     return {
#         "ville": "Rennes",
#         "temperature": 12,
#         "pluie_mm": 8,
#         "rafales_kmh": 62,
#         "risque": "modéré"
#     }


from fastapi import FastAPI
import ollama

app = FastAPI(title="Météo Bretagne IA")

@app.get("/")
def home():
    return {"message": "API Météo Bretagne IA OK"}

@app.get("/meteo/rennes")
def meteo_rennes():
    return {
        "ville": "Rennes",
        "temperature": 12,
        "pluie_mm": 8,
        "rafales_kmh": 62,
        "risque": "modéré"
    }

@app.get("/meteo/rennes/resume")
def resume_rennes():
    meteo = """
    Ville : Rennes
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
                "content": f"Explique cette prévision météo simplement en français : {meteo}"
            }
        ]
    )

    return {"resume": response["message"]["content"]}
