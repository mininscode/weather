import json
from pathlib import Path
from datetime import datetime
from typing import Protocol, TypedDict

from weather_api_service import Weather
from weather_formater import format_weather
from exceptions import HistoryStorageError


class WeatherStorage(Protocol):
    """Interface for any storage saving weather"""
    def save(self, weather: Weather) -> None:
        raise NotImplementedError

class HistoryRecord(TypedDict):
    date: str
    weather: str

class PlainFileWeatherStorage:
    """Store weather in plain text file"""
    def __init__(self, txt_file: Path):
        self._txt_file = txt_file

    def save(self, weather: Weather) -> None:
        current_time = datetime.now()
        formatted_weather = format_weather(weather)
        with open(self._txt_file, "a") as f:
            f.write(f"{current_time}\n{formatted_weather}\n")

class JSONFileWeatherStorage:
    """Store weather in JSON file"""
    def __init__(self, json_file: Path):
        self._json_file = json_file
        self._init_storage()

    def save(self, weather: Weather) -> None:
        history = self._read_history()
        history.append({
            "date": str(datetime.now()),
            "weather": format_weather(weather)
        })
        self._write(history)

    def _init_storage(self) -> None:
        if not self._json_file.exists():
            self._json_file.write_text("[]")

    def _read_history(self) -> list[HistoryRecord]:
        try:
            with open(self._json_file, "r") as f:
                return json.load(f)
        except EnvironmentError:
            raise HistoryStorageError

    def _write(self, history: list[HistoryRecord]) -> None:
        try:
            with open(self._json_file, "w") as f:
                json.dump(history, f, ensure_ascii=False, indent=4)
        except EnvironmentError:
            raise HistoryStorageError

def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    """Saves weather in the storage"""
    storage.save(weather)

