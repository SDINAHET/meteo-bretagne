from datetime import datetime, timezone, timedelta
from pathlib import Path
import requests

DATA_DIR = Path("/app/data/grib")
DATA_DIR.mkdir(parents=True, exist_ok=True)


def latest_gfs_cycle_safe():
    now = datetime.now(timezone.utc) - timedelta(hours=9)
    cycle = (now.hour // 6) * 6
    return now.strftime("%Y%m%d"), f"{cycle:02d}"


def download_gfs_bretagne(forecast_hour=6):
    date, cycle = latest_gfs_cycle_safe()
    fff = f"{int(forecast_hour):03d}"

    params = {
        "dir": f"/gfs.{date}/{cycle}/atmos",
        "file": f"gfs.t{cycle}z.pgrb2.0p25.f{fff}",
        "lev_2_m_above_ground": "on",
        "lev_10_m_above_ground": "on",
        "lev_surface": "on",
        "var_TMP": "on",
        "var_GUST": "on",
        "var_APCP": "on",
        "subregion": "",
        # "leftlon": "-6",
        # "rightlon": "0",
        # "toplat": "50",
        # "bottomlat": "46",
        "leftlon": "-6",
        "rightlon": "10",
        "toplat": "52",
        "bottomlat": "41",
        "var_UGRD": "on",
        "var_VGRD": "on",
        "var_RH": "on",
        "var_PRMSL": "on",
        "lev_mean_sea_level": "on",
        "lev_entire_atmosphere": "on",
    }

    url = "https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl"

    output = DATA_DIR / f"gfs_bretagne_{date}_{cycle}_f{fff}.grib2"

    r = requests.get(url, params=params, timeout=120)
    r.raise_for_status()

    if not r.content.startswith(b"GRIB"):
        debug_file = DATA_DIR / "gfs_error_response.txt"
        debug_file.write_bytes(r.content)

        raise RuntimeError(
            f"Réponse NOAA invalide : {len(r.content)} octets. "
            f"Réponse sauvegardée dans {debug_file}. "
            f"URL testée : {r.url}"
        )

    output.write_bytes(r.content)

    return {
        "file": str(output),
        "date": date,
        "cycle": cycle,
        "forecast_hour": int(forecast_hour),
        "size_mb": round(output.stat().st_size / 1024 / 1024, 2),
        "url": r.url,
    }
