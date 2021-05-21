from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import routes

app = FastAPI(
    title="2_FACES_NET-repackaging",
    openapi_url="/api/openapi.json")

origins = [
    "http://localhost:3455",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router, prefix='/api', tags=["api"])
