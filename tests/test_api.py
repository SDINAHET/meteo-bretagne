from fastapi.testclient import TestClient
from api.app.main import app

client = TestClient(app)


def test_api_status():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_meteo_rennes():
    response = client.get("/meteo/rennes")
    assert response.status_code == 200
    data = response.json()

    assert data["ville"] == "Rennes"
    assert "temperature" in data
    assert "pluie_mm" in data
    assert "rafales_kmh" in data


def test_meteo_bretagne():
    response = client.get("/api/meteo/bretagne")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0
    assert "ville" in data[0]
    assert "temperature" in data[0]
