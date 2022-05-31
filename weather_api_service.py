from enum import Enum
from datetime import datetime
from dataclasses import dataclass

from gps_coordinates import Coordinates


Celsius = int

class WeatherType(str, Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморозь"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"

@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str

def get_weather(coordinates: Coordinates) -> Weather:
    """REquests weather in OpenWeather API and returns it"""
    return Weather(
        temperature=21,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2022-05-31 03:25:00"),
        sunset=datetime.fromisoformat("2022-05-31 20:38:00"),
        city="Nizhniy Novgorod"
    )

