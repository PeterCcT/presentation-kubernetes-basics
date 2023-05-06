from fastapi import APIRouter
from backend_app.routes.text_routes import router as text_routes

__routes = text_routes.routes

app_routes = APIRouter(routes=__routes)