from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import planet_tracker  # Your custom module

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    today = datetime.now()
    sunrise, sunset = planet_tracker.get_sun_times(today)
    visible_planets = planet_tracker.get_planet_visibility(today)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "date": today.strftime("%Y-%m-%d"),
        "sunrise": sunrise,
        "sunset": sunset,
        "visible_planets": visible_planets
    })
