from fastapi import FastAPI;
from fastapi.staticfiles import StaticFiles
from app.routes.routes import router as appRoutes
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return "Welcome to the crops+ backend"

app.include_router(appRoutes,prefix='/api')
