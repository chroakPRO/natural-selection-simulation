from enum import Enum
from GameConditions import GameCondition

class Weather(GameCondition):
    # super
    def __init__(self, name, description, icon, weather):
        super().__init__(name, description, icon)
        self.weather = weather
        self.weather_type = weather.get_weather_type()
        self.weather_description = weather.get_weather_description()
        self.weather_icon = weather.get_weather_icon()
    
    def get_weather_type(self):
        return self.weather_type
    
    def get_weather_description(self):
        return self.weather_description
    
    def get_weather_icon(self):
        return self.weather_icon

    def get_weather(self):
        return self.weather

    def set_weather(self, weather):
        self.weather = weather
        self.weather_type = weather.get_weather_type()
        self.weather_description = weather.get_weather_description()
        self.weather_icon = weather.get_weather_icon()

    
class WeatherTypes(Enum):
    HURRICANE = 0x01
    THUNDERSTORM = 0x02
    RAIN = 0x03
    SNOW = 0x04
    SUNNY = 0x05
    CLOUDY = 0x06
    DRIZZLE = 0x07
    FOG = 0x08
    HAZARDOUS_WEATHER = 0x09
    UNKNOWN = 0x0A