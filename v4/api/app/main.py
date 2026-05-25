# # # # from fastapi import FastAPI

# # # # app = FastAPI(title="Météo Bretagne IA")

# # # # @app.get("/")
# # # # def home():
# # # #     return {"message": "API Météo Bretagne IA OK"}

# # # # @app.get("/meteo/rennes")
# # # # def meteo_rennes():
# # # #     return {
# # # #         "ville": "Rennes",
# # # #         "temperature": 12,
# # # #         "pluie_mm": 8,
# # # #         "rafales_kmh": 62,
# # # #         "risque": "modéré"
# # # #     }


# # # from fastapi import FastAPI
# # # import ollama

# # # app = FastAPI(title="Météo Bretagne IA")

# # # @app.get("/")
# # # def home():
# # #     return {"message": "API Météo Bretagne IA OK"}

# # # @app.get("/meteo/rennes")
# # # def meteo_rennes():
# # #     return {
# # #         "ville": "Rennes",
# # #         "temperature": 12,
# # #         "pluie_mm": 8,
# # #         "rafales_kmh": 62,
# # #         "risque": "modéré"
# # #     }

# # # @app.get("/meteo/rennes/resume")
# # # def resume_rennes():
# # #     meteo = """
# # #     Ville : Rennes
# # #     Température : 12°C
# # #     Pluie cumulée : 8 mm
# # #     Rafales : 62 km/h
# # #     Risque météo : modéré
# # #     """

# # #     response = ollama.chat(
# # #         model="llama3.1:8b",
# # #         messages=[
# # #             {
# # #                 "role": "user",
# # #                 "content": f"Explique cette prévision météo simplement en français : {meteo}"
# # #             }
# # #         ]
# # #     )

# # #     return {"resume": response["message"]["content"]}


# # from fastapi import FastAPI
# # import ollama

# # from scripts.analyse_meteo import analyse_meteo
# # from fastapi.middleware.cors import CORSMiddleware

# # app = FastAPI(title="Météo Bretagne IA")

# # app.add_middleware(
# #     CORSMiddleware,
# #     # allow_origins=["*"],
# #     allow_origins=[
# #         "http://localhost:5500",
# #         "http://127.0.0.1:5500",
# #     ],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # @app.get("/")
# # def home():
# #     return {"message": "API Météo Bretagne IA OK"}


# # @app.get("/meteo/rennes")
# # def meteo_rennes():
# #     return analyse_meteo()


# # # @app.get("/meteo/rennes/resume")
# # # def resume_rennes():
# # #     meteo = analyse_meteo()

# # #     prompt = f"""
# # #     Prévision météo Bretagne :

# # #     Ville : {meteo['ville']}
# # #     Température : {meteo['temperature']}°C
# # #     Pluie : {meteo['pluie_mm']} mm
# # #     Rafales : {meteo['rafales_kmh']} km/h
# # #     Risque : {meteo['risque']}

# # #     Explique simplement cette météo en français.
# # #     """

# # #     response = ollama.chat(
# # #         model="llama3.1:8b",
# # #         messages=[
# # #             {
# # #                 "role": "user",
# # #                 "content": prompt
# # #             }
# # #         ]
# # #     )

# # #     return {
# # #         "meteo": meteo,
# # #         "resume": response["message"]["content"]
# # #     }

# # @app.get("/meteo/rennes/resume")
# # def resume_rennes():
# #     meteo = analyse_meteo()

# #     prompt = f"""
# # Prévision météo Bretagne :

# # Ville : {meteo['ville']}
# # Température : {meteo['temperature']}°C
# # Pluie : {meteo['pluie_mm']} mm
# # Rafales : {meteo['rafales_kmh']} km/h
# # Risque : {meteo['risque']}

# # Explique simplement cette météo en français en 3 phrases maximum.
# # """

# #     try:
# #         response = ollama.generate(
# #             model="llama3.1:8b",
# #             prompt=prompt
# #         )

# #         return {
# #             "meteo": meteo,
# #             "resume": response["response"]
# #         }

# #     except Exception as e:
# #         return {
# #             "meteo": meteo,
# #             "resume": None,
# #             "error": str(e)
# #         }


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import requests
# import ollama

# from scripts.analyse_meteo import analyse_meteo

