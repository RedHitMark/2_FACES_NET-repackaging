from fastapi import FastAPI

from .routes import routes

app = FastAPI(
    title="2_FACES_NET-repackaging",
    openapi_url="/api/openapi.json")

app.include_router(routes.router, prefix='/api', tags=["api"])
