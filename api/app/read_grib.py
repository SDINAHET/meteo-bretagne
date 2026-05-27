import xarray as xr


def read_gfs_summary(path):
    ds = xr.open_dataset(path, engine="cfgrib")

    result = {
        "file": path,
        "variables": [],
    }

    for var in ds.data_vars:
        result["variables"].append({
            "name": var,
            "shape": list(ds[var].shape),
            "min": float(ds[var].min()),
            "max": float(ds[var].max()),
        })

    return result
