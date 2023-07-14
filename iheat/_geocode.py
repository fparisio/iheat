import geopandas as gpd


def _address2latlon(address: str) -> gpd.GeoDataFrame:
    """Geocode addresses to latlon coordinates.

    Parameters
    ----------
    address
        Address to geocode.

    Returns
    -------
    gpd.GeoDataFrame
        Geocoded address.
    """
    geocoded_addresses = gpd.tools.geocode(
        address, provider="nominatim", user_agent="autogis2022", timeout=10
    )
    lat, lon = (
        geocoded_addresses["geometry"].values[0].y,
        geocoded_addresses["geometry"].values[0].x,
    )
    return lat, lon
