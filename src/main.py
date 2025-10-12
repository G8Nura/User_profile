from fastapi import FastAPI
from src.localities.router import router as LocalitiesRouter
from src.profile.router import router as ProfileRouter

app = FastAPI()

app.include_router(LocalitiesRouter)
app.include_router(ProfileRouter)

