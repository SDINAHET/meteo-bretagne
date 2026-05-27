"""
Analyse météo simple pour le projet Météo Bretagne IA.
Version MVP avec données simulées.
"""


def calcul_risque(temp, pluie_mm, rafales_kmh):
    """Calcule un niveau de risque météo simple."""
    score = 0

    if pluie_mm > 5:
        score += 2
    if pluie_mm > 15:
        score += 3
    if rafales_kmh > 50:
        score += 2
    if rafales_kmh > 80:
        score += 4
    if temp < 0:
        score += 2
    if temp > 30:
        score += 2

    if score >= 7:
        return "fort"

    if score >= 4:
        return "modéré"

    return "faible"


def analyse_meteo():
    """Retourne une prévision météo simulée pour Rennes."""
    temperature = 12
    pluie_mm = 8
    rafales_kmh = 62

    risque = calcul_risque(temperature, pluie_mm, rafales_kmh)

    return {
        "ville": "Rennes",
        "temperature": temperature,
        "pluie_mm": pluie_mm,
        "rafales_kmh": rafales_kmh,
        "risque": risque,
    }


if __name__ == "__main__":
    resultat = analyse_meteo()
    print(resultat)
