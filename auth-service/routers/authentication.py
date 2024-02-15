from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sql import database, models
from utils import token, hashing

router = APIRouter(tags=['Authentication'])

@router.post("/login")
def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(database.get_db)):
    print("Request", request.username, request.password)
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    
    if not hashing.Hash.verify(request.password, user.password):
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    # Generate JWT Token
    access_token = token.create_access_token(
        data={"sub": user.email}
    ) 

    return {"access_token": access_token, "token_type": "bearer"}