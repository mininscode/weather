USE_ROUNDED_COORDS = True
OPENWEATHER_API = "418c358901495031ad82968882ace829" # it is better to store in environment variables
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru&"
    "units=metric"
)
