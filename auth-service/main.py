from fastapi import FastAPI, Depends, HTTPException
from sql import models, schemas
from sql.database import engine, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def index():
    return {"message": "Auth Home page"}

@app.post("/create")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_exists = db.query(models.User).filter(models.User.email == user.email).first()

    if user_exists:
        raise HTTPException(status_code=400, detail="Email already registered")

    fake_hashed_password = user.password + "notreallyhashed"
    new_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users")
def all_users(db:Session = Depends(get_db)):
    users = db.query(models.User).all()

    return users