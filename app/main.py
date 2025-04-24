from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from fastapi import Request, HTTPException

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    now = datetime.now()
    birthday = datetime(year=2025, month=5, day=8, hour=0, minute=0, second=0)
    if now >= birthday:
        return templates.TemplateResponse("index.html", {"request": request, "opened": True})
    else:
        return templates.TemplateResponse("index.html", {"request": request, "opened": False})

@app.get("/test", response_class=HTMLResponse)
async def test_page(request: Request, targetDate: str = None):
    if targetDate is None:
        targetDate = datetime.now().isoformat() 

    try:
        target_datetime = datetime.fromisoformat(targetDate)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DDTHH:MM:SS format.")

    now = datetime.now()
    delta = target_datetime - now

    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds // 60) % 60
    seconds = delta.seconds % 60

    return templates.TemplateResponse('test.html', {
        'request': request,
        'target_date': target_datetime,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    })


@app.get("/countdown")
async def countdown():
    now = datetime.now()
    birthday = datetime(year=2025, month=5, day=8, hour=0, minute=0, second=0)
    delta = birthday - now
    return {
        "days": delta.days,
        "hours": delta.seconds // 3600,
        "minutes": (delta.seconds // 60) % 60,
        "seconds": delta.seconds % 60
    }
