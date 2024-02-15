from fastapi import APIRouter, Depends, status, HTTPException
from sql import schemas, database, models
from sqlalchemy.orm import Session
from utils.hashing import Hash

router = APIRouter(tags=['User'], prefix="/user")

@router.post("/create", response_model=schemas.User)
def create_user(request: schemas.UserCreate, db: Session = Depends(database.get_db)):
    user_exists = db.query(models.User).filter(models.User.email == request.email).first()

    if user_exists:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = models.User(email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/all", response_model=list[schemas.User])
def all_users(db:Session = Depends(database.get_db)):
    users = db.query(models.User).all()

    return users