# app = FastAPI(title="Météo Bretagne IA")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:5500",
#         "http://127.0.0.1:5500",
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# VILLES_BRETAGNE = [
#     {"nom": "Rennes", "lat": 48.1173, "lon": -1.6778},
#     {"nom": "Brest", "lat": 48.3904, "lon": -4.4861},
#     {"nom": "Quimper", "lat": 47.9960, "lon": -4.1020},
#     {"nom": "Lorient", "lat": 47.7482, "lon": -3.3702},
#     {"nom": "Vannes", "lat": 47.6582, "lon": -2.7608},
#     {"nom": "Saint-Brieuc", "lat": 48.5142, "lon": -2.7658},
#     {"nom": "Saint-Malo", "lat": 48.6493, "lon": -2.0257},
#     {"nom": "Morlaix", "lat": 48.5775, "lon": -3.8270},
#     {"nom": "Redon", "lat": 47.6514, "lon": -2.0840},
#     {"nom": "Fougères", "lat": 48.3516, "lon": -1.1990},
# ]


# def calculer_risque(pluie_mm, rafales_kmh):
#     pluie = pluie_mm or 0
#     rafales = rafales_kmh or 0

#     if rafales >= 80 or pluie >= 20:
#         return "élevé"
#     if rafales >= 55 or pluie >= 5:
#         return "modéré"
#     return "faible"


# def recuperer_meteo_ville(ville):
#     url = (
#         "https://api.open-meteo.com/v1/meteofrance"
#         f"?latitude={ville['lat']}"
#         f"&longitude={ville['lon']}"
#         "&current=temperature_2m,precipitation,wind_gusts_10m,weather_code"
#         "&timezone=Europe%2FParis"
#     )

#     response = requests.get(url, timeout=10)
#     response.raise_for_status()

#     data = response.json()
#     current = data.get("current", {})

#     temperature = current.get("temperature_2m")
#     pluie = current.get("precipitation")
#     rafales = current.get("wind_gusts_10m")

#     return {
#         "ville": ville["nom"],
#         "lat": ville["lat"],
#         "lon": ville["lon"],
#         "temperature": temperature,
#         "pluie_mm": pluie,
#         "rafales_kmh": rafales,
#         "code_meteo": current.get("weather_code"),
#         "risque": calculer_risque(pluie, rafales),
#     }


# @app.get("/")
# def home():
#     return {"message": "API Météo Bretagne IA OK"}


# @app.get("/meteo/rennes")
# def meteo_rennes():
#     return recuperer_meteo_ville(
#         {"nom": "Rennes", "lat": 48.1173, "lon": -1.6778}
#     )


# @app.get("/api/meteo/bretagne")
# def meteo_bretagne():
#     resultats = []

#     for ville in VILLES_BRETAGNE:
#         try:
#             resultats.append(recuperer_meteo_ville(ville))
#         except Exception as e:
#             resultats.append({
#                 "ville": ville["nom"],
#                 "lat": ville["lat"],
#                 "lon": ville["lon"],
#                 "temperature": None,
#                 "pluie_mm": None,
#                 "rafales_kmh": None,
#                 "code_meteo": None,
#                 "risque": "indisponible",
#                 "error": str(e),
#             })

#     return resultats


# @app.get("/meteo/rennes/resume")
# def resume_rennes():
#     meteo = meteo_rennes()

#     prompt = f"""
# Prévision météo Bretagne :

# Ville : {meteo['ville']}
# Température : {meteo['temperature']}°C
# Pluie : {meteo['pluie_mm']} mm
# Rafales : {meteo['rafales_kmh']} km/h
# Risque : {meteo['risque']}

# Explique simplement cette météo en français en 3 phrases maximum.
# """

#     try:
#         response = ollama.generate(
#             model="llama3.1:8b",
#             prompt=prompt
#         )

#         return {
#             "meteo": meteo,
#             "resume": response["response"]
#         }

#     except Exception as e:
#         return {
#             "meteo": meteo,
#             "resume": None,
#             "error": str(e)
#         }


# from datetime import datetime, timedelta
from datetime import datetime, timedelta, timezone

import os
import ollama
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .cities import VILLES_BRETAGNE
from .database import Base, SessionLocal, engine
from .meteo_service import recuperer_meteo_bretagne, recuperer_meteo_ville
from .models import MeteoHistorique

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
ollama_client = ollama.Client(host=OLLAMA_HOST)

app = FastAPI(title="Météo Bretagne IA v4")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)



@app.get("/")
def home():
    return {"message": "API Météo Bretagne IA v4 OK"}


@app.get("/meteo/rennes")
def meteo_rennes():
    ville = {"nom": "Rennes", "lat": 48.1173, "lon": -1.6778}
    return recuperer_meteo_ville(ville)


