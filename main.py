from fastapi import FastAPI;
from app.routes.routes import router as appRoutes;

app = FastAPI()


@app.get('/')
def root():
    return "Welcome to the crops+ backend"

app.include_router(appRoutes,prefix='/api')