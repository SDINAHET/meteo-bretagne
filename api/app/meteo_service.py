import requests

from .cities import VILLES_BRETAGNE


def calculer_risque(pluie_mm, rafales_kmh):
    pluie = pluie_mm or 0
    rafales = rafales_kmh or 0

    if rafales >= 80 or pluie >= 20:
        return "élevé"

    if rafales >= 55 or pluie >= 5:
        return "modéré"

    return "faible"


def recuperer_meteo_ville(ville):
    url = (
        "https://api.open-meteo.com/v1/meteofrance"
        f"?latitude={ville['lat']}"
        f"&longitude={ville['lon']}"
        "&current=temperature_2m,precipitation,wind_gusts_10m,weather_code"
        "&timezone=Europe%2FParis"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    current = data.get("current", {})

    temperature = current.get("temperature_2m")
    pluie = current.get("precipitation")
    rafales = current.get("wind_gusts_10m")
    code_meteo = current.get("weather_code")
    actualise_le = current.get("time")

    return {
        "ville": ville["nom"],
        "lat": ville["lat"],
        "lon": ville["lon"],
        "temperature": temperature,
        "pluie_mm": pluie,
        "rafales_kmh": rafales,
        "code_meteo": code_meteo,
        "risque": calculer_risque(pluie, rafales),
        "actualise_le": actualise_le,
    }


def recuperer_meteo_bretagne():
    resultats = []

    for ville in VILLES_BRETAGNE:
        try:
            resultats.append(recuperer_meteo_ville(ville))
        except Exception as e:
            resultats.append({
                "ville": ville["nom"],
                "lat": ville["lat"],
                "lon": ville["lon"],
                "temperature": None,
                "pluie_mm": None,
                "rafales_kmh": None,
                "code_meteo": None,
                "risque": "indisponible",
                "error": str(e),
            })

    return resultats
