# # from fastapi import FastAPI

# # app = FastAPI(title="Météo Bretagne IA")

# # @app.get("/")
# # def home():
# #     return {"message": "API Météo Bretagne IA OK"}

# # @app.get("/meteo/rennes")
# # def meteo_rennes():
# #     return {
# #         "ville": "Rennes",
# #         "temperature": 12,
# #         "pluie_mm": 8,
# #         "rafales_kmh": 62,
# #         "risque": "modéré"
# #     }


# from fastapi import FastAPI
# import ollama

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

# @app.get("/meteo/rennes/resume")
# def resume_rennes():
#     meteo = """
#     Ville : Rennes
#     Température : 12°C
#     Pluie cumulée : 8 mm
#     Rafales : 62 km/h
#     Risque météo : modéré
#     """

#     response = ollama.chat(
#         model="llama3.1:8b",
#         messages=[
#             {
#                 "role": "user",
#                 "content": f"Explique cette prévision météo simplement en français : {meteo}"
#             }
#         ]
#     )

#     return {"resume": response["message"]["content"]}


from fastapi import FastAPI
import ollama

from scripts.analyse_meteo import analyse_meteo
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Météo Bretagne IA")

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"],
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API Météo Bretagne IA OK"}


@app.get("/meteo/rennes")
def meteo_rennes():
    return analyse_meteo()


# @app.get("/meteo/rennes/resume")
# def resume_rennes():
#     meteo = analyse_meteo()

#     prompt = f"""
#     Prévision météo Bretagne :

#     Ville : {meteo['ville']}
#     Température : {meteo['temperature']}°C
#     Pluie : {meteo['pluie_mm']} mm
#     Rafales : {meteo['rafales_kmh']} km/h
#     Risque : {meteo['risque']}

#     Explique simplement cette météo en français.
#     """

#     response = ollama.chat(
#         model="llama3.1:8b",
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )

#     return {
#         "meteo": meteo,
#         "resume": response["message"]["content"]
#     }

@app.get("/meteo/rennes/resume")
def resume_rennes():
    meteo = analyse_meteo()

    prompt = f"""
Prévision météo Bretagne :

Ville : {meteo['ville']}
Température : {meteo['temperature']}°C
Pluie : {meteo['pluie_mm']} mm
Rafales : {meteo['rafales_kmh']} km/h
Risque : {meteo['risque']}

Explique simplement cette météo en français en 3 phrases maximum.
"""

    try:
        response = ollama.generate(
            model="llama3.1:8b",
            prompt=prompt
        )

        return {
            "meteo": meteo,
            "resume": response["response"]
        }

    except Exception as e:
        return {
            "meteo": meteo,
            "resume": None,
            "error": str(e)
        }
