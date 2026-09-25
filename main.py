from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from gemini_utils import get_home_recommendations


app = FastAPI(title="PocketSmart AI")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.post("/generate-home", response_class=HTMLResponse)
async def generate_home(
    request: Request,
    budget: float = Form(...),
    room: str = Form(...),
    style: str = Form(...),
    items: str = Form(...)
):

    recommendations = get_home_recommendations(
        budget=budget,
        room=room,
        style=style,
        items=items
    )

    return templates.TemplateResponse(
        request=request,
        name="home_recommendations.html",
        context={
            "recommendations": recommendations
        }
    )