from fastapi import FastAPI
from sql import models
from sql.database import engine
from routers import authentication, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Auth Home page"}

app.include_router(authentication.router)
app.include_router(user.router)