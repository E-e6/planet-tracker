from astral.sun import sun
from datetime import datetime
from skyfield.api import load, Topos
from astral import LocationInfo
import pytz

city = LocationInfo(
    name="Perth",
    region="Australia",
    timezone=pytz.timezone("Australia/Perth"),
    latitude=-31.9505,
    longitude=115.8605
)

# Load planetary data
planets = load('de421.bsp')
earth = planets['earth']
mercury = planets['mercury']
venus = planets['venus']
mars = planets['mars']
jupiter = planets['jupiter barycenter']
saturn = planets['saturn barycenter']

planet_list = {
    'Mercury': mercury,
    'Venus': venus,
    'Mars': mars,
    'Jupiter': jupiter,
    'Saturn': saturn
}

def get_planet_visibility(date):
    ts = load.timescale()
    # Convert 8 PM local Perth time to UTC
    perth_tz = pytz.timezone("Australia/Perth")
    local_time = perth_tz.localize(datetime(date.year, date.month, date.day, 20, 0, 0))
    utc_time = local_time.astimezone(pytz.utc)
    t = ts.utc(utc_time.year, utc_time.month, utc_time.day, utc_time.hour, utc_time.minute, utc_time.second)

    perth = earth + Topos(latitude_degrees=city.latitude, longitude_degrees=city.longitude)

    visible_planets = []

    for name, planet in planet_list.items():
        astrometric = perth.at(t).observe(planet)
        alt, az, distance = astrometric.apparent().altaz()
        altitude_deg = alt.degrees
        if altitude_deg > 0:
            visible_planets.append({"name": name, "altitude": round(altitude_deg, 2)})

    return visible_planets

def get_sun_times(date):
    s = sun(city.observer, date=date)
    sunrise = s['sunrise'].astimezone(city.timezone)
    sunset = s['sunset'].astimezone(city.timezone)
    return sunrise.strftime('%H:%M'), sunset.strftime('%H:%M')