import geocoder
from dataclasses import dataclass

import config
from exceptions import CantGetCoordinates

IpOwner = 'me'

@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float

def get_coordinates() -> Coordinates:
    """Returns current coordinates using MacBook GPS"""
    coordinates = _get_geocoder_gps_coordinates()
    return _round_coordinates(coordinates)

def _get_geocoder_gps_coordinates() -> Coordinates:
    try:
        geocode = geocoder.ip(IpOwner)
    except Exception:
        raise CantGetCoordinates
    latitude, longitude = geocode.latlng
    if latitude is None or longitude is None:
        raise CantGetCoordinates
    return Coordinates(latitude=latitude, longitude=longitude)
   
def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(
            lambda coord: round(coord, 2),
            [coordinates.latitude, coordinates.longitude]
        ))

if __name__ == "__main__":
    print(get_coordinates())