@app.get("/api/meteo/bretagne")
def meteo_bretagne():
    return recuperer_meteo_bretagne()


@app.get("/meteo/bretagne")
def meteo_bretagne_alias():
    return recuperer_meteo_bretagne()


def sauvegarder_snapshot_meteo():
    db = SessionLocal()

    try:
        villes = recuperer_meteo_bretagne()

        for ville in villes:
            ligne = MeteoHistorique(
                ville=ville["ville"],
                lat=ville["lat"],
                lon=ville["lon"],
                temperature=ville["temperature"],
                pluie_mm=ville["pluie_mm"],
                rafales_kmh=ville["rafales_kmh"],
                code_meteo=ville["code_meteo"],
                risque=ville["risque"],
            )

            db.add(ligne)

        # limite = datetime.utcnow() - timedelta(hours=24)
        limite = datetime.now(timezone.utc) - timedelta(hours=24)

        db.query(MeteoHistorique).filter(
            MeteoHistorique.created_at < limite
        ).delete()

        db.commit()

    except Exception as e:
        db.rollback()
        print("Erreur sauvegarde météo :", e)

    finally:
        db.close()


@app.post("/api/meteo/refresh")
def refresh_meteo():
    sauvegarder_snapshot_meteo()
    return {"message": "Snapshot météo sauvegardé"}


@app.get("/api/meteo/historique/24h")
def historique_24h():
    db = SessionLocal()

    # limite = datetime.utcnow() - timedelta(hours=24)
    limite = datetime.now(timezone.utc) - timedelta(hours=24)

    lignes = db.query(MeteoHistorique).filter(
        MeteoHistorique.created_at >= limite
    ).order_by(MeteoHistorique.created_at.asc()).all()

    resultats = []

    for ligne in lignes:
        resultats.append({
            "ville": ligne.ville,
            "lat": ligne.lat,
            "lon": ligne.lon,
            "temperature": ligne.temperature,
            "pluie_mm": ligne.pluie_mm,
            "rafales_kmh": ligne.rafales_kmh,
            "code_meteo": ligne.code_meteo,
            "risque": ligne.risque,
            # "created_at": ligne.created_at.isoformat(),
            "created_at": ligne.created_at.astimezone(timezone.utc).isoformat(),
        })

    db.close()

    return resultats


@app.get("/api/meteo/previsions/bretagne")
def previsions_bretagne():
    resultats = []

    moments = {
        "matin": "08:00",
        "midi": "12:00",
        "apres-midi": "15:00",
        "soir": "20:00",
        "nuit": "23:00",
    }

    for ville in VILLES_BRETAGNE:
        url = (
            "https://api.open-meteo.com/v1/meteofrance"
            f"?latitude={ville['lat']}"
            f"&longitude={ville['lon']}"
            "&hourly=temperature_2m,precipitation,wind_gusts_10m,weather_code"
            "&forecast_days=4"
            "&timezone=Europe%2FParis"
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        hourly = data["hourly"]

        previsions = []

        for jour in range(1, 4):
            date_jour = hourly["time"][jour * 24].split("T")[0]

            for moment, heure in moments.items():
                cible = f"{date_jour}T{heure}"

                if cible in hourly["time"]:
                    index = hourly["time"].index(cible)

                    previsions.append({
                        "jour": f"J+{jour}",
                        "moment": moment,
                        "heure": cible,
                        "temperature": hourly["temperature_2m"][index],
                        "pluie_mm": hourly["precipitation"][index],
                        "rafales_kmh": hourly["wind_gusts_10m"][index],
                        "code_meteo": hourly["weather_code"][index],
                    })

        resultats.append({
            "ville": ville["nom"],
            "lat": ville["lat"],
            "lon": ville["lon"],
            "previsions": previsions,
        })

    return resultats


@app.get("/api/rainviewer/weather-maps")
def rainviewer_weather_maps():
    url = "https://api.rainviewer.com/public/weather-maps.json"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


@app.get("/meteo/rennes/resume")
def resume_rennes():
    meteo = meteo_rennes()

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
        response = ollama_client.generate(
            model="llama3.1:8b",
            prompt=prompt,
        )

        return {
            "meteo": meteo,
            "resume": response["response"],
        }

    except Exception as e:
        return {
            "meteo": meteo,
            "resume": None,
            "error": str(e),
        }


scheduler = BackgroundScheduler()
scheduler.add_job(sauvegarder_snapshot_meteo, "interval", minutes=15)
scheduler.add_job(sauvegarder_snapshot_meteo, "cron", minute="0,15,30,45")
scheduler.start()
